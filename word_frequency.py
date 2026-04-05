file_input = input("Enter the name of the file :-")

try:
    file_handle = open(file_input, "r")
except:
    print("Invalid File Name. ")
    exit()
    
count = dict()

for lines in file_handle:
    words = lines.split()
    for word in words:
        word = word.lower()
        count[word] = count.get(word, 0) + 1 

lst = []
newlst=[]

for key, value in count.items():
    newt = (value,key)
    if value==1:
        newlst.append(newt)
    else:
        lst.append(newt)


lst = sorted(lst, reverse=True)

print("======================= \n")
print("Word Frequency Counter \n")
print("======================= \n")
print("File:- ", file_input)
print("----------------------- \n")
i = 0
for value, key in lst:
    print(str(i+1) + "." + key + "- " + str(value))
    i+=1
print("Unique Words:- ", len(newlst))
