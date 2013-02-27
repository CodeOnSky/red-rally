


import urllib
import json
import datetime
openda = urllib.urlopen('http://maccherone.com/share/1000-snapshots-overlap-with-Feb-2012.json').read()

datafile = json.loads(openda)

from_time = [item.get('_ValidFrom') for item in datafile]
from_d = [datetime.datetime.strptime( item.get('_ValidFrom'), "%Y-%m-%dT%H:%M:%S.%fZ" ) for item in datafile]
#to_time= [item.get('_ValidTo') for item in datafile]
time_d = [datetime.datetime.strptime( item.get('_ValidTo'), "%Y-%m-%dT%H:%M:%S.%fZ" ) for item in datafile]
state = [item.get('ScheduleState') for item in datafile]
obj_Id = [item.get('ObjectID') for item in datafile]
unique_Id = set(obj_Id)
Id_object = list(unique_Id)
unique_state = set(state)
sta = list(unique_state)
       
import texttable as tt
from texttable import Texttable
tab = tt.Texttable()
table_list = [[]]

c=0
for uni in Id_object:
    alltime=[]
    worktime=[]
    time_spent=0
    b=0
    for line in datafile:
                
        if uni == line.get('ObjectID'):
            t = datetime.datetime.strptime( line.get('_ValidTo'), "%Y-%m-%dT%H:%M:%S.%fZ" )
            f = datetime.datetime.strptime( line.get('_ValidFrom'), "%Y-%m-%dT%H:%M:%S.%fZ" )
            tt = t.time()
            ft = f.time()
            x=t.month
            y=f.month
            
            if (t.month != 2) and (f.month !=2) and (t.year == 2012) and (f.year == 2012) :
                days_spent=0
                #time_spent=alltime
                time_spent=0
                a=0
                b=0
                
            if (t.month == 2) and (f.month ==2) and (t.year == 2012) and (f.year == 2012) :
                days_spent=(t.day-f.day+1)
                start = f.date()
                end =t.date()
                daydiff = end.weekday() - start.weekday()
                days = ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5)
                #total  = ((tt.hour-ft.hour)*3600000 +(tt.minute-ft.minute)*60000+(tt.second-ft.second)*1000+(tt.microsecond-ft.microsecond))+((t.day-f.day)-1)*24*3600000
                total = (24*3600000-(ft.hour*3600000 +ft.minute*60000+ft.second*1000+ft.microsecond))+(tt.hour*3600000 +tt.minute*60000+tt.second*1000+tt.microsecond)+((t.day-f.day)-1)*24*3600000
                time_spent = float(total)/3600000   #to get Hours
                
                if ((tt.hour and ft.hour) in range(9,18)):
                    a = (17*3600000-(ft.hour*3600000 +ft.minute*60000+ft.second*1000+ft.microsecond))+(tt.hour*3600000 +tt.minute*60000+tt.second*1000+tt.microsecond-9*3600000)+(days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour >=17 and tt.minute>=0):
                    a = 8*3600000 +(days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour < 9):
                    a = (days)*8*3600000
                b = float(a)/3600000
                        
            if (t.year == 2012) and (t.month == 2)and (f.month != 2):
                #print('to')
                start = datetime.date(2012,2,1)
                end =t.date()
                daydiff = end.weekday() - start.weekday()
                days = ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5)
                days_spent=(t.day)
                total = (tt.hour*3600000 +tt.minute*60000+tt.second*1000+tt.microsecond)+ (t.day-1)*24*3600000
                time_spent = float(total)/3600000
                #print(time_spent)
                if (tt.hour  in range(9,18)):
                    a=((tt.hour-9)*3600000 +tt.minute*60000+tt.second*1000+tt.microsecond) + (days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour >=17 and tt.minute>=0):
                    a = 8*3600000 +(days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour < 9):
                    a = (days)*8*3600000
                    #b = float(a)/3600000
                b = float(a)/3600000
                
                        
                    
                
            if (f.year == 2012) and (f.month == 2)and (t.month != 2):
                start = f.date()
                end =datetime.date(2012,2,29)
                daydiff = end.weekday() - start.weekday()
                days = ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5)
                days_spent=(29 - f.day)
                total = (24*3600000-(ft.hour*3600000 +ft.minute*60000+ft.second*1000+ft.microsecond))+ (29-f.day)*24*3600000
                time_spent = float(total)/3600000 
                if (ft.hour in range(9,18)):
                    a=(17*3600000-(ft.hour*3600000 +ft.minute*60000+ft.second*1000+ft.microsecond))+ (days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour >=17 and tt.minute>=0):
                    a = 8*3600000 +(days)*8*3600000
                    #b= float(a)/3600000
                if (tt.hour < 9):
                    a = (days)*8*3600000
                    #b = float(a)/3600000
                b = float(a)/3600000
                
            
                
            alltime.append(time_spent)
            worktime.append(b)    
    
    
    table_list.append([repr(uni),sum(alltime),sum(worktime)])
#====================

import texttable as aa
from texttable import Texttable           
tab1 = aa.Texttable()
table_list1 = [[]]
for item in Id_object:
    ab = ['']*len(sta)
    ab.append(repr(item))
    ab.reverse()
    i=0
    for b1 in sta:
        #print(item,b1
        suma =[]
        i=i+1
        for lin in datafile:
            if (item == lin.get('ObjectID')) and (b1 == lin.get('ScheduleState')):
                t = datetime.datetime.strptime( lin.get('_ValidTo'), "%Y-%m-%dT%H:%M:%S.%fZ" )
                f = datetime.datetime.strptime( lin.get('_ValidFrom'), "%Y-%m-%dT%H:%M:%S.%fZ" )
                if (t.year  == 9999):
                    t= datetime.datetime.now()
                
                tt = t.time()
                ft = f.time()
                x=t.month
                y=f.month
                start = f.date()
                end =t.date()
                daydiff = end.weekday() - start.weekday()
                days = ((end-start).days - daydiff) / 7 * 5 + min(daydiff,5)
                if ((tt.hour and ft.hour) in range(9,18)):
                    a = (17*3600000-(ft.hour*3600000 +ft.minute*60000+ft.second*1000+ft.microsecond))+(tt.hour*3600000 +tt.minute*60000+tt.second*1000+tt.microsecond-9*3600000)+(days)*8*3600000
                    
                if (tt.hour >=17 and tt.minute>=0):
                    a = 8*3600000 +(days)*8*3600000
                    
                if (tt.hour < 9):
                    a = (days)*8*3600000


                time_spent = float(a)/3600000
                


                #time_spent=10
                suma.append(time_spent)

                                
        ab[i] = sum(suma)
                  
                
          
    table_list1.append(ab)
    
        
tab1.add_rows(table_list1)
tab1.set_cols_align(['r']*(len(sta)+1))
he=sta
he.reverse()
#he = ['']*len(sta)

he.append('Object_Id')
he.reverse()
#he.append(sta)
tab1.header(he)



tab.add_rows(table_list)
tab.set_cols_align(['r','r','r'])
header = ['Object_ ID','Hours_spent(24hrs scale)', 'Working hours']
tab.header(header)


print tab.draw()
print tab1.draw()

#table can also be saved into a new file
tsk1 = open("Feb_objectdata.txt","w")
tsk1.write(tab.draw())
tsk1.write('\n')
tsk1.write(tab1.draw())
tsk1.close()

                
                
##--LaxmiSunkara              
