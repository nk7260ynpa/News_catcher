import csv



def db_read(base):#讀取資料庫函式
    fout=open(base,"rt",encoding = 'utf8')
    all_data=fout.readlines()
    back_list=[]
    for each_data in all_data:
        back_list.append(each_data[0:-1])
    fout.close()
    return back_list

read_file=open("News_list.txt","rt",encoding = 'utf8')#叫出要被分析的數據
cin=csv.reader(read_file)
villains=[row for row in cin]


c=db_read("positive.txt")
g=db_read("negative.txt")

for analyzed in villains:#驗證
    e=0
    for d in c:
        f=analyzed[0].find(d)
        if f!=(-1):
            e+=1
    j=0
    for i in g:
        k=analyzed[0].find(i)
        if k!=(-1):
            j-=1
    if e+j>0:
        analyzed.append("#好的")
        analyzed.append(e)
    elif e+j<0:
        analyzed.append("#壞的")
        analyzed.append(j)
    else:
        analyzed.append("#一般的")



result=open("Result.txt","wt",encoding = 'utf8')

fileout = csv.writer(result)
fileout.writerows(villains)

read_file.close()
result.close()