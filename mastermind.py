from enum import Enum


goal = [4, 3, 2, 1]


class result(Enum):
    WRONG = 0
    CORRECT = 1
    WRONG_PLACE = 2


def evaluate(val, ind):
    if goal[ind] == val:
        return result.CORRECT
    else:
        if val in goal:
            return result.WRONG_PLACE
        else:
            return result.WRONG


# incorrect
def check(sequence):
    evaluation = [evaluate(guess[1], guess[0])
                  for guess in list(enumerate(sequence))]
    corrects = list(filter(lambda x: x == result.CORRECT, evaluation))
    wrong_place = list(filter(lambda x: x == result.WRONG_PLACE, evaluation))
    just_wrong = list(filter(lambda x: x == result.WRONG, evaluation))

    return corrects + wrong_place + just_wrong


print(list(check([3, 3, 9, 2])))
# NOT DONE
