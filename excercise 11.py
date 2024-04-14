heights_input = input("Enter the heights: ")
heights = heights_input.split(',')
print(heights)

count = 0
for height in heights:
    count = count + 1

print("Number of heights:", count)

print(count)
for i in range(0,count):
    heights[i]=int(heights[i])
print(heights)
total=0
for i in heights:
    total=total+i
    
print(total)
avg=total/4
print(avg)
print(round(avg))
