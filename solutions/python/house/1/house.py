phrases = [ "house that Jack built.",
            "malt that lay in ",
            "rat that ate " ,
            "cat that killed ",
            "dog that worried ",
            "cow with the crumpled horn that tossed ",
            "maiden all forlorn that milked ",
            "man all tattered and torn that kissed ",
            "priest all shaven and shorn that married ",
            "rooster that crowed in the morn that woke ",
            "farmer sowing his corn that kept ",
            "horse and the hound and the horn that belonged to " ]  

def recite(start_verse, end_verse):
    if start_verse == end_verse:
        body = "the ".join(phrases[0:end_verse][::-1])
        return [f"This is the {body}"]
    result = []
    for verse in range(start_verse,end_verse+1):
        result.extend(recite(verse, verse))
    return result