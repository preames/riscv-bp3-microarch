

import os
template = os.path.join(os.path.dirname(__file__), 'template.s')

def is_valid_combination(SEW, LMUL):
    # Hard coded for VLEN=256 (i.e. bp3)
    if SEW == "e64":
        return LMUL != "mf8";
    return True

with open(template, "r") as f:
    template = f.read()

    for SEW in ["e8", "e16", "e32", "e64"]:
        for LMUL in ["mf8", "mf4", "mf2", "m1", "m2", "m4", "m8"]:
            if not is_valid_combination(SEW, LMUL):
                continue
            s = template;
            s = s.replace("PARAM_LMUL", LMUL);
            s = s.replace("PARAM_SEW", SEW);
            name = "vadd-vv-" + SEW + "_" + LMUL + "_vlmax.s"
            print ("Generating " + name)
            with open(name, "w") as of:
                of.write(s);
