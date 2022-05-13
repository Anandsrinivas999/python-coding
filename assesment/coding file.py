class DS:
    out=[]

class ui:
    def get(self):
        for i in range(1,11):
            d=int(input('enter distance:'))
            t=int(input('enter time:'))
            DS.out+=[[d,t]]
class M:
    def measure(self):
        a=DS.out
        for i in a:
            res=i[0]/i[1]
            i.append(res)
class Disp:
    def display(self):
        for i in DS.out:
            print(i)
ob1=ui()
ob1.get()
ob2=M()
ob2.measure()
ob3=Disp()
ob3.display()

import csv
a=['Distance','Time','Speed']
r=DS.out
f='data.csv'

fo=open(f,'w')
f1=csv.writer(fo)
f1.writerow(a)
f1.writerows(r)
fo.close()
