import sys
from enigmas import enigmas


def main(args=sys.argv[1:]):
    SETTINGS = [
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"]
    ]
    WALZEN = [
        2,
        1,
        0,
        5,
        6
    ]
    STECKBRETT = [
    ]
    ENIGMA = enigmas.Enigma_I.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print( ENIGMA.enc_string("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") )


# Call the main function at the end of the file
main()