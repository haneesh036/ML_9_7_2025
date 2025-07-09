#converting string to lower case and checking and incrementing the variables 
inpstr=input("Enter a text:")
inpstr=inpstr.lower()
countv=0
countc=0
for w in inpstr:
    if w in ('a','e','i','o','u'):
        countv=countv+1
    else:
        countc=countc+1
print("Number of vowels:")
print(countv)
print("Number of consonants:")
print(countc)
