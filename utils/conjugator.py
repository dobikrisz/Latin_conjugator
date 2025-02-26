import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils

from tabulate import tabulate
import pandas as pd

inflections = pd.read_csv('./PyWORDS/pywords/data/INFLECTS.tsv', sep='\t', header=0)

def verb_conjugator(match, form="ACTIVE", mood="IND", tense="PRES", verbose=True):
    if not isinstance(match.dl_entry, pywords.definitions.DictlineVerbEntry):
        raise TypeError("Word is not WordMatch verb. Cannot conjugate it")
    if form not in ["ACTIVE", "PASSIVE"]:
        raise ValueError(r"%s is not a correct latin verb form" % (form))
    if mood not in ["IND", "SUB", "IMP", "INF", "PAR", "GER", "SUPINE"]:
        raise ValueError(r"%s is not a correct latin verb mood" % (mood))
    if tense not in ["PRE", "PER", "IMPF", "pluperperfect", "FUT", "PERF"]:
        raise ValueError(r"%s is not a correct latin tense" % (tense))
    if type(verbose) is not bool:
        raise TypeError("The verbose parameter must be True/False")
    
    infl_type = match.dl_entry.conj
    variant = match.dl_entry.variant
    
    
    
