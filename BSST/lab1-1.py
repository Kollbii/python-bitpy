myChars1 = {
    6 : "$",
    7 :	"%",
    1 :	"*",
    12:	"+",    # e, o, i
    1:  "/",
    15:	"?",    # a
    5:	"A",
    5:	"E",
    2:	"H",
    5:	"K",
    5:	"L",
    1:	"M",
    9:	"N",
    3:	"P",
    12:	"Q",    # e, i, o
    2:	"R",
    3:	"S",
    3:	"T",
    6:	"V",
    2:	"W",
    2:	"X",
    7:	"Y",
    3:	"Z"
}

myChars2 = {
    5:	"A",
    6:	"B",
    6:	"C",
    4:	"D",
    4:	"E",
    3:	"F",
    3:	"J",
    5:	"K",
    3:	"L",
    3:	"M",
    2:	"N",
    10:	"O",    # a, e, i, o, u
    1:	"P",
    4:	"Q",
    6:	"R",
    1:	"S",
    6:	"U",
    8:	"W",    # a, e, i, o, u
    11:	"X",    # a, e, i, o, u
}

string1 = "P?A  S?YV%  +?XV?+NE  L+NZK  M%$%?SZ?WQYNE+$N  $TQ  PQLY  VE?SQ  WQ+HTQE+$N  H%$TQV?+  +RK?R+?  E/?K?AYQKNLYNAQ  PQ+NA%V?  YQALYX  +?L+NZK%V?$Q*%"
string2 = "WXQOWK LXCFRXBCXUAWJO R URXLXCFRXBCXUAWJO J AKAWXQOBM WXNXRUSDEQOWKBCUKBM FDEPACOQK UO NOLDEOWDEROBM"

if __name__ == '__main__':

    ciphertext = string1

    # STRING 1
    cipher = ["?", "$", "T", "Q", "A", "P", "L", "Y", "X", "+", "K","Z","L","Y","V","W","E","S","%","N","H","R","/","*"]
    alphabet = ["a", "n", "i", "e","k", "j", "s", "t", "u", "z", "r","f","L", "Y", "w","b","c","l","o","y","p","d","h","g"]
    decrypted = ""

    for element in ciphertext:
        if element == ' ':
            decrypted += " "
            continue
        elif element in cipher:
            decrypted += alphabet[cipher.index(element)]
        else:
            decrypted += element

    print(decrypted)
    decrypted = ""