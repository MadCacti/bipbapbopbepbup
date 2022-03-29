{% include base.html %}

# [Link to Replit](https://replit.com/@MadCacti/bipbapbopbepbup)

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@MadCacti/bipbapbopbepbup?lite=true#README%22%3E">

## Week 0
### Learning how menus work and are built in terminal.
```
def menu():
    title = "menu" + banner 
    menu_list = main_menu.copy()
    menu_list.append(["patterns", submenu])
    buildMenu(title, menu_list)


```
## Week 1
### Learned how to create datalists and print them 3 different ways.

```
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
```
```
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
```