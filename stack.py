#-*-coding:utf-8-*-
class Stack(object):
    def __init__(self, limit=10):
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限
    def push(self, data): #入栈
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
        self.stack.append(data)
    def pop(self):#出栈
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack') #空栈不能被弹出
    def peek(self): #查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
    def is_empty(self): #判断栈是否为空
        return not bool(self.stack)
    def size(self): #返回栈的大小
        return len(self.stack)
if __name__ =="__main__":
    stack=Stack()
    print(stack.is_empty())#True
    print(stack.size())#0
    stack.push([1])
    stack.push([3])
    stack.push([2])
    print(stack.peek())#[2]
    print(stack.is_empty())#False
    print(stack.size())#3
    print(stack.pop())#[2]
    print(stack.peek())# [3]