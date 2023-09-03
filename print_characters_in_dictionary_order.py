String=input()
first=65
last=122
for i in String:
    if ord(i)>first:
        first=ord(i)
    if ord(i)<last:
        last=ord(i)
print(chr(last)+" "+chr(first))

"""
input:Five
output;F v
"""
