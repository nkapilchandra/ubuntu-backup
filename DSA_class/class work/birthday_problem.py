import random
import matplotlib.pyplot as plt

days = []
data = []
for j in range(100000):
    data.append(days)
    days = []
    for i in range(70):
        days.append(random.randint(1,366))

nums = [0]*len(data)

for i in range(len(data)):
    temp = data[i]
    for j in data[i]:
        temp.remove(j)
        if j in temp:
            nums[i] += 1
            while(True):
                try:
                    temp.remove(j)
                except:
                    break

# print(nums)
avg = sum(nums)/len(nums)
print(avg)
