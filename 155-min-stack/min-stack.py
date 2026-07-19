class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else :
            self.min_stack.append(self.min_stack[-1])
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        

