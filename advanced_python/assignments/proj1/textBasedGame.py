import cmd
from location import get_location
import textwrap

class Game(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = get_location(1)
        self.look()

    def move(self, dir):
        new_location = self.loc._neighbor(dir)
        if new_location is None:
            print("You are out of Manhattan")
        else:
            self.loc = get_location(new_location)
            self.look()

    def look(self):
        print(self.loc.name)
        print("")
        for line in textwrap.wrap(self.loc.description, 100):
            print(line)

    def do_n(self, args):
        '''Go North'''
        self.move('n')

    def do_s(self, args):
        '''Go South'''
        self.move('s')

    def do_w(self, args):
        '''Go West'''
        self.move('w')

    def do_e(self, args):
        '''Go East'''
        self.move('e')

    def do_quit(self, args):
        '''Leave the game'''
        print('Thank you for playing')
        return True

if __name__ == "__main__":
    g=Game()
    g.cmdloop()
