import data
import convertions
from cmd import Cmd
import rtlsdr

class Prompt(Cmd):
    
    def do_collect_data(self,args):
        """Collects data. Usage collect_data logatude latitude freqency sampleNumber"""
        pass
    
    def do_disableSDR(self,args):
        """Disables the RTLSDR so that it can safely be unpluged from your comp"""
        pass
    
    def do_enableSDR(self,args):
        """Enables the RTLSDR so that I/Q Data can be sampled from it"""
        pass
    
    def do_quit(self, args):
        """Quits the program."""
        print "Quitting."
        raise SystemExit
        

if __name__ == '__main__':
    prompt = Prompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting RadioLocator...')