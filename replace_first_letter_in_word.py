String=input()
first=""
full_string=""
for i in range(len(String)):
    if String[i]!=" ":
        char=String[i]
        first+=char
    if String[i]==" " or i==len(String)-1:
        ch=first[0]
        new_char=ord(ch)+1
        new=chr(new_char)
        full_string+=new+first[1:]+" "
        first=""
print(full_string)

"""
input:East And West
output:Fast Bnd Xest
"""
