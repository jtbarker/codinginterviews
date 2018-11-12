import csv
import pandas as pd

filename1 = "outfile1.csv"
filename2 = "outfile2.csv"
filename3 = "outfile3.csv"
filename4 = "outfile4.csv"
filename5 = "outfile5.csv"

dedupe1 = "dedupe1.csv"
dedupe2 = "dedupe2.csv"
dedupe3 = "dedupe3.csv"
dedupe4 = "dedupe4.csv"
dedupe5 = "dedupe5.csv"

globalrowcount = 0
globalrowcountdeduped = 0

# with open(filename1,newline='',errors='ignore') as csvfile:
#     reader = csv.DictReader(csvfile)
#     rowcount = 0
#     n = 0
#     for row in reader:
#             print(row['recipient_name'],row['recipient_duns'])

df = pd.read_csv(filename1, sep=",",engine='python', encoding="utf-8-sig", error_bad_lines=False)
df1 = df.iloc[:,1:10]
df1.drop_duplicates(subset='recipient_doing_business_as_name')
df1.to_csv('dedupe1.csv')

df = pd.read_csv(filename2, sep=",",engine='python', encoding="utf-8-sig", error_bad_lines=False)
df1 = df.iloc[:,1:10]
df1.drop_duplicates(subset='recipient_doing_business_as_name')
df1.to_csv('dedupe2.csv')

df = pd.read_csv(filename3, sep=",",engine='python', encoding="utf-8-sig", error_bad_lines=False)
df1 = df.iloc[:,1:10]
df1.drop_duplicates(subset='recipient_doing_business_as_name')
df1.to_csv('dedupe3.csv')

df = pd.read_csv(filename4, sep=",",engine='python', encoding="utf-8-sig", error_bad_lines=False)
df1 = df.iloc[:,1:10]
df1.drop_duplicates(subset='recipient_doing_business_as_name')
df1.to_csv('dedupe4.csv')

df = pd.read_csv(filename5, sep=",",engine='python', encoding="utf-8-sig", error_bad_lines=False)
df1 = df.iloc[:,1:10]
df1.drop_duplicates(subset='recipient_doing_business_as_name')
df1.to_csv('dedupe5.csv')


with open(filename1,newline='',errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcount += 1

with open(filename2, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcount += 1

with open(filename3, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcount += 1

with open(filename4, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcount += 1

with open(filename5, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcount += 1



### dedupe calculation:

with open(dedupe1, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcountdeduped += 1

with open(dedupe2, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcountdeduped += 1

with open(dedupe3, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcountdeduped += 1

with open(dedupe4, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcountdeduped += 1

with open(dedupe5, newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile)
    rowcount = 0
    for row in reader:
        rowcount += 1
        globalrowcountdeduped += 1

print("Total number of contracts before deduplicating on exact vendor matches:", globalrowcount) #this number is the total government contracts before deduplication
print("Total number of contracts after exact vendor match deduplication:",globalrowcountdeduped) #count after deduplication
