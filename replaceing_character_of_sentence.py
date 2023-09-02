String=input()
reverse_string=""
for i in String:
    if i!=" ":
        ordnum=ord(i)+1
        reverse_string+=chr(ordnum)
    else:
        reverse_string+=" "
print(reverse_string)
"""
input:Hello World
output:Ifmmp Xpsme
"""
