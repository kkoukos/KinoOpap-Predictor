import requests



response = requests.get("https://drand.cloudflare.com/public/latest")
b = []
a = response.text
a = a.split(",")
a = a[1].split(":")
a = a[1][1:]
a = a[:-1]
print("The random number given by clouflare in hex:")
print(a)

for x in range(1,33):
    

    b.append(a[2*x-2:2*x]) 

response = requests.get("https://api.opap.gr/draws/v3.0/1100/last-result-and-active")

a = response.text


a = a.split("winningNumbers")

a = a[1].split("list\"")
a = a[1].split("\"bonus\"")

winners = a[0]



temp="[]:"

for char in temp:
    winners=winners.replace(char,"")

winners=winners.split(",")
print("These are the winning numbers:")
winners.pop(len(winners)-1)#vgazei to teleutaio stoixeio p einai ''
print(winners)

sum=0


for x in b:
  
  b[sum]=int(x,16)%80
  sum+=1



sum=0
for x in range(0,len(b)-1): #to teleutaio checkarete me ola hdh
 

 for temp in range(x+1,len(b)):
     
     if b[x] == b[temp] and b[x]!= "blank":
         b[temp]="blank"

r=32

while(sum<r):
    if b[sum]=="blank":
        b.pop(sum)
        r=r-1
        sum-=1
    sum+=1

sum=0
win=[]
print("These are the numbers we generated:")
print(b)  

for x in b:
    
    temp=str(x)
    
    if temp in winners:
        win.append(temp)
        sum+=1
   
print("We found that",sum,"numbers would win")
print("The winning numbers were:")
print(win)
print("Press any button to terminate")





input()
