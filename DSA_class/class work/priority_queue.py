class priority_queue:
    def __init__(self,inp={}):
        self._array = inp
    def __len__(self):
        return len(self._array)
    def push(self,item,weight):
        self._array[item] = weight
    def pop(self):
        key = list(self._array.keys())[0]
        val = self._array[key]
        for keys in self._array:
            if self._array[key] > self._array[keys]:
                key = keys
                val = self._array[keys]
        temp = key
        del self._array[key]
        return temp
    # def top(self):
    #     if self.is_empty():
    #         raise IndexError("The queue is empty")
    #     else:
    #         return self._array[-1]
    def is_empty(self):
        return (len(self._array)==0)
    def show(self):
        return self._array
    def __repr__(self):
        return str(self._array)

Q = priority_queue()
Q.push(1,3.5)
Q.push(2,1)
# Q.push(4,0)
print(Q.show())
print(Q.pop())
print(Q.show())
