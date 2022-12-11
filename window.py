from strategy import Strategy
from randomStrategy import random_for_group_of_prisoner
from followStrategy import follow_for_group_of_prisoner
from babyStepGiantStepStrategy import baby_step_giant_step_for_group_of_prisoner
from permutation import create_drawers
from tkinter import *

window = Tk()
window.withdraw()
window.title("Probability of success")
window.geometry("700x350")

strategy = Strategy.RANDOM
no_try = 0
probability = 0
no_of_success = 0
no_of_failure = 0
open = False
run = False

def process() :
    if run :
        run_strategy(strategy)
        update()
        window.after(0, process)

def start() :
    global run
    global start_button
    global end_button

    run = True
    start_button["state"] = DISABLED
    end_button["state"] = NORMAL
    process()

def end() :
    global run
    global start_button
    global end_button

    run = False
    start_button["state"] = NORMAL
    end_button["state"] = DISABLED

def update() :
    global no_try_label
    global no_try
    global probability_label
    global probability
    global no_of_success_label
    global no_of_success
    global no_of_failure_label
    global no_of_failure

    no_try_label.config(text = no_try)
    probability_label.config(text = probability)
    no_of_success_label.config(text = no_of_success)
    no_of_failure_label.config(text = no_of_failure)
    window.update()

def reset() :
    global no_try
    global probability
    global no_of_success
    global no_of_failure

    no_try = 0
    probability = 0
    no_of_success = 0
    no_of_failure = 0
    update()

def change_to_random() :
    global strategy
    global strategy_label

    if (strategy != Strategy.RANDOM) :
        reset()
        strategy = Strategy.RANDOM
        strategy_label.config(text = "RANDOM")
        update()

def change_to_follow() :
    global strategy
    global strategy_label

    if (strategy != Strategy.FOLLOW) :
        reset()
        strategy = Strategy.FOLLOW
        strategy_label.config(text = "FOLLOW")
        update()

def change_to_baby_step_giant_step() :
    global strategy
    global strategy_label

    if (strategy != Strategy.BABY_STEP_GIANT_STEP) :
        reset()
        strategy = Strategy.BABY_STEP_GIANT_STEP
        strategy_label.config(text = "BABY-STEP GIANT-STEP")
        update()

def run_strategy(strategy_name) :
    global no_try
    global no_of_success
    global no_of_failure
    global probability

    result = None
    if (strategy_name == Strategy.RANDOM) :
        result = random_for_group_of_prisoner(100, False)
    elif (strategy_name == Strategy.FOLLOW) :
        drawers = create_drawers(100)
        result = follow_for_group_of_prisoner(drawers, 100, False)
    else :
        result = baby_step_giant_step_for_group_of_prisoner(100, False)
    no_try += 1
    if result : no_of_success += 1
    else : no_of_failure += 1
    probability = round((no_of_success / no_try) * 100, 10)


strategy_bar = Menu(window)
strategy_bar.add_command(label = "Random Strategy", command = change_to_random)
strategy_bar.add_command(label = "Follow Strategy", command = change_to_follow)
strategy_bar.add_command(label = "Baby-Step Giant-Step Strategy", command = change_to_baby_step_giant_step)
window.config(menu = strategy_bar)

strategy_label = Label(window, text = "RANDOM", font = ("TkDefaultFont", 13, "bold"), pady = 20)
strategy_label.pack()

Label(window, text = "Number of tries").pack()
no_try_label = Label(window, text = no_try)
no_try_label.pack(anchor = CENTER)

Label(window, text = "Actual probability of success").pack()
probability_label = Label(window, text = probability)
probability_label.pack(anchor = CENTER, padx = 30)

Label(window, text = "Number of success").pack()
no_of_success_label = Label(window, text = no_of_success)
no_of_success_label.pack(anchor = CENTER)

Label(window, text = "Number of fails").pack()
no_of_failure_label = Label(window, text = no_of_failure)
no_of_failure_label.pack(anchor = CENTER)

start_button = Button(window, text = "Start", command = start)
start_button.pack(side = LEFT, anchor = E, expand = True)

end_button = Button(window, text = "End", command = end)
end_button["state"] = DISABLED
end_button.pack(side = RIGHT, anchor = W, expand = True)

def open_window() :
    global window
    window.deiconify()
    window.mainloop()