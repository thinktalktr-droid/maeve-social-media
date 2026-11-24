import sys,os
sys.path.insert(0,'/workspace/premium')
import scen
from scen import *
scen.C='/workspace/social/tiktok_night1/src/hd/'
G=dict(contrast=1.12,bright=1.08,sat=1.1,shadow=(0.08,0.02,0.07),high=(1,.84,.72),sh_amt=.22)
GD=dict(G,gamma=1.25,bright=.95)
OUT='/workspace/social/tiktok_night1/out/'
WOLF='7325462702988741934.mp4'; INC='inc_d.mp4'; AMY='7566919210073378070.mp4'; DDC='7658336793338596622.mp4'
HP='7656678406527962398.mp4'; EGGC='7321803408107785518.mp4'; EGGG='7286285549617319211.mp4'; SUN='7473840213270269207.mp4'
def hook(kick,title,sub,tsz=120):
    return [('scrim',0,1,0,1,.30,0,'END'),('scrim',.5,1,.5,.9,.62,.2,3.8),
     ('text',kick,'jos',26,.56,.575,.2,3.6,dict(kind='plain',track=7,fill=GOLD,fi=.5)),
     ('text',title,'cin',tsz,.72,.675,.35,3.6,dict(track=5,glow=.55,blur=22,shine=True)),
     ('text',sub,'cormi',46,.85,.775,.9,3.6,dict(kind='plain'))]
def cap(txt,y=.80,t0=.4,t1=3.6):
    return [('scrim',.6,1,.66,.92,.45,t0-.2,t1),('text',txt,'jos',32,.88,y,t0,t1,dict(kind='plain',track=3,fill=PARCH))]
def endcard(l1,l2,pill,vo,clip,ss,focus=(.5,.5)):
    return Sc(clip,ss,3.0,focus,(1.4,1.5),grade=GD,vo=vo,els=[('scrim',0,1,0,1,.62,0.1,'END'),
     ('text','MAEVE CROSS','jos',30,.30,.30,.3,'END',dict(kind='plain',track=14,fill=GOLD)),
     ('text',l1,'cin',92,.50,.43,.35,'END',dict(track=5,glow=.6,blur=22,shine=True)),
     ('text',l2,'jos',40,.585,.50,.6,'END',dict(kind='plain',track=12)),
     ('line',480,.64,.54,.5,'END'),('pill',pill,28,.74,.60,.8,'END'),
     ('text','LINK IN BIO','jos',28,.84,.66,1.1,'END',dict(kind='plain',track=8,fill=GOLD))])
V={}
V['t1']=dict(listing='love',music='mystic',scenes=lambda:[
 Sc(WOLF,12.5,3.8,(.5,.5),(1.0,1.15),grade=G,vo='Pick a card. Trust your first pull.',els=hook('A MESSAGE FOR THIS WEEK','PICK A CARD','one  ·  two  ·  three')),
 Sc(WOLF,26,4.2,(.5,.5),(1.0,1.12),grade=G,vo='One is quiet courage. Two is release. Three is small signs.',els=[
   ('scrim',0,1,0,1,.35,0,3.9),
   ('flip3',.40,.40,.2,1.0,3.9,[(['QUIET','COURAGE'],['one']),(['RELEASE'],['two']),(['SMALL','SIGNS'],['three'])],1.0)]+cap('which one did your hand go to?')),
 Sc(WOLF,52,3.6,(.5,.5),(1.0,1.12),grade=G,vo='Comment your number, and take what fits.',els=[
   ('scrim',.5,1,.55,.9,.6,.2,3.4),
   ('text','COMMENT YOUR NUMBER','cin',58,.77,.72,.35,3.4,dict(track=5,glow=.5,blur=18)),
   ('text','and take what fits','cormi',46,.85,.775,.8,3.4,dict(kind='plain'))]),
 endcard('YOUR READING','IS WAITING','SAME HOUR  ·  WRITTEN PDF','Maeve Cross. Same hour psychic readings.',WOLF,64,(.5,.5)),
])

def vb(txt,t0=.35,t1=3.4,y=(.77,.72),size=58):
    return [('scrim',.5,1,.55,.9,.6,.2,t1),('text',txt[0],'cin',size,y[0],y[1],t0,t1,dict(track=5,glow=.5,blur=18)),('text',txt[1],'cormi',46,.85,.775,t0+.45,t1,dict(kind='plain'))]
V['t2']=dict(listing='yesno',music='night',scenes=lambda:[
 Sc(WOLF,28,3.9,(.5,.5),(1.0,1.15),grade=G,vo='If this found you, it is not an accident. Take a breath.',els=hook('A MESSAGE FOR WHOEVER IS WATCHING','MEANT FOR YOU','listen closely',tsz=88)),
 Sc(WOLF,36,4.2,(.5,.5),(1.0,1.12),grade=G,vo='Something you have been carrying is ready to be set down.',els=vb(('SET IT DOWN','you have carried it long enough'))+cap('what is it for you?',t0=.6)),
 Sc(WOLF,44,3.8,(.5,.5),(1.0,1.12),grade=G,vo='You already know the answer. Trust it.',els=vb(('YOU ALREADY KNOW','trust the first answer'),size=52)),
 endcard('YES OR NO?','PSYCHIC READING','ONE QUESTION  ·  WRITTEN ANSWER','Maeve Cross. Yes or no psychic readings.',WOLF,72),
])
V['t3']=dict(listing='y2027',music='mystic',scenes=lambda:[
 Sc(WOLF,56,3.9,(.5,.5),(1.0,1.15),grade=G,vo='Twenty twenty seven is almost here. How do you want it to feel?',els=hook('THE YEAR AHEAD','2027','what do the cards whisper?',tsz=190)),
 Sc(WOLF,64,4.2,(.5,.5),(1.0,1.12),grade=GD,vo='Choose one word for the year. Say it out loud.',els=vb(('ONE WORD','for the year ahead'))+cap('write it down before you scroll',t0=.6)),
 Sc(WOLF,72,3.8,(.5,.5),(1.0,1.12),grade=G,vo='Then let the cards show you the months.',els=vb(('MONTH BY MONTH','a tarot reading for 2027'),size=50)),
 endcard('2027','YEAR AHEAD TAROT','WRITTEN PDF  ·  MONTH BY MONTH','Maeve Cross. Year ahead tarot reading.',WOLF,78),
])
V['t4']=dict(listing='egg',music='candle',scenes=lambda:[
 Sc(EGGC,4.0,2.6,(.55,.72),(1.7,1.8),speed=.55,grade=G,vo='The egg cleanse. An old tradition, explained in thirty seconds.',els=hook('AN OLD TRADITION, EXPLAINED','EGG CLEANSE','what people look for',tsz=100)),
 Sc(EGGG,72,4.4,(.5,.55),(1.1,1.3),speed=.72,grade=G,vo='Traditionally, people read cloudy water, strings, and bubbles as signs.',els=vb(('SIGNS PEOPLE READ','cloudy water  ·  strings  ·  bubbles'),size=46)),
 Sc(EGGG,162.5,3.6,(.5,.36),(1.5,1.6),grade=GD,vo='Then the water is poured away. A symbol of letting go.',els=vb(('LET IT GO','the water is poured away'))),
 endcard('EGG CLEANSE','READING WITH PHOTOS','PHOTOS  ·  WRITTEN READING','Maeve Cross. Egg cleanse reading with photos.',EGGG,72,(.5,.55)),
])
V['t5']=dict(listing='cord',music='candle',scenes=lambda:[
 Sc(DDC,18,3.9,(.5,.67),(1.4,1.5),grade=G,vo='Light one candle. Name one intention.',els=hook('A TWO MINUTE RESET','ONE CANDLE','one intention',tsz=130)),
 Sc(DDC,30,4.4,(.5,.67),(1.4,1.5),grade=G,vo='Add something that feels like you. A petal, a crystal, a quiet word.',els=vb(('MAKE IT YOURS','a petal  ·  a crystal  ·  a word'),size=52)),
 Sc(SUN,0.4,3.6,(.5,.7),(1.45,1.55),grade=G,vo='Let it burn slowly while you breathe.',els=vb(('BREATHE','let it burn slowly'))),
 endcard('LETTING GO?','CORD CUTTING READING','WRITTEN PDF  ·  SAME DAY','Maeve Cross. Cord cutting reading.',DDC,36,(.5,.67)),
])
V['t6']=dict(listing='brutal',music='night',scenes=lambda:[
 Sc(HP,0,4.0,(.5,.5),(1.5,1.65),grade=G,vo='Card of the day. The High Priestess.',els=hook('CARD OF THE DAY','HIGH PRIESTESS','intuition  ·  quiet knowing',tsz=96)),
 Sc(HP,6,4.2,(.5,.5),(1.4,1.2),grade=G,vo='What you feel is information. Listen before you decide.',els=vb(('LISTEN FIRST','what you feel is information'),size=52)+cap('where do you feel it in your body?',t0=.6)),
 Sc(HP,12,3.6,(.5,.5),(1.2,1.5),grade=G,vo='Not every answer arrives loudly.',els=vb(('SOFT ANSWERS','not every answer is loud'),size=52)),
 endcard('HONEST','TAROT READING','STRAIGHT TALK  ·  WRITTEN PDF','Maeve Cross. Honest tarot guidance.',HP,20,(.5,.5)),
])
V['t7']=dict(listing='egg',music='mystic',scenes=lambda:[
 Sc(INC,0.2,3.7,(.5,.5),(1.0,1.12),grade=G,vo='Open a window. Let the smoke carry it out.',els=hook('A QUIET RESET FOR YOUR SPACE','LET IT CLEAR','breathe out slowly',tsz=120)),
 Sc(INC,3.0,4.0,(.5,.5),(1.12,1.0),grade=GD,vo='Clear the room. Clear the head. Start again.',els=vb(('START AGAIN','clear the room, clear the head'),size=54)),
 endcard('EGG CLEANSE','READING WITH PHOTOS','PHOTOS  ·  WRITTEN READING','Maeve Cross. Egg cleanse reading with photos.',INC,2,(.5,.5)),
])
if __name__=='__main__':
    name=sys.argv[1]; trial=float(sys.argv[2]) if len(sys.argv)>2 else None
    v=V[name]; print(render_scenario(v['scenes'](),1080,1920,OUT+name+'.mp4',social=True,music=v['music'],grade=G,trial=trial))
