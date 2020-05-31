from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."

knowledge0 = And(
    Or(AKnight, AKnave),
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    Implication(AKnight, BKnight),
    Implication(BKnight, AKnave),
    Implication(AKnave, BKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)),
    Implication(BKnight, And(Not(AKnave), Not(AKnight))),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnave, AKnave)
)

# Puzzle 4
# A says B is knave.
# B says neither A nor I are knaves.
knowledge4 = And(
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    Biconditional(AKnight, BKnave),
    Implication(BKnight, And(Not(AKnave), Not(BKnave)))
)

# Puzzle 5
# A tells you that “of B and I, exactly one is a knight'.
# B tells you that only a knave would say that A is a knave.
knowledge5 = And(
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    Implication(AKnight, Not(BKnight)),
    Biconditional(BKnight, Not(AKnave))
)

# Puzzle 6
# A tells you, “At least one of the following is true: that I am a knight or that B is a knight.
# B claims, “A could say that I am a knave.
knowledge6 = And(
    And(Or(AKnight, AKnave), Or(BKnave, BKnight)),
    Implication(BKnight, AKnave),
    Biconditional(BKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
        ("Puzzle 4", knowledge4),
        ("Puzzle 5", knowledge5),
        ("Puzzle 6", knowledge6)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
