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


# <<< Define the "SykeShell" class >>>

class SykeShell(cmd.Cmd):

    # ~~~ Definitions ~~~
    intro = 'Welcome to SykeShell, the shell for PySyke\n'
    prompt = '>-=> '
    file = None
    def default(self, line):
        print("ERROR! Invalid command: " + line)


    # ~~~ Core commands ~~~

    def do_quit(self, arg):
        quit()
    def help_quit(self):
        print("Quit SykeShell, then PySyke.")

    def do_clear(self, arg):
        # Try to clear the screen
        try:
            os.system("cls")
        except:
            try:
                os.system("clear")
            except:
                print("An error occurred.")
    def help_clear(self):
        print("Attempt to clear the screen (Should work on Windows and Linux/UNIX).")

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
    def help_credits(self):
        print("Shows the credits for your current version of PySyke SykeShell.")


    # ~~~ Basic commands ~~~

    def do_beep(self, arg):
        # Print a bell character
        print('\b',end='')
    def help_beep(self):
        print("Attempts to beep by printing the bell character.")

    def do_print(self, arg):
        # Print the argument(s) inputted
        print(arg)
    def help_print(self):
        print("Prints the text supplied to the console.")
        print("SYNTAX: print [text]")


    # ~~~ Mathematical commands ~~~

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
    def help_calc(self):
        print("Performs a calculation with 1-2 numbers.")
        print("SYNTAX: calc [sub-command] [num1] ([num2])")
        print("Run calc's \"help\" command to list sub-commands.")

    def do_eval(self, arg):
        # Attempt to calculate
        try:
            print(eval(arg))
        except:
            print("Formatting error or mismatch.")
    def help_eval(self):
        print("Evaluate an expression.")
        print("SYNTAX: eval [expression]")


# <<< Start the "cmdloop" >>>

if __name__ == '__main__':
    try:
        # Try the "cmdloop"
        SykeShell().cmdloop()
    except:
        # If it exits or fails, let the user know
        print("Well, something happened or you exited.")
        print("Goodbye!")