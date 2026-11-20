import sys
sys.path.insert(0,'/workspace/premium'); sys.path.insert(0,'/workspace/social/tiktok_night1')
import scen
from scen import *
import importlib.util
spec=importlib.util.spec_from_file_location('tv','/workspace/social/tiktok_night1/vids.py'); tv=importlib.util.module_from_spec(spec)
_a=sys.argv; sys.argv=['x']; spec.loader.exec_module(tv); sys.argv=_a
G,GD,hook,cap,endcard,vb=tv.G,tv.GD,tv.hook,tv.cap,tv.endcard,tv.vb
scen.C='/workspace/social/daily_2026-11-20/eve/hd/'
OUT='/workspace/social/daily_2026-11-20/eve/out/'
V={}
# EG-04 video variant: 5 things before an egg cleanse -> Egg Cleanse 4487175574
V['egg5']=dict(music='candle',scenes=lambda:[
 Sc('n56.mp4',14.0,3.9,(.5,.5),(1.0,1.14),speed=.8,grade=G,vo='Before you do an egg cleanse, here are five things to know.',els=hook('BEFORE AN EGG CLEANSE','5 THINGS','save this for later',tsz=150)),
 Sc('n141.mp4',3.0,3.6,(.5,.55),(1.0,1.1),speed=.8,grade=G,vo='One. Write down one clear question first.',els=vb(('1 · ONE QUESTION','write it down first'),size=58)),
 Sc('n63.mp4',12.0,3.6,(.5,.55),(1.05,1.18),grade=G,vo='Two. Use a clear glass and clean water, so you can see everything.',els=vb(('2 · A CLEAR GLASS','clean water, nothing hidden'),size=56)),
 Sc('n56.mp4',3.0,3.6,(.5,.5),(1.12,1.0),speed=.85,grade=G,vo='Three. Photograph the glass, from the side and from above.',els=vb(('3 · PHOTOGRAPH IT','side view and top view'),size=56)),
 Sc('v26.mp4',4.0,3.6,(.5,.6),(1.0,1.1),grade=GD,vo='Four. Treat what you see as reflection, a mirror, not a verdict.',els=vb(('4 · A MIRROR','reflection, not a verdict'),size=60)+cap('which one did you skip?',t0=.6)),
 Sc('n128.mp4',2.0,3.6,(.5,.45),(1.0,1.1),grade=G,vo='Five. Respect the roots. This is an old tradition from many cultures.',els=vb(('5 · RESPECT THE ROOTS','an old tradition, many cultures'),size=50)),
 endcard('EGG CLEANSE','READING WITH PHOTOS','PHOTOS  ·  WRITTEN READING','Maeve Cross. Egg cleanse reading with photos.','v15.mp4',10,(.5,.6)),
])
# DW-01 x DW-02 date window -> One Question Reading 4620791021
V['dw27']=dict(music='night',scenes=lambda:[
 Sc('v301.mp4',0.3,3.9,(.5,.5),(1.0,1.12),speed=.8,loop=True,grade=G,vo='If you see this on November twenty seventh, twenty eighth, or twenty ninth, this is for you.',els=hook('IF YOU SEE THIS ON','NOV 27 · 28 · 29','this one is for you',tsz=92)),
 Sc('v311.mp4',2.0,3.8,(.5,.5),(1.0,1.1),speed=.85,grade=G,vo='Slow down before you answer.',els=vb(('SLOW DOWN','before you answer'),size=62)),
 Sc('n2.mp4',3.0,3.8,(.5,.4),(1.28,1.36),speed=.85,grade=G,vo='The pause is part of the answer.',els=vb(('THE PAUSE','is part of the answer'),size=62)+cap('save it for the 29th',t0=.6)),
 Sc('v311.mp4',8.0,3.6,(.5,.5),(1.1,1.0),grade=G,vo='Send this to someone who needs to hear it.',els=vb(('SEND IT','to someone who needs it'),size=62)),
 endcard('ONE QUESTION','PSYCHIC READING','ONE QUESTION  ·  WRITTEN PDF','Maeve Cross. One question readings.','v27.mp4',6,(.5,.6)),
])
if __name__=='__main__':
    name=sys.argv[1]; v=V[name]
    print(render_scenario(v['scenes'](),1080,1920,OUT+name+'.mp4',social=True,music=v['music'],grade=G))
