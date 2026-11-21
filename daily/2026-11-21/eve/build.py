import sys
sys.path.insert(0,'/workspace/premium'); sys.path.insert(0,'/workspace/social/tiktok_night1')
import scen
from scen import *
import importlib.util
spec=importlib.util.spec_from_file_location('tv','/workspace/social/tiktok_night1/vids.py'); tv=importlib.util.module_from_spec(spec)
_a=sys.argv; sys.argv=['x']; spec.loader.exec_module(tv); sys.argv=_a
G,GD,hook,cap,endcard,vb=tv.G,tv.GD,tv.hook,tv.cap,tv.endcard,tv.vb
scen.C='/workspace/social/daily_2026-11-21/eve/hd/'
OUT='/workspace/social/daily_2026-11-21/eve/out/'
V={}
# ZA-02a: variation of best performer (ZA-01 water signs, YT 166 views) -> 2027 Year Ahead 4600018290
V['earth27']=dict(music='mystic',scenes=lambda:[
 Sc('n243.mp4',1.0,3.9,(.5,.5),(1.0,1.12),speed=.8,grade=G,vo='Earth signs. Taurus, Virgo, Capricorn. Your twenty twenty seven starts here.',els=hook('TAURUS · VIRGO · CAPRICORN','EARTH SIGNS 2027','your year starts here',tsz=104)),
 Sc('v229.mp4',2.0,4.0,(.5,.6),(1.0,1.1),speed=.85,grade=G,vo='Taurus. Saturn and Neptune move through your quiet twelfth house. Rest is part of the plan.',els=vb(('TAURUS','rest is part of the plan'),size=70)),
 Sc('v229.mp4',9.0,4.0,(.5,.6),(1.08,1.0),speed=.85,grade=G,vo='Virgo. Jupiter enters your sign in late July. A new chapter that is about you.',els=vb(('VIRGO','jupiter arrives in late july'),size=70)),
 Sc('v229.mp4',15.0,4.0,(.5,.6),(1.0,1.1),speed=.85,grade=G,vo='Capricorn. Saturn in Aries puts home and roots in focus. Build the base first.',els=vb(('CAPRICORN','home and roots in focus'),size=66)+cap('which earth sign are you?',t0=.6)),
 endcard('2027','YEAR AHEAD TAROT','WRITTEN PDF  ·  MONTH BY MONTH','Maeve Cross. Year ahead tarot reading.','n229.mp4',6,(.5,.5)),
])
# ZA-02b: air signs -> 2027 Year Ahead 4600018290
V['air27']=dict(music='mystic',scenes=lambda:[
 Sc('n223.mp4',1.0,3.9,(.5,.5),(1.0,1.12),speed=.8,grade=G,vo='Air signs. Gemini, Libra, Aquarius. Your twenty twenty seven starts here.',els=hook('GEMINI · LIBRA · AQUARIUS','AIR SIGNS 2027','your year starts here',tsz=110)),
 Sc('v298.mp4',0.5,4.0,(.5,.45),(1.05,1.15),speed=.8,grade=G,vo='Gemini. Uranus is in your sign all year. Give yourself room to reinvent.',els=vb(('GEMINI','room to reinvent'),size=70)),
 Sc('v298.mp4',4.5,4.0,(.5,.45),(1.15,1.05),speed=.8,grade=G,vo='Libra. Saturn in Aries asks for honest conversations in your partnerships.',els=vb(('LIBRA','honest talks in love'),size=70)),
 Sc('v229.mp4',9.0,4.0,(.5,.6),(1.0,1.1),speed=.85,grade=G,vo='Aquarius. Jupiter in Leo lights up your relationship sector until late July.',els=vb(('AQUARIUS','relationships in the spotlight'),size=64)+cap('which air sign are you?',t0=.6)),
 endcard('2027','YEAR AHEAD TAROT','WRITTEN PDF  ·  MONTH BY MONTH','Maeve Cross. Year ahead tarot reading.','n223.mp4',9,(.5,.5)),
])
# ZA-05 (new, timely): last quarter moon Dec 1 2026 06:08 UTC (USNO) -> One Question Reading 4620791021
V['lqmoon']=dict(music='night',scenes=lambda:[
 Sc('n101.mp4',1.0,3.9,(.5,.45),(1.0,1.12),speed=.8,grade=G,vo='If you see this before December first, this is for you.',els=hook('IF YOU SEE THIS BEFORE','DECEMBER 1ST','this one is for you',tsz=118)),
 Sc('n101.mp4',6.0,4.0,(.5,.45),(1.1,1.0),speed=.8,grade=GD,vo='The full moon has passed. On December first, the moon reaches its last quarter.',els=vb(('LAST QUARTER MOON','december 1st'),size=56)),
 Sc('v298.mp4',4.0,4.0,(.5,.45),(1.05,1.15),speed=.8,grade=G,vo='A waning moon is a classic time to clear things out. Pick one thing to let go before December.',els=vb(('LET ONE THING GO','before december begins'),size=58)+cap('what is yours? one word',t0=.6)),
 Sc('v229.mp4',15.0,3.8,(.5,.6),(1.08,1.0),speed=.85,grade=G,vo='Then ask one clear question for the month ahead.',els=vb(('ONE QUESTION','for the month ahead'),size=64)),
 endcard('ONE QUESTION','PSYCHIC READING','ONE QUESTION  ·  WRITTEN PDF','Maeve Cross. One question readings.','n101.mp4',3,(.5,.45)),
])
if __name__=='__main__':
    name=sys.argv[1]; v=V[name]
    print(render_scenario(v['scenes'](),1080,1920,OUT+name+'.mp4',social=True,music=v['music'],grade=G))
