import random
from typing import List, Tuple

def roll_dice(qty: int, sides: int) -> int:
    """ 
    """
    result = 0
    for i in range(qty):
        result += random.randint(1,sides)
    return result

def roll_stats(method: int) -> List(int):
    """ The methods are those outlined in the AD&D 2E PHB
        Method I  : 3d6 in order
        Method II : 3d6 twice for each ability, keep the better one
        Method III: 3d6 assign as you wish (for this purpose, it is
                    effectively the same as Method I)
        Method IV : Roll 3d6 twelve times, keep best six scores,
                    assign as you wish
        Method V  : 4d6 drop lowest, assign as you wish,
                    a.k.a. the standard way
        Method VI : 8 for each ability, plus 7 dice you can
                    add to your abilities as you wish, although
                    you can't exceed 18.
    """
    assert method in range(1,7), "Unrecognized value for method"
    stats = []
    
    if method == 1:
        for i in range(6):
            stats.append(roll_dice(3,6))
        return stats
    
    if method == 5:
        for i in range(6):
            my_rolls = [roll_dice(1,6) for x in range(4)]
            my_rolls.sort()
    return
    