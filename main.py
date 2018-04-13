##########################
# MAIN SCRIPT FOR PYSYKE #
##########################
# (C)2018                #
# Ben Sykes              #
##########################

# <<< Import libraries and custom modules >>>
import cmd
import os

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
            os.system("clear")

if __name__ == '__main__':
    SykeShell().cmdloop()