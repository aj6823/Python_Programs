class AsciiCal:
    
    def __init__(self, inputStr):
        self.str = inputStr

    def stringConvertor(self):
        #print(self.str)
        asciiList = []
        for i in self.str:
             asciiList.append(ord(i))
        return asciiList
    
    ## Function for validating ASCII value
    def ascii_value_validator(self, ascii_value):
        if ( min(ascii_value, 128) == ascii_value ):
            return ascii_value
        else:
            ascii_value = 83
            return ascii_value

    ## Function for coverting ASCII Value to string
    def asciiCalculator(self, convertedString):
        length = len(convertedString)
        tempList = [0]*length
        for i in range(length):
            if ( convertedString[i] % 2 == 0 and (i+1 < length) and tempList[i+1] == 0 ):
                new_ascii = convertedString[i] % 7
                convertedString[i+1] = self.ascii_value_validator(new_ascii + convertedString[i+1])
                tempList[i+1] = 1
            else:
                if ( i-1 >= 0 and tempList[i-1] == 0 ):
                        new_ascii = convertedString[i] % 5
                        convertedString[i-1] = self.ascii_value_validator(convertedString[i-1] - new_ascii)
                        tempList[i-1] = 1
        result_string = ''.join(chr(ascii_val) for ascii_val in convertedString)
        return result_string



inputString = input("Enter a String :- ").strip()
AsciiObj = AsciiCal(inputString)

print("===================================================================")
print("Original String :- " + inputString)
convertedString = AsciiObj.stringConvertor()
print("String Converted into ASCII List :- " , convertedString)

Final_Output = AsciiObj.asciiCalculator(convertedString)
print("Transform string :- " + Final_Output)
print("===================================================================")