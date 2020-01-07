#-*-coding:utf-8-*-
#数组实现
class Queue():
    def __init__(self):
        self.entries = [] #表示队列内的参数
        self.length = 0 #表示队列的长度
        self.front=0 #表示队列头部位置
    def enqueue(self, item):#入队列
        self.entries.append(item)
        self.length = self.length + 1 #队列长度增加 1
    def dequeue(self):#出队列
        self.length = self.length - 1 #队列的长度减少 1
        dequeued = self.entries[self.front] #队首元素为dequeued
        self.front-=1 #队首的位置减少1
        self.entries = self.entries[self.front:] #更新队列
        return dequeued
    def peek(self):#获取队列第一个元素
        return self.entries[0]
if __name__ == "__main__":
    q=Queue()
    q.enqueue(7)
    q.enqueue(89)
    print(q.peek())#7
    print(q.dequeue())#7
    print(q.peek())#89