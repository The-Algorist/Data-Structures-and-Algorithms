# Function to split a Camel Case string into words
import re

def process_string(s):
    if not s:
        return ""

    parts = s.strip().split(";")
    if len(parts) != 3:
        return ""

    sc, mcv, op = parts
    if sc not in {"S", "C"} or mcv not in {"M", "C", "V"} or not op:
        return ""

    if sc == "S":
        if mcv == "M":
            cap = op[:-2]
        else:
            cap = op

        s = re.sub(r"(\w)([A-Z])", r"\1 \2", cap)
        return s.lower()

    if sc == "C":
        cap = op.title()
        s = re.sub(r" ", r"", cap)
        q = s[:1].lower() + s[1:]

        if mcv == "M":
            return q + "()"
        elif mcv == "C":
            return s
        else:
            return q

while True:
    try:
        s = input()
        result = process_string(s)
        if result:
            print(result)
    except EOFError:
        break
