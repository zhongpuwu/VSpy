
class Node: #一个队列节点类
    def __init__(self,value):
        self.value=value
        self.next=None

class Line: #队列模型
    def __init__(self,num):
        self.head=None
        self.current=None
        self.num=num
        self.size=0
    def add(self,a): #入队
        if(self.head==None):
            self.head=a
            self.current=a
            self.size+=1
        else:
            self.current.next=a
            self.size+=1
            self.current=self.current.next
    def isfull(self): #是否满
        if(self.size==m):
            return True
    def isempty(self): #是否为空
        if(self.size==0):
            return True
    def out(self): #出队列
        if(self.head==None):
            return 0
        else:
            a=self.head.value
            self.head=self.head.next
            self.size-=1
            return a


def getrealtime(t):
    return "%02d:%02d" % (t//60,t%60)


n=2
m=2
p=7
q=5
a=[1,2,6,4,3,534,2]
b=[3,4,5,6,7]

x=[]
for i in range(0,n):
    x.append(Line(n)) #创建两个队列
num=0

for i in range(0,len(a)):
    x[0].add(Node(a[i]))

for i in range(0,7*60):
    for j in x:
        if(j.isempty() and not j.isfull()):
            j.add(Node(a[num]))
            num+=1
        if(j.head.value==0) j.out()
