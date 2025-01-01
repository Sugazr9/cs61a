"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert isinstance(num_rolls, int), 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    score_for_roll = 0
    i = 0
    rolled_a_1 = 0
    for i in range(0, num_rolls):
        dice_value = dice()
        if dice_value == 1:
            rolled_a_1 += 1
        else:
            score_for_roll += dice_value
            i += 1
    if rolled_a_1 != 0:
        return 0
    else:
        return score_for_roll    
    # END Question 1


def is_prime(number):
    k = 2
    while k < number:
        if number % k == 0:
            return False
        k += 1
    if number < 2:
        return False
    return True


def next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        else:
            number += 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert isinstance(num_rolls, int), 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls == 0:
        score_turn = max((opponent_score % 10), (opponent_score // 10)) + 1
    else:
        score_turn = roll_dice(num_rolls, dice)
    if is_prime(score_turn):
        score_turn = next_prime(score_turn)
    return score_turn
    # END Question 2


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    score0 = score0 % 100
    score1 = score1 % 100
    if (score0 // 10 == score1 % 10) and (score0 % 10 == score1 // 10):
        return True
    return False
    # END Question 4


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        DiceType = select_dice(score0, score1)
        if player == 0:
            num_rolls = strategy0(score0, score1)
            score_for_turn = take_turn(num_rolls, score1, DiceType)
            if score_for_turn == 0:
                score1 += num_rolls
            score0 += score_for_turn
        else:
            num_rolls = strategy1(score1, score0)
            score_for_turn = take_turn(num_rolls, score0, DiceType)
            if score_for_turn == 0:
                score0 += num_rolls
            score1 += score_for_turn
        player = other(player)
        if is_swap(score0, score1):
            score0, score1 = score1, score0    
    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    def repetition(*args):
        k = 0
        total = 0
        for k in range(0, num_samples):
            total += fn(*args)
            k += 1
        return total/num_samples
    return repetition
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    roll_result = 1
    num_rolls = 1
    high_mark = 0
    while num_rolls < 11:
        mark = make_averaged(roll_dice, num_samples)(num_rolls, dice)
        if mark > high_mark:
            roll_result = num_rolls
            high_mark = mark
        num_rolls += 1
    return roll_result
    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(5)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))
    if True:
        print(make_averaged(roll_dice)(3, four_sided))
    if True:
        print(make_averaged(roll_dice)(6, six_sided))
    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    if take_turn(0, opponent_score) >= margin:
        return 0
    return num_rolls  # Replace this statement
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    if score < opponent_score:
        score_hypothetical = score + take_turn(0, opponent_score)
        if score_hypothetical == opponent_score:
            return num_rolls
        if is_swap(score_hypothetical, opponent_score):
            return 0
    return num_rolls  # Replace this statement
    # END Question 9


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    This program choose a number of dice to roll based on dice type and assesses if using the free bacon rule will be beneficial to the player (if 
    one can score more points with free bacon rule). It also assesses the user's situation and rolls if the situation is bad.Finally, the turn 
    shouldn't result in a hindering swine swap, so that is calculated and if a swap will occur, then the opposite approach is taken 
    (i.e. if rolling result in a swine swap, then not rolling is choosen).
    """
    # BEGIN Question 10
    DiceType = select_dice(score, opponent_score)
    if DiceType == four_sided:
        num_rolls = 0
        if bacon_strategy(score, opponent_score, 3, num_rolls) == 0 or swap_strategy(score, opponent_score, num_rolls) == 0:
            num_rolls = 0
    if DiceType == six_sided:
        num_rolls = 2
        if bacon_strategy(score, opponent_score, 3, num_rolls) == 0 or swap_strategy(score, opponent_score, num_rolls) == 0:
            num_rolls = 0
    if score > 92:
        num_rolls = bacon_strategy(score, opponent_score, 100 - score, num_rolls)
    if num_rolls != 0 and ((opponent_score - score) < 10 or (opponent_score + num_rolls >= 100)):
        num_rolls = 0
    if num_rolls == 0:
        score_hypothetical = score + take_turn(0, opponent_score)
        if is_swap(score_hypothetical, opponent_score):
            if DiceType == four_sided:
                num_rolls = 1
            if DiceType == six_sided:
                num_rolls = 2
    else:
        if DiceType == four_sided:
            score_hypothetical = score + 1
        else:
            score_hypothetical = score + 5
        if is_swap(score_hypothetical, opponent_score) and score_hypothetical > opponent_score:
            num_rolls = 0
    return num_rolls  # Replace this statement
    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
