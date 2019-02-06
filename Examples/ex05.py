import re as regex
import sys

txt = 'my name is vinod and i live in bangalore'
x = regex.sub("vinod", "Vinod Kumar", regex.sub("bangalore", "Bengaluru", txt))

