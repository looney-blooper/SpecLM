"""
Seed examples for smart-glasses intent/slot dataset.
Each entry: (raw_utterance, target_dict)
Used as few-shot templates for synthetic generation + as hand-labeled base set.
"""

SEEDS = {

    "photo": [
        ("take a photo", {"i": "photo"}),
        ("snap a pic", {"i": "photo"}),
        ("take a picture with the front camera", {"i": "photo", "s": {"state": "front"}}),
        ("switch to selfie cam and take a shot", {"i": "photo", "s": {"state": "front"}}),
        ("capture this", {"i": "photo"}),
        ("take a photo using the back camera", {"i": "photo", "s": {"state": "back"}}),
        ("get a picture of this", {"i": "photo"}),
    ],

    "video": [
        ("start recording", {"i": "video"}),
        ("record a video", {"i": "video"}),
        ("film this with the back camera", {"i": "video", "s": {"state": "back"}}),
        ("start a selfie video", {"i": "video", "s": {"state": "front"}}),
        ("capture a clip", {"i": "video"}),
        ("record what i'm seeing right now", {"i": "video"}),
    ],

    "call": [
        ("call mom", {"i": "call", "s": {"contact": "mom"}}),
        ("phone john", {"i": "call", "s": {"contact": "john"}}),
        ("dial sarah", {"i": "call", "s": {"contact": "sarah"}}),
        ("get my brother on the phone", {"i": "call", "s": {"contact": "brother"}}),
        ("ring up the office", {"i": "call", "s": {"contact": "office"}}),
        ("call dr. patel", {"i": "call", "s": {"contact": "dr. patel"}}),
        ("call", {"i": "unk"}),  # no contact given, ambiguous
    ],

    "msg": [
        ("text mom running late", {"i": "msg", "s": {"contact": "mom", "content": "running late"}}),
        ("send john i'm on my way", {"i": "msg", "s": {"contact": "john", "content": "i'm on my way"}}),
        ("message sarah be there in five", {"i": "msg", "s": {"contact": "sarah", "content": "be there in five"}}),
        ("text mom", {"i": "msg", "s": {"contact": "mom"}}),  # content missing, optional
        ("tell alex meeting moved to 3", {"i": "msg", "s": {"contact": "alex", "content": "meeting moved to 3"}}),
        ("send a message to dad call me when free", {"i": "msg", "s": {"contact": "dad", "content": "call me when free"}}),
    ],

    "nav": [
        ("navigate to starbucks", {"i": "nav", "s": {"loc": "starbucks"}}),
        ("directions home", {"i": "nav", "s": {"loc": "home"}}),
        ("take me to the airport", {"i": "nav", "s": {"loc": "airport"}}),
        ("how do i get to 123 main street", {"i": "nav", "s": {"loc": "123 main street"}}),
        ("navigate to the nearest gas station", {"i": "nav", "s": {"loc": "nearest gas station"}}),
        ("get me to work", {"i": "nav", "s": {"loc": "work"}}),
    ],

    "weather": [
        ("what's the weather", {"i": "weather"}),
        ("is it going to rain today", {"i": "weather", "s": {"time": "today"}}),
        ("weather in chicago", {"i": "weather", "s": {"loc": "chicago"}}),
        ("what's the forecast tomorrow", {"i": "weather", "s": {"time": "tomorrow"}}),
        ("do i need a jacket", {"i": "weather"}),
        ("weather in paris this weekend", {"i": "weather", "s": {"loc": "paris", "time": "weekend"}}),
    ],

    "setting": [
        ("turn off wifi", {"i": "setting", "s": {"device": "wifi", "state": "off"}}),
        ("turn on bluetooth", {"i": "setting", "s": {"device": "bluetooth", "state": "on"}}),
        ("lower the brightness", {"i": "setting", "s": {"device": "brightness", "state": "down"}}),
        ("mute notifications", {"i": "setting", "s": {"device": "notifications", "state": "off"}}),
        ("turn volume up", {"i": "setting", "s": {"device": "volume", "state": "up"}}),
        ("enable do not disturb", {"i": "setting", "s": {"device": "dnd", "state": "on"}}),
    ],

    "translate": [
        ("translate to spanish", {"i": "translate", "s": {"lang": "es"}}),
        ("what does this say in french", {"i": "translate", "s": {"lang": "fr"}}),
        ("translate this to hindi", {"i": "translate", "s": {"lang": "hi"}}),
        ("say this in german", {"i": "translate", "s": {"lang": "de"}}),
        ("translate to japanese", {"i": "translate", "s": {"lang": "ja"}}),
    ],

    "ocr": [
        ("read this sign", {"i": "ocr"}),
        ("what does this text say", {"i": "ocr"}),
        ("read this for me", {"i": "ocr"}),
        ("scan this menu", {"i": "ocr"}),
        ("what's written here", {"i": "ocr"}),
    ],

    "oos": [
        ("what's the capital of france", {"i": "oos"}),
        ("who won the game last night", {"i": "oos"}),
        ("tell me a joke", {"i": "oos"}),
        ("what's the meaning of life", {"i": "oos"}),
        ("how tall is mount everest", {"i": "oos"}),
        ("what's my horoscope today", {"i": "oos"}),
    ],

    "unk": [
        ("uh call the um", {"i": "unk"}),
        ("thing send message okay", {"i": "unk"}),
        ("weather no wait navigate", {"i": "unk"}),
        ("hey glasses do the", {"i": "unk"}),
        ("", {"i": "unk"}),  # empty/garbled ASR
    ],
}
