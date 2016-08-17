# RadioStationLocatingTools
Using RTL-SDR and python to find the location of RadioStations based off powerlevel

The main part of this system is the cheap RTL-SDR. In this case I have 3 two of which I bought thru NewEgg and one that I bought thru Adfruit.
I will be using the one from Adfruit becasue it is smaller and also has better filtering built in.



##Requirments
A modified version of https://github.com/roger-/pyrtlsdr which will be on my github.

Numpy (Used for converting I/Q data into data that can be used)

googlemaps (Used for positional data)

livejson (Used for storage of locational information)

##Equipment

1 x RTL2832 w/R820T USB Software Defined Radio

1 x WideBand Antenna (50-2000Mhz)

1 x Laptop (In my case a dell N15500 Inspiron )

1 x 8 GB USB for the collected data (Recomended but not required)

This also requires and internet connection for colelction of the location data. (Unless tyou manually enter in the data)