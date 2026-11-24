import json
LIST={'love':('4476113245','Psychic Love Reading'),'yesno':('4475221227','Yes or No Psychic Reading'),'y2027':('4600018290','2027 Year Ahead Tarot Reading'),'egg':('4487175574','Egg Cleanse Reading With Photos'),'cord':('4475065546','Cord Cutting Reading'),'brutal':('4482663151','Brutal Tarot Reading')}
DISC='For reflection and entertainment only, 18+.'
BOARDS={'tarot':'961729764116915435','egg':'961729764116958216','candle':'961729764117057202','evil':'961729764117057203','protect':'961729764117057204'}
T={
't1':dict(listing='love',hook='PICK A CARD 🔮 A message for this week',body='Choose 1, 2 or 3, then read your pile.\n\n1 — Quiet courage. 2 — Release. 3 — Small signs.',q='Which number did your hand go to? 👇',
  de='Wähle 1, 2 oder 3: deine Botschaft für diese Woche.',es='Elige 1, 2 o 3: tu mensaje para esta semana.',tags='#pickacard #tarotreading #psychicreading #tarotcommunity #tarot',
  yt='Pick a Card 🔮 Your Message This Week | Tarot Reading #shorts',pin_title='Pick a Card Tarot: Your Message This Week (1, 2 or 3)',
  pin_desc='Pick a card tarot reading for this week: choose pile 1, 2 or 3. Quiet courage, release, or small signs? Want a same hour psychic reading about your own situation? Written by Maeve Cross.',board='tarot',
  src='TikTok @atonthelemedia? no: @thewolfinlace 7325462702988741934'),
't2':dict(listing='yesno',hook='MEANT FOR YOU 🔮 If this found you, take a breath.',body='Something you have been carrying is ready to be set down. You already know the answer. Trust the first one that came to mind.',q='What is the one thing you are ready to put down? 👇',
  de='Wenn dich dieses Video gefunden hat: atme tief durch. Du kennst die Antwort schon.',es='Si este video te encontró, respira hondo. Ya conoces la respuesta.',tags='#tarotreading #tarotmessage #psychicreading #intuition #tarotcommunity',
  yt='Meant For You 🔮 If You See This, Take a Breath | Tarot Message #shorts',pin_title='A Tarot Message If You Need One Today: You Already Know the Answer',
  pin_desc='A quiet tarot message for whoever needs it today: something you have been carrying is ready to be set down. Have one clear question? A yes or no psychic reading gives a written answer from Maeve Cross.',board='tarot',src='TikTok @thewolfinlace 7325462702988741934'),
't3':dict(listing='y2027',hook='2027 IS ALMOST HERE 🌙 Choose one word for the year ahead.',body='Say it out loud. Write it down before you scroll. Then let the cards show you the months.',q='What is your one word for 2027? 👇',
  de='2027 steht vor der Tür: Wähle ein Wort für das neue Jahr.',es='2027 está por llegar: elige una palabra para el año.',tags='#2027 #tarotreading #yearahead #tarotcommunity #psychicreading',
  yt='2027 Is Almost Here 🌙 Choose One Word | Year Ahead Tarot #shorts',pin_title='2027 Year Ahead Tarot Reading: Month by Month',
  pin_desc='2027 year ahead tarot reading, month by month, as a written PDF from Maeve Cross. Choose one word for the year, then see what the cards say about each month.',board='tarot',src='TikTok @thewolfinlace 7325462702988741934'),
't4':dict(listing='egg',hook='THE EGG CLEANSE, EXPLAINED 🥚',body='An old tradition: an egg is passed over the body, then cracked into a glass of water. People traditionally read cloudy water, strings and bubbles as symbolic signs.',q='Have you ever tried one? 👇',
  de='Die Ei-Reinigung, erklärt: eine alte Tradition mit Symbolen.',es='La limpia con huevo, explicada: una tradición antigua con símbolos.',tags='#eggcleanse #limpiaconhuevo #spiritualtiktok #psychicreading #tarotcommunity',
  yt='The Egg Cleanse, Explained 🥚 What the Signs Traditionally Mean #shorts',pin_title='Egg Cleanse Explained: What Cloudy Water, Strings and Bubbles Traditionally Mean',
  pin_desc='The egg cleanse explained: an old tradition where an egg is cracked into water and the shapes are read as symbols. Personal egg cleanse reading with photos and a PDF explaining each sign, by Maeve Cross.',board='egg',src='TikTok @circeboutique 7321803408107785518 + @genatew2 7286285549617319211'),
't5':dict(listing='cord',hook='ONE CANDLE. ONE INTENTION. 🕯️',body='A two minute reset: light a candle, name one intention, add something that feels like you, and breathe while it burns slowly.',q='What is your intention tonight? 👇',
  de='Eine Kerze, eine Absicht: ein Reset in zwei Minuten.',es='Una vela, una intención: un reinicio de dos minutos.',tags='#candlelight #intentions #tarotcommunity #psychicreading #witchyvibes',
  yt='One Candle, One Intention 🕯️ A Two Minute Reset #shorts',pin_title='Two Minute Candle Reset: One Candle, One Intention',
  pin_desc='A two minute candle reset: light one candle, name one intention, breathe while it burns. Letting go of someone or something? A cord cutting reading, written for you by Maeve Cross.',board='candle',src='TikTok @darklydivinecrystals 7658336793338596622 + @dropsofsunlight 7473840213270269207'),
't6':dict(listing='brutal',hook='CARD OF THE DAY 🌙 The High Priestess',body='Intuition and quiet knowing. What you feel is information, so listen before you decide. Not every answer arrives loudly.',q='Where do you feel your intuition in your body? 👇',
  de='Tageskarte: Die Hohepriesterin. Hör zuerst auf dein Gefühl.',es='Carta del día: La Sacerdotisa. Escucha primero lo que sientes.',tags='#tarotcardoftheday #highpriestess #tarotreading #intuition #psychicreading',
  yt='Card of the Day 🌙 The High Priestess | Intuition #shorts',pin_title='The High Priestess Tarot Card: Intuition and Quiet Knowing',
  pin_desc='The High Priestess tarot card of the day: intuition, quiet knowing, and listening before you decide. Want honest guidance written for your situation? A brutal tarot reading by Maeve Cross.',board='tarot',src='TikTok @atonthelemedia 7656678406527962398'),
't7':dict(listing='egg',hook='LET IT CLEAR 🌫️ A quiet reset for your space.',body='Open a window. Breathe out slowly. Let the smoke carry the heaviness out of the room, then start again.',q='What do you want to clear out this week? 👇',
  de='Lass es los: ein ruhiger Neustart für deinen Raum.',es='Déjalo ir: un reinicio tranquilo para tu espacio.',tags='#incense #resetyourenergy #spiritualtiktok #tarotcommunity #psychicreading',
  yt='Let It Clear 🌫️ A Quiet Reset For Your Space #shorts',pin_title='A Quiet Reset for Your Space: Incense Smoke and a Fresh Start',
  pin_desc='A quiet reset for your space: open a window, breathe out slowly, start again. Curious about the egg cleanse tradition? A personal egg cleanse reading with photos and a PDF, by Maeve Cross.',board='protect',src='TikTok @hey_its_sheena.g 7594474027503176990'),
}
T['t1']['src']='TikTok @thewolfinlace 7325462702988741934'
def url(t,plat):
    lid=LIST[T[t]['listing']][0]; return f'https://www.etsy.com/listing/{lid}?utm_source={plat}&utm_medium=social&utm_campaign=tiktok_night1&utm_content={t}'
def cap(t,plat):
    m=T[t]; name=LIST[m['listing']][1]
    if plat=='instagram':
        return f"{m['hook']}\n\n{m['body']}\n\n{m['q']}\n\nLink in bio → Etsy shop → {name}.\n\nDE: {m['de']}\nES: {m['es']}\n\n{m['tags']}\n\n{DISC}"
    if plat=='youtube':
        return f"{m['hook']}\n\n{m['body']}\n\n{m['q']}\n\n{name} by Maeve Cross: {url(t,'youtube')}\n\nDE: {m['de']}\nES: {m['es']}\n\n#shorts {' '.join(m['tags'].split()[:2])}\n\n{DISC}"
    if plat=='facebook':
        return f"{m['hook']}\n\n{m['body']}\n\n{m['q']}\n\nWant the {name}? Comment READING and I will send you the link.\n\nDE: {m['de']}\nES: {m['es']}\n\n{DISC}"
    if plat=='pinterest':
        return f"{m['pin_desc']}\n\nDE: {m['de']}\nES: {m['es']}\n\n{DISC}"
