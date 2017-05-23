p=0.4
import math
def entropy_cal(val):
    log = math.log2(val)
    entropy = -val * log
    return entropy

print(entropy_cal(p))

