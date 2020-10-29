#LANGUAGE: Python
#AUTHOR: Arisandi
#GITHUB: https://github.com/arisandi1

# import modules
import os,time


# hello function
def hello():
    chars = 'Hello Hacktober2020'
    for i in chars:
      print(i,end="")
      time.sleep(0.5)

if __name__=='__main__':
  os.system("clear")
  hello()
