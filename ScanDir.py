import requests
import sys
import os.path
from requests import *


def working(url, Path):
    if os.path.isfile(Path):
        file = open(Path, "r")
        while True:
            line = file.readline()
            if not line:
                break
            if url[-1]=='/':
                response = requests.get(url+line)
                print('=>'+url+line+' (CODE: '+str(response.status_code)+')')
            else:
                response = requests.get(url+'/'+line)
                print('=>'+url+'/'+line+' (CODE: '+str(response.status_code)+')')
        file.close
    else:
        print("[X]   Path is not correct")
        print()
        print()


def drawicon():
    print("---------------------------------------------------------------------")
    print("|      ///////                            ///////                     ||")
    print("|     //       //////  ////     //       //     //   //   //////      ||||")
    print("|    //////   //      // //    /////    //     //   //   //           ||||||>")
    print("|       //   //      //////   //  //   //     //   //   //            ||||")
    print("|  //////   /////   //   //  //  //   ///////     //   //             ||")
    print("---------------------------------------------------------------------")


if __name__ == "__main__":
    if((sys.argv[1]=="-h") or (sys.argv[1]=="--help")):
        drawicon()
        print()
        print()
        print("[*] First arg is URL")
        print("[*] Second arg is PATH")
        print()
        print("EXAMPLE:   python ScanDir.py http://example.com/ /usr/share/wordlists/dirbuster/small.txt")
        print()
        print("------------------------------------------")
    else:
        drawicon()
        print()
        print()
        url = sys.argv[1]
        dic = sys.argv[2]
        working(url, dic)







