# lookup is the main module
import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils

from utils.verb_conjugation import verb_conjugate
from utils.noun_conjugation import noun_conjugate

word = 'bibit'

for match in lookup.match_word(word): # Match possible words
    print(match)
    print("\n")
    if isinstance(match.dl_entry, pywords.definitions.DictlineVerbEntry):
        verb_conjugate(match)
    elif isinstance(match.dl_entry, pywords.definitions.DictlineNounEntry):
        noun_conjugate(match)
