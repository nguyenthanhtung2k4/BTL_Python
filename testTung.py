import json

#  import colorama
# /////////// Font color
f={
     "F1":"\033[30m"  ,     # black
     "F2":"\033[31m",       # red
     "F3":"\033[32m"  ,     # green
     "F4":"\033[33m"   ,    # yellow
     "F5":"\033[34m" ,      # blue
     "F6":"\033[35m"    ,   # magenta
     "F7":"\033[36m" ,      # cyan
     "F8":"\033[37m"  ,     # white
     "F0":"\033[39m"      # reset
     
}
# /////////// Back color
b={
     "B1":"\033[40m"  ,    # black
     "B2":"\033[41m",      # red
     "B3":"\033[42m"  ,    # green
     "B4":"\033[43m"   ,   # yellow
     "B5":"\033[44m" ,     # blue
     "B6":"\033[45m"    ,  # magenta
     "B7":"\033[46m" ,     # cyan
     "B8":"\033[47m"  ,    # white
     "B0":"\033[49m"      # reset
}
table={0:"Mac dinh",1:"Black",2:"Red",3:"Green",4:"yellow",5:"Blue",6:"Magenta",7:"Cyan",8:"White",}
file_color="D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json"

with open(file_color,"w+")as js:
     FC='F5';FR='F2'
     BC='B0';BR='B4'
     time_logo=0.025
     time_about=0.025
     
     try:
          Data=json.load(js)
     except json.JSONDecodeError:
          Data={}
          new_data = {
          "Setting": {
          "Font_Color": FC,
          "Font_ERROR": FR,
          "Back_Color": BC,
          "Back_ERROR": BR,
               },
          "Delay": {
               "Time_logo": time_logo,  #0.025,
               "Time_About": time_about#0.025
               },
          "Tabale":{
               "Font":table,
               "Back":table
               }
          }
          Data.update(js)
          json.dump(new_data, js,indent=4)
with open(file_color,"r")as color:
     data=json.load(color);
     Back_RESET="\033[49m";Font_RESET="\033[39m"
     Font_color=data['Setting']['Font_Color']
     Back_color=data['Setting']['Back_Color']
     Font_ERROR=data['Setting']['Font_ERROR']
     Back_ERROR=data['Setting']['Back_ERROR']
     for i  in f :
          if  Font_color== i:
               Font_color=f[i]
          if  Font_ERROR== i:
               Font_ERROR=f[i]
     for  j in b:
          if  Back_color== j:
               Back_color=b[j]
          if Back_ERROR == j:
              Back_ERROR =b[j]
print(f'{Font_color}Color F\n{Back_color} color back\n{Back_RESET+Font_ERROR} error  f\n{Back_ERROR} error  back{Back_RESET}')