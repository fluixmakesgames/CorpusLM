temps = {
    "the":{
        "man":[0.4],
        "cat":[0.5],
        "thing":[0.1],
        },
    "man":{
        "ate":[0.4],
        "did":[0.5],
        "died":[0.1],
        },
    "cat":{
        "ate":[0.3],
        "meowed":[0.6],
        "fell":[0.1],
        },
    "fell":{
        "off":[0.8],
        None:[0.2],
        },
    "ate":{
        "kibble":[1,"cat"],
        "a burger":[1,"man"],
        },
    "did":{
        "nothing":[0.2,],
        "not":[0.2,],
        "do":[0.2,],
        "something":[0.4,],
        },
    "didn't":{
        "win":[0.2,],
        "sleep":[0.2,],
        "do":[0.6,],
        },
    "do":{
        "the dishes":[0.5,],
        "their work":[0.5,],
        },
}

combines = {
    ("did", "not"): "didn't"
}

subjects = ["man","cat","thing"]
