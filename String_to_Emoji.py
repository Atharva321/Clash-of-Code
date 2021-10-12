import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()
emojis = {
    ":slight_smile:":  ":)",
    ":slight_smil...":  ":)",
":disappointed:" : ":(",
":loud_laugh:" : "XD" ,
":open_mouth:" : ":o",
":stuck_out_tongue:" : ":p"
}
arr = s.split()
i =0
for string in arr:
    if string in emojis:
        arr[i] = emojis.get(string)
    i+=1
print(' '.join(arr))
