# Import all handlers for correspond with the users 
from .start import dp
from .help import dp
from .hello import dp
from .menu import dp
from .buttons import dp
from .inline_menu import dp

# This command must be in the end
from .error import dp 


__all__ = ['dp'] # list of allowd import parametrs