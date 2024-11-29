


class StacK:
    def __init__(self, stackLength):
        self.stack = [None for i in range(stackLength)]
        self.sp = -1
        self.max = stackLength
    
    def isFull(self) -> bool:
        return self.sp + 1 == self.max
    #end function
    
    def isEmpty(self) -> bool:
        return self.sp == -1
    #end function

    def push(self, item) -> None:
        if not self.isFull():
            self.sp = self.sp + 1
            self.stack[self.sp] = item
        else:
            print("stack full")
            #endif
    #end procedure

    def pop(self) -> str:
        if not self.isEmpty():
            self.sp = self.sp - 1
            return self.stack[self.sp + 1]
        else:
            print("empty stack")
            return ""
        #endif
    #end procedure

    def peek(self) -> str:
        if not self.isEmpty():
            return self.stack[self.sp]
        else:
            print("stack empty")
            return ""
        #endif
    #endfunction

    def __repr__(self) -> str:
        return ":".join(self.stack)



stack1 = StacK(3)
for c in "abcde":
    stack1.push(c)

for _ in range(5):
    print(stack1.pop())