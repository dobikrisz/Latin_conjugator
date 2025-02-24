import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils
from typing import List

from tabulate import tabulate

noun_endings = {
    "I declension" : {
        "no spec ending" : {
            "singular" : {
                "nominative" : "ă",
                "vocative" : "ă",
                "accusative" : "ăm",
                "genetive" : "ae",
                "dative" : "ae",
                "ablative" : "ā"
            },
            "plural" : {
                "nominative" : "ae",
                "vocative" : "ae",
                "accusative" : "ās",
                "genetive" : "ārum",
                "dative" : "is",
                "ablative" : "is"
            }
        }
    },
    "II declension" : {
        "-us ending" : {
            "singular" : {
                "nominative" : "us",
                "vocative" : "e",
                "accusative" : "um",
                "genetive" : "i",
                "dative" : "o",
                "ablative" : "o"
            },
            "plural" : {
                "nominative" : "i",
                "vocative" : "i",
                "accusative" : "os",
                "genetive" : "ōrum",
                "dative" : "is",
                "ablative" : "is"
            }
        },
           "-er ending" : {
            "singular" : {
                "nominative" : "",
                "vocative" : "",
                "accusative" : "um",
                "genetive" : "i",
                "dative" : "o",
                "ablative" : "o"
            },
            "plural" : {
                "nominative" : "i",
                "vocative" : "i",
                "accusative" : "os",
                "genetive" : "ōrum",
                "dative" : "is",
                "ablative" : "is"
            }
        },
        "-um ending" : {
            "singular" : {
                "nominative" : "um",
                "vocative" : "um",
                "accusative" : "um",
                "genetive" : "i",
                "dative" : "o",
                "ablative" : "o"
            },
            "plural" : {
                "nominative" : "a",
                "vocative" : "a",
                "accusative" : "a",
                "genetive" : "ōrum",
                "dative" : "is",
                "ablative" : "is"
            }
        },
    }
}

def noun_conjugate(match, verbose = True):
    if not isinstance(match.dl_entry, pywords.definitions.DictlineNounEntry):
        raise TypeError("Word is not WordMatch noun. Cannot conjugate it")
    if type(verbose) is not bool:
        raise TypeError("The verbose parameter must be True/False")
    
    stem = match.dl_stem2 #ToDo: handle other stem conjugations
    decl_type = match.dl_entry.decl
    variant = match.dl_entry.variant

    declensions = {"1" : "I declension", "2" : "II declension", "3" : "III declension", "4" : "IV declension", "5" : "V declension"}
    declension = noun_endings.get(declensions[decl_type])
    if int(decl_type) == 2:
        endings = {"1" : "-us ending", "2" : "-um ending", "3" : "-er ending"}
    else:
        endings = {}
    ending = declension.get(endings.get(variant, "no spec ending"))
    
    result = []

    for mood, ne in ending["singular"].items():
        result.append(stem + ne)
    for mood, ne in ending["plural"].items():
        result.append(stem + ne)

    if verbose:
        headers = ["mood", "Singular", "plural"]
        list_of_moods = ["nominative", "vocative", "accusative", "genitive", "dative", "ablative"]
        table = []
        for i in range(0,6):
            table.append([list_of_moods[i], result[i], result[6+i]])

        print(tabulate(table, headers))
            

    return result