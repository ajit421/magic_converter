encrypt = {
    "a": "~!@1$*2&*()",
    "b": "+_*ku?@,]^&",
    "c": "Abca3bh4c11",
    "d": "d1%2s0#445g",
    "e": "E7!+p9=qWw)",
    "f": "F=atyuio[pl",
    "g": "gZx$vb^*,./",
    "h": "Hjl;'658v3|",
    "i": "Iza_+@}}[]i",
    "j": "J1!q2#3e4r5",
    "k": "K6d+f8g9h66",
    "l": "zx=vbn=,./7",
    "m": "Maqws#drfjk",
    "n": "Ntui;p'[]:/",
    "o": "xzcv#,._/+n",
    "p": "P12qwe#r4@y",
    "q": "Qasd+hjklpd",
    "r": "Rxcv^nm@./l",
    "s": "S1!#2#3^%5+",
    "t": "&*()_+|i|=6",
    "u": "U6789q^erty",
    "v": "Vzcvbnma+df",
    "w": "1!qw#e4*t=%",
    "x": "Xyzu#opp[]^",
    "y": "Yhj@,.mn#bv",
    "z": "Zaws+cd$rf^",

    "1": "#$%#j^f5t6.",
    "2": ".@?/#.<'';f",
    "3": "6+7{tb6db'@",
    "4": ".2+{|*cwak}",
    "5": "^9n##**&#zv",
    "6": "+95^:[8z.~!",
    "7": "bhd8&&^^64&",
    "8": "!@#~-++vr2^",
    "9": "%3)n+1v\{^}",
    "0": "p.v@d**#aL=",
    
    " ": "*@/#|^v@,:d",
    ",": "0932hf*6%T@",
    ".": "89.:]+v$Ax~",
    "[": "09-?]Rjtc#5",
    "]": ".37]ercx#@!",
    "(": "$oNBG&*5VdQ",
    ")": "123.$%^&vfN",
    "-": "*&6#nMlP;?|",
    ";": "02@y%9Ol,Gr",
    "'": "-=Kmd$rAv@v",
    
    "!": "@_)bgD59*.?",
    "@": "34OjBC*-!vD",
    "#": "tybC$%^&*(2",
    "$": ";;$8@Xol.Sp",
    "%": "94vmJA@!9=.",
    "^": "wOPm,.:'@34",
    "&": "@%^&*jhVnXd",
    "*": "&*jGvX453.@",

}

# Decryption dictionary: 11-bit string -> char
decrypt = {v: k for k, v in encrypt.items()}
# the key becomes the 11-character encrypted string
