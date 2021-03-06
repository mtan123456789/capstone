import Levenshtein
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_language( search_value ):
    dmin = sys.maxsize
    lang = "None"
    with open("./static/txt/languages.txt") as f:
        for line in f:
            if search_value is not None: 
                for word in search_value.split( ):
                    dis = Levenshtein.distance(line.strip().lower(),word.strip().lower())
                    if dis < dmin:
                        lang = line.strip().lower()
                        dmin = dis
        if dmin < 3:
            return lang
        return None
    
def get_command( search_value ):
    dmin = 0
    comm = "None"
    with open("./static/txt/commands.txt") as f:
        for line in f:
            dis = fuzz.partial_ratio(line.strip().lower(),search_value.strip().lower())
            if dis > dmin:
                comm = line.strip().lower()
                dmin = dis
        if dmin > 60:
            return comm
        return None

