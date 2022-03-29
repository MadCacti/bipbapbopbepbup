import math

def BinToDec(bin):
  tot = 0
  for i in range(len(bin)):
    sum = float(bin[i])*(2**((len(bin)-i)))
    tot += sum
  return tot/2



def DecToBin(dec):

  bin = ""
  digits = math.floor(math.log2(dec) + 1) 
  
  for i in range(digits):
    place = digits - 1 - i
    if(2**place <= dec):
      dec -= 2**place
      bin += "1"
    else:
      bin += "0"
    
  return bin


print(BinToDec(DecToBin(253423)))