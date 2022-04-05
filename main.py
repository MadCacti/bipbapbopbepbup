# import needed procedures, with ["name", "name.py"]
from procedures import submenus
from procedures.week1.database import *
from procedures.week2.lcm import *

# Create all menus/submenus accordingly
main_menu = [
  ["change the colors", "procedures/week3/color.py"]
]

sub_menu = [
    ["tree", "procedures/week0/tree.py"],
    ["biker", "procedures/week0/biker.py"],
]

math_sub_menu = [
    ["decimal/binary converter", "procedures/week3/decBinConverter.py"],
    ["matrix", "procedures/week0/matrix.py"],
    ["swap", "procedures/week0/swap.py"],
    ["fibonacci", "procedures/week1/fibonacci.py"],
    ["factorial", "procedures/week2/factorial.py"],
    ["least common mulitple", "procedures/week2/lcm.py"]
]

misc_sub_menu = [
    ["number guesser", "procedures/week3/numGuesser.py"],
    ["rock, paper, scissors", "procedures/week3/rockPaperScissors.py"],
    ["database", "procedures/week1/database.py"],
    ["palindrome", "procedures/week2/palindrome.py"]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nchoose one\n{border}"


# menu blueprint
def menu():
    title = "menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["patterns", submenu])
    menu_list.append(["math", math_submenu])
    menu_list.append(["misc", misc_submenu])
    buildMenu(title, menu_list)

def submenuc(): # establish each blueprint, the rest are just duplicates
    title = "submenu" + banner
    m = submenus.Menu(title, sub_menu)
    m.menu()

def submenu():
    title = "submenu" + banner
    buildMenu(title, sub_menu)

def math_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, math_sub_menu)
    m.menu()

def math_submenu():
    title = "submenu" + banner
    buildMenu(title, math_sub_menu)

def misc_submenuc():
    title = "submenu" + banner
    m = submenus.Menu(title, misc_sub_menu)
    m.menu()

def misc_submenu():
    title = "submenu" + banner
    buildMenu(title, misc_sub_menu)
  
# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("input your choice: ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"file not found!: {action}")
                print()
    except ValueError:
        # not a number
        print(f"not a number: {choice}")
        print()
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"invalid choice: {choice}")
        print()

    buildMenu(banner, options)

if __name__ == "__main__":
    menu()