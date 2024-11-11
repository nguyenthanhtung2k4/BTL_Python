import json

def Update_Color(file_Setting):
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
     with open(file_Setting,'r')as file:
          data=json.load(file)
          Font_Logo=data['Setting']['Font_Logo']
          Back_Logo=data['Setting']['Back_Logo']
          Bar_Logo=data['Setting']['Bar_Logo']
          Font_color=data['Setting']['Font_Color']
          Back_color=data['Setting']['Back_Color']
          Font_ERROR=data['Setting']['Font_ERROR']
          Back_ERROR=data['Setting']['Back_ERROR']
          for i  in f :# check font
               if  Font_color== i:
                    Font_color=f[i]
               if  Font_ERROR== i:
                    Font_ERROR=f[i]
               if Bar_Logo == i:
                    Bar_Logo=f[i]
               if Font_Logo== i:
                    Font_Logo=f[i]
          for  j in b:#check back
               if  Back_color== j:
                    Back_color=b[j]
               if Back_ERROR == j:
                    Back_ERROR =b[j]
               if Back_Logo==j:
                    Back_Logo=b[j]
     Back_RESET="\033[49m";Font_RESET="\033[39m"
     RESETS=Back_RESET+Font_RESET         
     return Font_Logo,Back_Logo,Bar_Logo ,Font_color,Back_color,Font_ERROR,Back_ERROR,RESETS;
# if __name__ == "__main__":
#      file_Setting=r'D:\CODE\DNU_PYTHON\BTL\BTL_Python\Setting.json'
#      colorF_logo,colorB_logo,color_bar, colorF,colorB,erF,erB,RESETs=Update_Color(file_Setting),
     