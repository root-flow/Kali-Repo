#!/usr/bin/env python3
import os,colorama
from colorama import  Fore, Back, Style
colorama.init()                                                               print(Fore.GREEN)                                                             print("#coded by pesimistni")
                                                                              os.system("sudo apt update -y")                                               


os.system("sudo apt install figlet -y")


os.system("clear ")

print(Fore.BLUE)

os.system("figlet Kali Repo")

print("!!Bu Toolun Amacı Kali Reposunu Farklı Linux Dağıtımlarına Kurup Kali Linuxun İçinde Bulunan Pentest  Araçlarini Ubuntu Linux Mint vb. Linux Dağıtımlarına Kurmak Amaçlı Yazılmıştır!!!")

print(Fore.GREEN)
                                                                              print("insta:@pesimistpentester")
                                                                              print(Fore.RED)                                                                                                                                             
print("""


1) Kali Repo Update & Install/ Kali Repo Güncelleme & Kurma

2) GPG ERROR NO_PUBKEY HATASI ÇÖZÜMÜ VE SİSTEM PAKETİ GÜNCELLEME


""")



islemno=input("İşlem Numarasını Giriniz : ")

if islemno=="1":

    repo=input("Devam Etmek İçin Entera Basınız : ")
    os.system("echo deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware | sudo tee /etc/apt/sources.list"+repo)
    os.system("echo deb http://http.kali.org/kali kali-last-snapshot main contrib non-free non-free-firmware | sudo tee /etc/apt/sources.list"+repo)
    os.system("sudo apt update -y"+repo)
    os.system("echo deb http://http.kali.org/kali kali-experimental main contrib non-free non-free-firmware | sudo tee /etc/apt/sources.list.d/kali-experimental.list"+repo)
    os.system("sudo rm /etc/apt/sources.list.d/kali-experimental.list"+repo)
    os.system("echo deb http://http.kali.org/kali kali-bleeding-edge main contrib non-free non-free-firmware  | sudo tee /etc/apt/sources.list.d/kali-bleeding-edge.list"+repo)
    os.system("sudo rm /etc/apt/sources.list.d/kali-bleeding-edge.list"+repo)
    os.system("echo deb-src http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware  | sudo tee -a /etc/apt/sources.list"+repo)

print(Fore.GREEN)
print("#!coded by pesimistda")


if  islemno=="2":

   gpg=input("Devam Etmek İçin Hata Kodunu Giriniz : ")
   os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "+gpg)
   os.system("sudo apt update -y && sudo apt upgrade -y  && sudo apt-get upgrade -y && sudo apt-get update -y && sudo apt-get dist-upgrade -y"+gpg)

print(Fore.RED)
