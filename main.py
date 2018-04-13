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

    # ~~~ Basic commands ~~~
    def do_beep(self, arg):
        print('\b',end='')
    def do_print(self, arg):
        print(arg)

    # ~~~ Mathematical commands ~~
    def do_math(self, arg):
        arglist = arg.split()
        mathmode = arglist[0]
        try:
            if mathmode == "add":
                print(int(arglist[1]) + int(arglist[2]))
            elif mathmode == "subtract":
                print(int(arglist[1]) - int(arglist[2]))
            elif mathmode == "multiply":
                print(int(arglist[1]) * int(arglist[2]))
            elif mathmode == "divide":
                print(int(arglist[1]) / int(arglist[2]))
            elif mathmode == "modulo":
                print(int(arglist[1]) % int(arglist[2]))
            elif mathmode == "sin":
                print(math.sin(float(arglist[1])))
            elif mathmode == "cos":
                print(math.cos(float(arglist[1])))
            elif mathmode == "tan":
                print(math.tan(float(arglist[1])))
            elif mathmode == "sqrt":
                print(math.sqrt(float(arglist[1])))
            else:
                print("Invalid operation.")
        except ValueError:
            print("Invalid type or argument count.")

if __name__ == '__main__':
    SykeShell().cmdloop()