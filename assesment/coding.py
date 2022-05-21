
class DS:
    pass
    
    
    

class ui:
    a=()
    @staticmethod
    def get():
        for i in range(1,11):
            d=int(input('enter distance:'))
            t=int(input('enter time:'))
            ui.a+=((d,t),)
class M:
    @staticmethod
    def measure():
        p=()
        a=ui.a
        for i in a:
            res=i[0]/i[1]
            p+=((i[0],i[1],res),)
        return p
            
class Disp:
    @staticmethod
    def display():
        for i in M.measure():
            print(i)
ui.get()
res=M.measure()
Disp.display()
import csv
a=['Distance','Time','Speed']
f='data1.csv'

fo=open(f,'w')
f1=csv.writer(fo)
f1.writerow(a)
f1.writerows(res)
fo.close()


