# Læg et image af Raspberry Pi OS på sd-kort

Denne opskrift viser hvordan man lægger et _Raspberry Pi OS Lite_ image på et sd-kort, og sætter det op til at starte "headless". I denne sammenhæng er "headless" at starte Raspberry Pi'en op, uden skærm, men tilsluttet wifi, så man kan (fjern)styre den, fra en anden computer med __`ssh`__.

Vi bruger __Raspberry Pi OS Lite (64-bit)__, som debian linux. porteret til Raspberry Pi ARM processor.  


"__Lite__" er _uden_ GUI (X-windows).

Til at skrive imaget til sd-kortet bruger vi Rasperry Pi's ejet program __`rpi-imager`__.  
Imager tilføjer nogle indstilliger på sd-kortet, efter imaget er skrevet ned på det. Derfor skal __`rpi-imager`__ køres som root, så programmet  får fuld adgang til de nyskrevne partitioner, på sd-kortet.

## Opskrift

1.  Download Imager, som .deb-fil  
    ![](2022-02-20-21-56-10.png)

1.  Installer Imager
    * Chrome  
    klik på den downloadede fil...  
    ![](2022-02-20-21-58-29.png)
    * Firefox  
        * gem filen
        * åbne file, og dbl-klik på den gemte fil


2.  Klik __Install__  
    ![](2022-02-20-22-02-04.png)

3.  start _Imager_ __som root__ med
    ```bash
     sudo rpi-imager
    ```
    ![](2022-02-20-18-58-44.png)
4.  Tryk på: _CHOOSE OS_:  
5.  Vælg _Raspberry PI OS (other)_:  
    ![](2022-02-20-19-06-02.png)
6.  Vælg _Raspberry Pi OS Lite (64-bit)_:  
    ![](2022-02-20-19-09-24.png)
7.  Vælg _Mass Storage_Device - 31.3 GB_: (eller hvad der dukker frem, og ligner et sd-kort på ca 32GB)  
    ![](2022-02-20-19-13-08.png)
8.  Tryk nu på Tandhjulet:  
    ![](2022-02-20-19-30-24.png) 
9.  Vælg:
    * [x] _Set hostname:_ noget med dine initialer
    * [x] _Enable SSH_ og
      * [x] _Use password authentication_  
    ![](2022-02-20-19-32-25.png)  
    og scoll ned:
10. vælg også:
    * [x] _Set username and password:_ 
      * [x] _Username:_ __`pi`__ er fint
      * [x] _Password:_ find på noget godt, __og skriv det ned! Ellers er du fu****!__
    ![](2022-02-20-19-47-03.png)
11. og ...
    * [x] Configure wifi
      * [x] _SSID:_ __`LinEmb`__
      * [x] _Password_: __`28368557`__ 
      * _wifi country_: __`DK`__  
    ![](2022-02-20-19-52-07.png)
12. og ... til sidst:
    * [x] _Set locale settings_:
        * _Time zone:_ __`Europe/Copenhagen`__
        * _Keyboard layout:_ lige meget, vi sætter helst ikke keyboard til...  
    ![](2022-02-20-19-54-38.png)
13. Tryk på _SAVE_  
    ![](2022-02-20-20-44-50.png)
14. Tryk på _WRITE_  
    ![](2022-02-20-20-45-26.png)
15. Tryk på _YES_, for at slette sd-kortet ... (håber du har valgt det rigtige... ;-) )
    ![](2022-02-20-20-46-05.png)
16. Vente, vente, vente ...   
    ![](2022-02-20-20-46-41.png)
17. Færdig!
    * skub sdkortet ud (unmount)
    * træk kortlæseren ud, fysisk.
    * sørg for at strømmen på "din" Raspberry Pi er ude
    * sæt sd-kortet i Raspberry Pi'en
    * sæt strøm til Raspberry Pi'en
    * vent lidt...  
    ![](2022-02-20-20-53-56.png)

18. Tilslut til "din" RaspberryPi med kommandoen:
    ```bash
    ssh pi@smagpi.local
    ```

    Det virker hvis du skriver brugernavnet (fra ovenfor) foran `@`'et, bruger hostnavnet (også fra ovenfor) efter `@`'et, og `.local` efter hostnavnet. 

    ![](2022-02-20-21-16-34.png)





