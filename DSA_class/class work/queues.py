# Defining a class for queue
class my_queue:
    def __init__(self,inp=[]):
        self._array = inp
    def __len__(self):
        return len(self._array)
    def push(self,item):
        self._array.append(item)
    def pop(self):
        return self._array.pop(0)
    def top(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        else:
            return self._array[-1]
    def is_empty(self):
        return (len(self._array==0))
    def show(self):
        return self._array
    def __repr__(self):
        return str(self._array)
