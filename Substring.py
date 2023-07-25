class FSubstring:

    def __init__(self, InputStr, LengthStr):
        self.str = InputStr
        self.lstr = LengthStr

    def calcualte_Substring(self):
        substrings = []
        for i in range(len(self.str)):
            #print(i)
            for j in range(i + self.lstr, len(self.str)):
                #print(j)
                if self.str[i] == self.str[j]:
                    substring = self.str[i:j+1]
                    if len(substring) >= self.lstr:
                        substrings.append(substring)
        return substrings


InputStr =  input("Enter the String").strip()
LengthStr = int(input("Enter length of substring"))

print("===================================================================")
print (f"Original String {InputStr} and length of string {LengthStr}")

fs = FSubstring(InputStr, LengthStr)
output = fs.calcualte_Substring()

print("List of substring from original string :- ", output)
print("===================================================================")






