import random
def primary():
  
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  #print(quotes)
  #print(quotes[len(quotes)-1])
  last = len(quotes)-1
  rnd = random.randint(0, last)
  print(quotes[rnd])
 
if __name__== "__main__":
  primary()
