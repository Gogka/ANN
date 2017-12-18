
from ANNLayer import *

if __name__ == "__main__":
    layer = ANNLayer([1, 2, 3], 3)
    for outputs in layer.get_outputs():
        print outputs