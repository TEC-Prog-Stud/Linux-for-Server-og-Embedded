Som anbefalet på https://www.raspberrypi.org/forums/viewtopic.php?f=104&t=109064&p=750616#p810193

Udfør:

```
sudo apt-get install octave
cd
cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
cd RTEllipsoidFit
RTIMULibCal
```

og 

```
rm ~/.config/sense_hat/RTIMULib.ini
sudo cp RTIMULib.ini /etc
```

I filen `demo/deno.py` fra https://github.com/astro-pi/python-sense-hat/blob/master/examples/compass.py
anbefales at kopiere `RTIMULib.ini` til `.`

( syns ikke rigtigt det virker...? )