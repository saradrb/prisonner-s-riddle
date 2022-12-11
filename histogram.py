import matplotlib.pyplot as plt
from strategy import Strategy
from randomStrategy import random_for_group_of_prisoner
from followStrategy import follow_for_group_of_prisoner
from babyStepGiantStepStrategy import baby_step_giant_step_for_group_of_prisoner
from permutation import create_drawers

def create_histogram(strategy_name, number_of_try, tab_result):
    left = [0,number_of_try]
    tick_label = ['fails', 'success']

    plt.bar(left, tab_result, tick_label = tick_label, width = 10, color = ['red', 'green'])
    plt.xlabel('Results')
    plt.ylabel('Number of tries')
    if (strategy_name == Strategy.RANDOM) : plt.title('Prisonners Random Strat')
    elif (strategy_name == Strategy.FOLLOW) : plt.title('Prisonners Follow Strat')
    else : plt.title('Prisonners Baby-Step Giant-Step Strat')
    plt.show()

def how_many_tries_to_solve_strategy(strategy_name, len, print_msg, try_test):
    i, j, k = 0, 0, 0
    while (k < try_test):
        if (strategy_name == Strategy.RANDOM) :
            result = random_for_group_of_prisoner(len, print_msg)
        elif (strategy_name == Strategy.FOLLOW) :
            result = follow_for_group_of_prisoner(create_drawers(len), len, print_msg)
        else :
            result = baby_step_giant_step_for_group_of_prisoner(len, print_msg)

        if (result == False): i += 1
        else: j+= 1
        k += 1
    create_histogram(strategy_name, try_test, [i, j])