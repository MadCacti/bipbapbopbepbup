InfoDb = []

InfoDb.append({  
               "Name": "Raiden Tung",  
               "Birthday": "January 15",  
               "Classes Taking":["US History", "AM Lit", "AP Physics", "AP Stats", "AP CSP"]  
              })  

InfoDb.append({  
               "Name": "Audrey Zeng",  
               "Birth": "July 22",  
               "Classes Taking":["AP Studio Art","APEL","APUSH","AP Stats", "AP Bio"] 
              })

InfoDb.append({  
               "Name": "Jeffrey Lee",  
               "Birth": "December 27",  
               "Classes Taking":["AP Physics","AP Calc BC", "US History", "AM Lit", "AP Music Theory"] 
              })

InfoDb.append({  
               "Name": "Muhan Wei",  
               "Birth": "February 22",  
               "Classes Taking":["US History","Racquet Sports","Pre-Calc","AP Physics", "Offroll"] 
              })

def for_loop():
  for i in range(len(InfoDb)):
    print(InfoDb[i])

def while_loop(i=0):
  while i < len(InfoDb):
    print(InfoDb[i])
    i += 1

def recursive_loop(i=0):
  if i < len(InfoDb):
    print(InfoDb[i])
    recursive_loop(i+1)

def database():
  num = input("for, while, recursive?")
  try:
      if num == "for":
        for_loop()
      elif num == "while":
        while_loop()
      elif num == "recursive":
        recursive_loop()
  except:
    print("somethings fishy it no worky")
      
if __name__ == "__main__":
  database()