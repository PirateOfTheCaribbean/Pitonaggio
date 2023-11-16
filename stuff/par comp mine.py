# DMPXST{ZEOWPHST_R_VEROY_SAL_EOL_MXLZL!}
# spritz
"""
now it's safe to assume that: 
D=s
M=p
P=r
X=i
S=t
T=z

the era of the pirates...doesn't sound useful, probably a joke in the flag
D = 3.3844% 17.25
M = 3.0129% 15.36
P = 3.1671% 16.14

first row are the expected frequencies
the second one ?? idk
"""
import string

#read the ciphertext text
with open("challenge.txt", "r") as file:
    cipher = file.read()

# ok i shall write a script that checks the frequency of the expected letters
counter=dict.fromkeys(string.ascii_uppercase, 0)  # dict of letters
for i in range(0, len(cipher)):
    if (cipher[i].isalpha()): 
        counter[cipher[i]] += 1

percentage=dict.fromkeys(string.ascii_uppercase, 0)  
for i in counter:
    percentage[i] = (counter[i]/len(cipher))*100


print(percentage)
print()
#print (counter)
#print("and now percentages!")
#print (percentage)

compass={
    "A": 8.4966,
    "B": 2.0720,
    "C": 4.5388,
    "D": 3.3844,
    "E": 11.1607,
    "F": 1.8121,
    "G": 2.4705,
    "H": 3.0034,
    "I": 7.5448,
    "J": 0.1965,
    "K": 0.2902,
    "L": 5.4893,
    "M": 3.0129,
    "N": 6.6544,
    "O": 7.1635,
    "P": 3.1671,
    "Q": 0.1962,
    "R": 7.5809,
    "S": 5.7351,
    "T": 6.9509,
    "U": 3.6308,
    "V": 1.0074,
    "W": 1.2899,
    "X": 0.2902,
    "Y": 1.7779,
    "Z": 0.2722,
}

for i in percentage:
    delta=abs(percentage[i]-compass["A"])
    curletter="A"
    for j in compass:
        if(percentage[i]-compass[j] < delta):
            delta = abs(percentage[i]-compass[j]) 
            curletter=j
    print(i," = ",curletter)