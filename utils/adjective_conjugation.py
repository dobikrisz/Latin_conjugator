import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils
from typing import List

from tabulate import tabulate


adjective_endings = {
    
}