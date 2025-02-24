# lookup is the main module
import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils

from utils.verb_conjugation import conjugate

word = 'capio'

for match in lookup.match_word(word): # Match possible words
    print(match)
    if isinstance(match.dl_entry, pywords.definitions.DictlineVerbEntry):
        conjugate(match)
