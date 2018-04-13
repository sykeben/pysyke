##########################
# MAIN SCRIPT FOR PYSYKE #
##########################
# (C)2018                #
# Ben Sykes              #
##########################


# <<< Import libraries and custom modules >>>
import cmd
import os
import math
import prettytable


# <<< Define the "SykeShell" class >>>
class SykeShell(cmd.Cmd):
    intro = 'Welcome to SykeShell, the shell for PySyke\n'
    prompt = '>-=> '
    file = None


    # ~~~ Core commands ~~~
    def do_quit(self, arg):
        quit()
    def do_clear(self, arg):
        # Try to clear the screen
        try:
            os.system("cls")
        except:
            try:
                os.system("clear")
            except:
                print("An error occurred.")
    def do_credits(self, arg):
        # Print the credits
        print("")
        print("-=< PYSYKE DEVELOPER >=-")
        print("* Benjamin Sykes")
        print("")
        print("-=< SPECIAL THANKS >=-")
        print("* JetBrains")
        print("* Nicholis Hubbard")
        print("")


    # ~~~ Basic commands ~~~
    def do_beep(self, arg):
        # Print a bell character
        print('\b',end='')
    def do_print(self, arg):
        # Print the argument(s) inputted
        print(arg)


    # ~~~ Mathematical commands ~~
    def do_calc(self, arg):
        # SPECIAL THANKS TO NICHOLIS HUBBARD :)
        try:
            # Attempt to split the args into a list
            arglist = arg.split()
            mathmode = arglist[0]
            try:
                # Calculate accordingly
                if mathmode == "help":
                    # Print help info
                    print("Math Commands:")
                    print(" add       subtract  multiply")
                    print(" divide    module    sin")
                    print(" cos       tan       sqrt")
                elif mathmode == "add":
                    # Add
                    print(int(arglist[1]) + int(arglist[2]))
                elif mathmode == "subtract":
                    # Subtract
                    print(int(arglist[1]) - int(arglist[2]))
                elif mathmode == "multiply":
                    # Multiply
                    print(int(arglist[1]) * int(arglist[2]))
                elif mathmode == "divide":
                    # Divide
                    print(int(arglist[1]) / int(arglist[2]))
                elif mathmode == "modulo":
                    # Modulo (Calculate remainder)
                    print(int(arglist[1]) % int(arglist[2]))
                elif mathmode == "sin":
                    # Calculate sine
                    print(math.sin(float(arglist[1])))
                elif mathmode == "cos":
                    # Calculate cosine
                    print(math.cos(float(arglist[1])))
                elif mathmode == "tan":
                    # Calculate tangent
                    print(math.tan(float(arglist[1])))
                elif mathmode == "sqrt":
                    # Calculate square root
                    print(math.sqrt(float(arglist[1])))
                else:
                    # Print error
                    print("Invalid operation.")
            except:
                # Print error
                print("Invalid type or argument count.")
        except:
            # Print error
            print("An error has occurred.")
    def do_eval(self, arg):
        # Attempt to calculate
        try:
            print(eval(arg))
        except:
            print("Formatting error or mismatch.")
    def do_itable(self, arg):
        # Get the command
        print("Enter an expression with x as the variable (E.G. \"3x+5\"):")
        tablecalc = input(">>> ")
        print("Checking . . . ", end='')
        try:
            x = 1
            eval(tablecalc)
            print("Done.")
        except:
            print("ERROR!")
            return
        print("Enter the starting point:")
        try:
            startpoint = float(input(">>> "))
        except:
            print("Invalid type.")
            return
        print("Enter the increment value:")
        try:
            increment = float(input(">>> "))
        except:
            print("Invalid type.")
            return
        print("Enter the amount of increments to do:")
        try:
            amount = int(input(">>> "))
        except:
            print("Invalid type.")
            return
        print("Please wait, calculating . . . ")
        calctable = prettytable.PrettyTable(['X', 'Result'])
        n = 0
        while n < amount:
            n += 1
            x = (increment * n) + startpoint
            calctable.add_row([x, eval(tablecalc)])

if __name__ == '__main__':
    SykeShell().cmdloop()