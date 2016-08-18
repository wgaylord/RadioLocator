import data
import convertions
from cmd import Cmd

class Prompt(Cmd):
    
    def do_collect_data(self,args):
        """Collects data Location,Freqency and Gain must be give as Args"""
        pass
    
    def do_disableSDR(self,args):
        pass
    
    def do_enableSDR(self,args):
        pass
    
    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit
        

if __name__ == '__main__':
    prompt = Prompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting RadioLocator...')