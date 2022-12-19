# Function for parsing the 'cmt' value from the debug info
def parse_cmt(debug_info: str) -> float:

    try:

        cmt_unparsed = debug_info.split("cmt\": \"")[1]

        if len(cmt_unparsed) == 0:

            return 0

        cmt = float(cmt_unparsed.split("\"")[0])

    except Exception:

        cmt = 0

    return cmt

def get_modifier_value(modifier: str):
    
    modifier_value = 0.0

    if modifier != "":

        division = modifier.split("/")

        if len(division) < 2:

            numerator = division[0]
            denominator = 1
            
        else:

            numerator = division[0]
            denominator = division[1]

        try:

            modifier_value = (float(numerator) / float(denominator))

        except ZeroDivisionError:

            pass

    return modifier_value