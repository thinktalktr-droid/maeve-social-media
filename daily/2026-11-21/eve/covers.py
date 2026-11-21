import sys; sys.path.insert(0,'/workspace/social/tools')
import pinlib
C='/workspace/social/work/clips/'
J=[('earth27',C+'n243.mp4',3.0,'TAURUS · VIRGO · CAPRICORN','EARTH SIGNS 2027','your year starts here'),
   ('air27',C+'n223.mp4',3.0,'GEMINI · LIBRA · AQUARIUS','AIR SIGNS 2027','your year starts here'),
   ('lqmoon',C+'n101.mp4',2.0,'IF YOU SEE THIS BEFORE','DECEMBER 1ST','last quarter moon · let one thing go')]
for n,clip,t,k,h,s in J:
    pinlib.pin_img(clip,t,k,h,s,f'out/cover_{n}.jpg',size=(1080,1920),hsize=150,dark=0.5)
print('ok')
