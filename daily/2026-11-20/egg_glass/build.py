import sys
sys.path.insert(0,'/workspace/social/tiktok_night1')
sys.argv=[sys.argv[0]]
import vids
from vids import *
import scen
scen.C='/workspace/social/daily_2026-11-20/v1/src/'
OUT='/workspace/social/daily_2026-11-20/v1/out/'
B='n63.mp4'; S='n56.mp4'; K='n82.mp4'; F='n193.mp4'
def hook2(kick,title,tsz=110):
    return [('scrim',0,1,0,1,.30,0,'END'),('scrim',.5,1,.5,.9,.62,.2,3.8),
     ('text',kick,'jos',30,.56,.60,.15,3.6,dict(kind='plain',track=7,fill=GOLD,fi=.4)),
     ('text',title,'cin',tsz,.72,.69,.3,3.6,dict(track=5,glow=.55,blur=22,shine=True))]
sc=[
 Sc(B,1.0,3.6,(.5,.5),(1.0,1.18),grade=G,vo='If you did an egg cleanse, this is how the glass is traditionally read.',els=hook2('IF YOU DID AN EGG CLEANSE','READ THE GLASS',tsz=86)),
 Sc(B,9.0,4.0,(.5,.5),(1.18,1.05),grade=G,vo='Bubbles are often read as energy rising, and leaving.',els=vb(('BUBBLES','energy rising, and leaving'))+cap('which one did you see?',y=.84,t0=.9)),
 Sc(S,2.0,4.2,(.5,.55),(1.05,1.2),grade=G,vo='Strings and webs are traditionally read as tension, something you keep carrying.',els=vb(('STRINGS & WEBS','tension you keep carrying'),size=54)),
 Sc(S,12.0,4.0,(.5,.6),(1.2,1.08),grade=GD,vo='Cloudy water? Many readers simply say: rest, reset, and look again.',els=vb(('CLOUDY WATER','rest, reset, look again'),size=56)),
 Sc(K,0.0,3.6,(.5,.55),(1.06,1.16),speed=.6,grade=G,vo='My egg cleanse reading comes with photos, and a written reading.',els=vb(('PHOTOS + WRITTEN READING','done by hand, step by step'),size=46)),
 endcard('EGG CLEANSE','READING WITH PHOTOS','PHOTOS  ·  WRITTEN READING','Maeve Cross. Egg cleanse reading with photos.',F,0.3,(.5,.5)),
]
trial=float(sys.argv_t) if hasattr(sys,'argv_t') else None
print(render_scenario(sc,1080,1920,OUT+'egg_glass.mp4',social=True,music='candle',grade=G,fx=('267.mp4',2)))
