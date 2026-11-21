"""
Core schema for the smart-glasses SLM dataset.

Two levels of validation:
  - TrainingTarget: the minified {"i": ..., "s": {...}} the model must output
  - DatasetRecord: the full record (utterance + target) used pre-flattening
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, model_validator


class Intent(str, Enum):
    PHOTO = "photo"
    VIDEO = "video"
    CALL = "call"
    MSG = "msg"
    NAV = "nav"
    WEATHER = "weather"
    SETTING = "setting"
    TRANSLATE = "translate"
    OCR = "ocr"
    OOS = "oos"   # out of scope -> handoff to phone/cloud
    UNK = "unk"   # heard something, couldn't parse (ASR garble, ambiguous, empty)


# Which slots each intent is allowed / required to use.
# Anything not listed here is disallowed for that intent.
REQUIRED_SLOTS: dict[Intent, set[str]] = {
    Intent.CALL: {"contact"},
    Intent.MSG: {"contact"},
    Intent.NAV: {"loc"},
    Intent.SETTING: {"device", "state"},
    Intent.TRANSLATE: {"lang"},
}

OPTIONAL_SLOTS: dict[Intent, set[str]] = {
    Intent.PHOTO: {"state"},          # front / back camera
    Intent.VIDEO: {"state"},          # front / back camera
    Intent.MSG: {"content"},          # message body, may be omitted
    Intent.WEATHER: {"loc", "time"},
}

# Closed vocabularies for slots that shouldn't be free text.
# Enforced in the validator below; extend as your hardware/task list grows.
CLOSED_SLOT_VALUES: dict[str, set[str]] = {
    "lang": {"es", "fr", "hi", "de", "ja", "zh", "ar", "pt", "ru", "ko","ta"},
    "device": {"wifi", "bluetooth", "brightness", "notifications", "volume", "dnd"},
    "state": {"on", "off", "up", "down", "front", "back"},
}


class Slots(BaseModel):
    contact: Optional[str] = None
    loc: Optional[str] = None
    time: Optional[str] = None
    lang: Optional[str] = None
    device: Optional[str] = None
    state: Optional[str] = None
    content: Optional[str] = None

    model_config = {"extra": "forbid"}




class TrainingTarget(BaseModel):
    """The minified {"i": ..., "s": {...}} the decoder must generate."""

    i: Intent                       #Intent
    s: Optional[Slots] = None       #Slots

    model_config = {"extra": "forbid"}

    @model_validator(mode="after")
    def validate_slots(self):
        """
            checks if:
                1. all required slots are parsed
                2. no extra/unwanted slots are parsed
        """
        allowed = REQUIRED_SLOTS.get(self.i, set()) | OPTIONAL_SLOTS.get(self.i, set())
        required = REQUIRED_SLOTS.get(self.i, set())

        present = {}
        if self.s is not None:
            present = {k: v for k, v in self.s.model_dump().items() if v is not None}

        extra = set(present.keys()) - allowed
        if extra:
            raise ValueError(f"intent '{self.i.value}' got disallowed slots: {extra}")

        missing = required - set(present.keys())
        if missing:
            raise ValueError(f"intent '{self.i.value}' missing required slots: {missing}")

        for key, value in present.items():
            closed_set = CLOSED_SLOT_VALUES.get(key)
            if closed_set is not None and value not in closed_set:
                raise ValueError(
                    f"slot '{key}' got value '{value}' outside closed set {closed_set}"
                )

        return self

    def to_minified_json(self) -> str:
        """Compact JSON string, no whitespace, for token budget."""
        return self.model_dump_json(exclude_none=True)




class DatasetRecord(BaseModel):
    """A single generated example before flattening into a training sequence."""

    utterance: str
    target: TrainingTarget

    # generation provenance, useful for debugging/filtering later
    source: str = "synthetic"   # "synthetic" | "seed" | "human"
    is_asr_noisy: bool = False

    model_config = {"extra": "forbid"}

    @model_validator(mode="after")
    def validate_utterance(self):
        if self.target.i == Intent.UNK:
            return self  # unk allows empty/garbled utterances
        if not self.utterance.strip():
            raise ValueError("non-unk intent cannot have an empty utterance")
        return self
