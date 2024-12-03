class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack)==0
    def push(self,item):
        self.stack.append(item)
        print(f"{item} Push in Stack")
    
    def pop(self):
        if self.is_empty():
            return"the stack is empty"
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty():
            return "the stack is empty"
        return self.stack[-1]
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(11)
stack.push(12)
stack1=Stack()
stack1.push(13)
print(stack1.peek())
print(stack.size())
print(stack.pop())
print(stack.is_empty())