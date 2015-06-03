import sys
import datetime
sys.path.append('C:\\Users\\Nero\\Desktop\\DESK')

class Priority_Queue(object):
    Pd={'P0':0,'P1':1,'P2':2,'P3':3}
    def __init__(self,s):
        self.s=s
    def new_task(self,t,p):
        self.s[Priority_Queue.Pd[p]]+=[t]
        Time[t]=datetime.datetime.now().strftime("%H:%M:%S %d-%m-20%y")
    def remove_task(self,t,p):
        self.s[Priority_Queue.Pd[p]].remove(t)
        Time.pop(t)
    def __str__(self):
        for i in range(4):
            print("Priority "+str(i))
            for j in self.s[i]:
                if j!="":
                    print(j+"   "+str(Time[j]))
            #print("")
        return " "


def read_data(a):
    s=[[],[],[],[]]
    Time={}
    ss,t=[i for i in a.split('\n')]
    ss=[i for i in ss.split('\/1')]
    for k in range(4):
        s[k]=[i for i in ss[k].split('\/0')]
    t=[i for i in t.split('\/2')]
    for k in t:
        k=[i for i in k.split(' : ')]
        if k!=[""]:
            Time[k[0]]=k[1]
    return(s,Time)

def write_data(s,Time):
    wd=""
    for i in s:
        for j in i:
            wd+=j+'\/0'
        wd+='\/1'
    wd+='\n'
    for i in Time:
        wd+=i+" : "+str(Time[i])
        wd+='\/2'
    return wd


plan=open("Plan.txt",'r')
a=''
for i in plan:
    a+=i
s,Time=read_data(a)
pq=Priority_Queue(s)
plan.close()
print(pq)
q=input("Add a task?(A) or Remove a task?(R) or Just wanted to see the queue?")
if q=='A':
    print('"Task->Pi" for ith Priority iE{0,1,2,3}.')
    b=input()
    t,p=[i for i in b.split("->")]
    pq.new_task(t,p)
    print(pq)
elif q=="R":
    print('"Task->Pi" for ith Priority iE{0,1,2,3}.')
    b=input()
    t,p=[i for i in b.split("->")]
    pq.remove_task(t,p)
    print(pq)
plan=open("Plan.txt",'w')
plan.write(write_data(s,Time))
plan.close()
