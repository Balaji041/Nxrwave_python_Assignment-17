String=input()
M=int(input())
N=int(input())
name=""
for i in String:
    if ord(i)>=M and ord(i)<=N:
        name+=i+" "
print(name)
"""
input:AiRPort
input:65
input:111
output:A i R P o 
"""
