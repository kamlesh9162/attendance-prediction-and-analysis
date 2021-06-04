import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

exl = pd.read_excel('attendance.xlsx',sheet_name='6th sem')
df = pd.DataFrame(exl)

def pred(n):
    total = df.at[n-1,'Jan total present']+df.at[n-1,'Jan total absent']+df.at[n-1,'Feb total present']+df.at[n-1,'Feb total absent']+df.at[n-1,'March total present']+df.at[n-1,'March total absent']+df.at[n-1,'April total present']+df.at[n-1,'April total absent']+df.at[n-1,'May total present']+df.at[n-1,'May total absent']
    tp = df.at[n-1,'Jan total present']+df.at[n-1,'Feb total present']+df.at[n-1,'March total present']+df.at[n-1,'April total present']+df.at[n-1,'May total present']
    ucc = int(input('Enter the no. of Up coming classes : '))
    sf = int((total+ucc)*0.75)
    ma = sf - tp
    if ma<=0:
        print('You can skip them all')
    else:
        if ma>ucc:
            print('Oops! yoy have no chance to make it 75%')
            print('it is',ma)
        else:
            print('You should attend',ma,'more classes')

def attend():
    n = int(input('Enter the roll no. of sutdent : '))
    att = np.array([round(df.at[n-1,'Jan %'],2),round(df.at[n-1,'Feb %'],2),round(df.at[n-1,'March %'],2),round(df.at[n-1,'April %'],2),round(df.at[n-1,'May%'],2),round(df.at[n-1,'Total'],2)])
    mnt = np.array(['Jan','Feb','March','April','May','Total'])
    clr = np.array(['blue','green','yellow','black','cyan','red'])

    plt.bar(mnt,att,color=clr)
    plt.title(df.at[n-1,'Name of Student'],fontsize=15)


    for index,data in enumerate(att):
        plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
    plt.tight_layout()
    plt.show()
    pred(n)
    attend()

attend()