import os
import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .YModulus import YModulus

def multiple(allname='Results',polymers=[],loc='./',savefig=True,savedata=True,needYM=True):
    """
    The method to create a Stress-Strain Curve chart and .csv relevant data file of all polymers you choose.
    multiple(allname='Results', polymers=[file1, file2, file3, ...], loc='./', savefig=True, savedata=True, needYM=True))
    allname: The name of your saved stress-strain curve chart and data file.
    polymers: Your selected polymer names on your file. The default is all polymers which has _Results.txt file in the location. 
    loc: File Location. The default is your current location.
    savefig, savedata: To show if you want to save the chart and .csv curve. The default is True.
    neddYM: To calculate Young's modulus of each polymers and display it in the data file.
    You can get the further information by .curve and .autocurve.
    Example:
        Input:
            from MCPoly.sscurve import multiple
            multiple(['P1','P2'])
        Output:
            ['P1','P2']
                               Strain Length (P1)  Strain Length (P2)  \
            Stress Force(nN)                                            
            0.0                         1.000000             1.000000   
            0.5                         1.012022                  NaN   
            1.0                         1.024666             1.028089   
            1.5                              NaN                  NaN   
            2.0                         1.053014             1.058092   
            2.5                              NaN                  NaN   
            3.0                         1.086888             1.093080   
            3.5                              NaN                  NaN   
            4.0                         1.130600             1.136959   
            4.5                              NaN                  NaN   
            5.0                         1.199289             1.203102   
            5.5                              NaN                  NaN   
            6.0                              NaN                  NaN   
            6.5                              NaN                  NaN   
            7.0                              NaN                  NaN   
            7.5                              NaN                  NaN   
            8.0                              NaN                  NaN   
            8.5                              NaN                  NaN   
            9.0                              NaN                  NaN   
            9.5                              NaN                  NaN   
            10.0                             NaN                  NaN   
            NaN                        29.516401             23.478160  NaN-> Young's Modulus
    TIPS: This function only depends on _Results.txt file, not .mol, .inp, .out, .xyz files.
    """
    opath=os.getcwd()
    if polymers==[]:
        for path in os.listdir(loc):
            if os.path.isfile(os.path.join(loc, path)):
                a=re.search('_Result.txt', path)
                if a:
                    polymers.append(path[:-11])            
    print(polymers)
    
    try:
        f=open('ot.txt','x')
    except:
        f=open('ot.txt','w')
    f.write('Stress Force(nN)\n0.\n0.5\n1.\n1.5\n2.\n2.5\n3.\n3.5\n4.\n4.5\n5.\n5.5\n6.\n6.5\n7.\n7.5\n8.\n8.5\n9.\n9.5\n10.')
    f.close()
    
    ot=pd.read_csv('ot.txt')
    ym=[None]
    name=[]
    i=0

    for polymer in polymers:
        polymer=polymer+'_Result.txt'
        try:
            datum=pd.read_csv(polymer)
        except:
            continue
        datum=datum[:].sort_values(by=['Strain Length(%)'])
        ax=plt.plot(datum['Strain Length(%)'][:-1],datum['Stress Force(nN)'][:-1],'*-')
        if needYM==True:
            ym.append(YModulus(polymer))
        b=re.search(r'[A-Z]+[a-z]?[0-9]*\-?[A-Z]*[0-9]*_', polymer)
        #print(b.group(0)[:-1])
        datum=datum.rename(columns={'Strain Length(%)':'Strain Length ({0})'.format(b.group(0)[:-1])})
        ot=pd.merge_ordered(ot, datum[:-1], fill_method="ffill" , left_by="Stress Force(nN)")
        name.append(b.group(0)[:-1])
        i=i+1

    if needYM==True:
        al=pd.DataFrame(data=ym, index=ot.columns, columns=["Young's Modulus"])
        al=al.T
    #print(al)
        ot=pd.concat([ot,al])
    ot=ot.set_index('Stress Force(nN)')
    print(ot)
    if savedata==True:
        ot.to_csv('file1.csv')
    
    #ax = sns.scatterplot(data=ot, alpha=0.8)
    #ax.set_ylabels='Strain Length(%)'
    #_ = plt.title('Stress-Strain Curve')
    #bx = sns.relplot(data=ot, kind="line", alpha=0.5)
    #bx.set_ylabels='Strain Length(%)'
    #ax.legend(bbox_to_anchor=[1.1,0.9])
    plt.xlabel('Strain Length(%)')
    plt.ylabel('Stress Force(nN)')
    plt.legend(name,bbox_to_anchor=[1.1,0.9])
    
    _ = plt.title('Stress-Strain Curve')
    if savefig==True:
        plt.savefig('{0}.png'.format(allname),bbox_inches='tight')
    
    os.system('rm ot.txt')
    os.chdir(opath)