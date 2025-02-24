import pywords.lookup as lookup  # The 'as lookup' part is optional, it creates an alias
import pywords.definitions
# Filtering is done with a MatchFilter
from pywords.matchfilter import MatchFilter
# utils has more specific tools for text analysis and generating vocab list files
import pywords.utils as pwutils
from typing import List

from tabulate import tabulate

verb_endings = {
    "active": {
        "indicative" : {
            "present" : {
                "conj_1" : {
                    "1st person singular" : "o",
                    "2nd person singular" : "as",
                    "3rd person singular" : "at",
                    "1st person plural" : "amus",
                    "2nd person plural" : "atis",
                    "3rd person plural" : "ant"
                },
                "conj_2" : {
                    "1st person singular" : "o",
                    "2nd person singular" : "es",
                    "3rd person singular" : "et",
                    "1st person plural" : "emus",
                    "2nd person plural" : "etis",
                    "3rd person plural" : "ent"
                },
                "conj_3" : {
                    "1st person singular" : "o",
                    "2nd person singular" : "is",
                    "3rd person singular" : "it",
                    "1st person plural" : "imus",
                    "2nd person plural" : "itis",
                    "3rd person plural" : "unt"
                },
                "mixed" : {
                    "1st person singular" : "io",
                    "2nd person singular" : "is",
                    "3rd person singular" : "at",
                    "1st person plural" : "imus",
                    "2nd person plural" : "itis",
                    "3rd person plural" : "unt"
                },
                "conj_4" : {
                    "1st person singular" : "io",
                    "2nd person singular" : "is",
                    "3rd person singular" : "it",
                    "1st person plural" : "imus",
                    "2nd person plural" : "itis",
                    "3rd person plural" : "unt"
                }
            },
            "perfect" :
            {

            },
            "imperfect" :
            {

            },
            "pluperfect" :
            {

            },
            "future" :
            {

            },
            "future perfect" :
            {

            }
        },
        "subjunctive" :
        {

        },
        "imperative" :
        {
            
        },
        "infinite" :
        {
            
        },
        "participio" :
        {
            
        },
        "gerundio" :
        {
            
        },
        "supin" :
        {
            
        }
    },
    "passive" :
    {

    }  
}

def verb_conjugate(match, form="active", mood="indicative", tense="present", verbose = True):
    if not isinstance(match.dl_entry, pywords.definitions.DictlineVerbEntry):
        raise TypeError("Word is not WordMatch verb. Cannot conjugate it")
    if form not in ["active", "passive"]:
        raise ValueError(r"%s is not a correct latin verb form" % (form))
    if mood not in ["indicative", "subjunctive", "imperative", "infinite", "participio", "gerundio", "supin"]:
        raise ValueError(r"%s is not a correct latin verb mood" % (mood))
    if tense not in ["present", "perfect", "imperfect", "pluperperfect", "future", "future perfect"]:
        raise ValueError(r"%s is not a correct latin tense" % (tense))
    if type(verbose) is not bool:
        raise TypeError("The verbose parameter must be True/False")
    
    stem = match.dl_stem2 #ToDo: handle other stem conjugations
    conj_type = match.dl_entry.conj

    result = []
    table = [["person", "verb"]]

    for person, ve in verb_endings[form][mood][tense]["conj_"+conj_type].items():
        result.append(stem + ve)
        table.append([person, stem + ve])

    if verbose:
        print(tabulate(table, headers="firstrow"))

    return result
            

     