'''count=0
0
 1
2
3
4
while completed
outof the loop
>>> 
while count<5:
    print(count)
    count+=1
else:
    print("while completed")

print("outof the loop) '''
count=0

while count<5:
    print(count)
    count+=1
    if count==3:
        break
else:
    print("while completed")

print("outof the loop")