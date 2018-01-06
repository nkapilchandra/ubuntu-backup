import random
import matplotlib.pyplot as plt

nums1 = []
nums2 = []

for i in range(1000):
    nums1.append(random.randint(1,10))
    nums2.append(random.random())

print(nums2)
# plt.hist(nums1)
plt.hist(nums2)
plt.show()
