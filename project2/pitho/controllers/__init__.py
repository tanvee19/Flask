import os
import glob
__all__ = [os.path.basename(file)[:-3] for file in glob.glob(os.path.dirname(__file__)+"/*.py")]
#global trace the files one by one,__file__ return current directory
