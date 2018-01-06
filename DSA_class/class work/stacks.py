# Defining a class for stack
class my_stack:
    def __init__(self,inp = []):
        self._array = inp
    def __len__(self):
        return len(self._array)
    def push(self,item):
        self._array.append(item)
    def pop(self):
        return self._array.pop()
    def top(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        else:
            return self._array[-1]
    def is_empty(self):
        return (len(self._array)==0)
    def show(self):
        return self._array
    def __repr__(self):
        return str(self._array)

if __name__ == '__main__':
    new = my_stack()
    print(new.is_empty())
    print(new.top())
    new.push(4)
    new.push(1)
    print(new.top())
    new.push(5)
    print(new.top())
    print(new.is_empty())
