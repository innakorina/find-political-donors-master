import pandas as pd
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]
outFile2 = sys.argv[3]

path=inFile
#import numpy as np
def zipper(data):    #1,11,14,15,16
    df1=data.loc[: , [0,10,13,14,15]]
    df1.columns = ['ID', 'ZIP','Date','Amount','Other']
    df1.Other.fillna(0, inplace=True)
    df1=df1[df1.Other==0]
    df1.dropna(axis=0, how='any')
    df1['ZIP'] = df1['ZIP'].astype(str).str[:5]
    df1.Amount = df1.Amount.astype(float)
    df2=df1.loc[: , ['ID','ZIP','Amount']]
    df3=df2.groupby(['ID','ZIP']).median().round().astype(int)
    df4=df2.groupby(['ID','ZIP']).sum().astype(int)
    df5=df2.groupby(['ID','ZIP']).count().astype(int)
    df6=pd.merge(df3, df5, left_index=True, right_index=True)
    df7=pd.merge(df6, df4, left_index=True, right_index=True)
    pairs=list(df7.index.values)
    IDs = [item[0] for item in pairs]
    ZIPs= [item[1] for item in pairs]
    #print(ZIPs)
    Result_df= pd.DataFrame(
        {'ID': IDs,
         'IZIP': ZIPs,
         'Median': df7['Amount_x'],
         'N':df7['Amount_y'],
         'Sum':df7['Amount']
        })
    return(Result_df)
    
def dater(data):    #1,11,14,15,16
    df1=data.loc[: , [0,10,13,14,15]]
    df1.columns = ['ID', 'ZIP','Date','Amount','Other']
    df1.Other.fillna(0, inplace=True)
    df1=df1[df1.Other==0]
    df1.dropna(axis=0, how='any')
    df1['ZIP'] = df1['ZIP'].astype(str).str[:5]
    df1.Amount = df1.Amount.astype(float)
    df2=df1.loc[: , ['ID','Date','Amount']]
    df3=df2.groupby(['ID','Date']).median().round().astype(int)
    df4=df2.groupby(['ID','Date']).sum().astype(int)
    df5=df2.groupby(['ID','Date']).count().astype(int)
    df6=pd.merge(df3, df5, left_index=True, right_index=True)
    df7=pd.merge(df6, df4, left_index=True, right_index=True)
    pairs=list(df7.index.values)
    IDs = [item[0] for item in pairs]
    ZIPs= [item[1] for item in pairs]
    print(ZIPs)
    Result_df= pd.DataFrame(
        {'ID': IDs,
         'IZIP': ZIPs,
         'Median': df7['Amount_x'],
         'N':df7['Amount_y'],
         'Sum':df7['Amount']
        })
    return(Result_df) 
    

def main():
    lines = []

    i=0
    for df in pd.read_csv(path,sep='|', header = None,dtype=object, chunksize = 1):
        lines.append(df)
        #print(lines)
        #print(i)
        #if i==0:
           # i=i+1
            #lines=df
        #else:
        lines_df = pd.concat(lines,axis=0,ignore_index=True)
        new_df=zipper(lines_df)
        #new_df=dater(lines_df)
        if i==0:
            save_df=new_df
            old_df=new_df
            i=i+1
        else:
            #save_df = new_df.merge(old_df, indicator=True, how='outer')
            save_df=pd.concat([new_df,old_df],axis=0)
            old_df=save_df
            save_df = save_df.drop_duplicates(keep=False)
              
        save_df.to_csv(outFile, mode='a', sep='|',  index = False, header=False)
    
    date_df=dater(lines_df)
    date_df.to_csv(outFile2, mode='a', sep='|',  index = False, header=False)

main()