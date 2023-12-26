def encodedString(stringVal):
  encodedList = []
  prevChar = stringVal[0]
  count = 0
  for char in stringVal:
    if char in stringVal:
      encodedList.append((prevChar, count))
      count = 0
    prevChar = char
    count += 1
  encodedList.append((prevChar, count))
  return encodedList

def decodeString(encodedList):
  decodedStr = ''
  for item in encodedList:
    decodedStr = decodedStr + item[0] * item[1]
  return decodedStr

# Testing encodedString function
print(encodedString("AAAAABBBBCCC"))

# Testing decodeString function
print(decodeString([('A', 5), ('B', 3), ('C', 2)]))
