import sys, html
HANDLE = sys.argv[1] if len(sys.argv) > 1 else "@yourhandle"
OUT = sys.argv[2]
N = 9
def esc(s): return html.escape(s, quote=False)

slides = []
# 1 cover
slides.append(("dark", f'''
<div class="kicker">Boxing coaches:</div>
<h1 class="cover">Your reels got <em>100K+ views</em> but your calendar is still <em>empty?</em></h1>
<p class="sub">Here are 4 critical mistakes that are costing you clients... and 1 dead simple solution to fix them all.</p>
<div class="swipe">Swipe &rarr;</div>'''))
# 2 stake
slides.append(("dark", '''
<h2 class="big">Your reel did its job.</h2>
<p class="body">100K people watched it. Your calendar is empty because of what happens in the <em>next 30 seconds</em>, when a stranger taps your name to see if you're the coach for them.</p>'''))
mist = [
 ("A bio written for fighters", '<span class="quote">"Former amateur. DM for coaching."</span> A beginner reads that and can\'t tell if it\'s for them. So they leave.'),
 ("A link that's a menu", "Shop, YouTube, podcast, free guide, coaching. They came for one thing, got seven choices, and picked none."),
 ("Hiding your price", '<span class="quote">"DM me for prices."</span> A nervous beginner won\'t message a stranger to ask what something costs. They\'ll find a coach who just tells them.'),
 ("Making them wait", "They message you at 11pm. You reply at 9am. By then they've booked a call with someone else."),
]
for i,(h,b) in enumerate(mist,1):
    slides.append(("dark", f'''
<div class="label">Mistake {i}</div>
<h2 class="mid">{esc(h)}</h2>
<p class="body">{b}</p>'''))
slides.append(("accent", '''
<div class="label inv">The dead simple fix</div>
<h2 class="big inv">One page.</h2>
<p class="body inv">One offer, one price, one button that puts them straight on your calendar. No DMs, no waiting on you.</p>'''))
slides.append(("light", '''
<div class="label dark">4 mistakes, 1 fix</div>
<ol class="recap">
<li><span>01</span>A bio written for fighters</li>
<li><span>02</span>A link that's a menu</li>
<li><span>03</span>A price hidden in your DMs</li>
<li><span>04</span>Beginners left waiting overnight</li>
</ol>
<p class="fixline">One page fixes all four, and people can book while you sleep.</p>'''))
slides.append(("dark", '''
<h2 class="big">Comment <em>FIX</em></h2>
<p class="body">and I'll tell you which mistake your profile is making.</p>'''))

css = '''
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000}
section{width:1080px;height:1350px;position:relative;overflow:hidden;
 padding:150px 120px;display:flex;flex-direction:column;justify-content:center;
 font-family:"Inter Display","Inter",sans-serif;color:#F2EEE7;background:#151515}
section.light{background:#F2EEE7;color:#151515}
section.accent{background:#C9B79C;color:#151515}
em{font-style:normal;color:#C9B79C}
.kicker{font-size:46px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#C9B79C;margin-bottom:40px}
h1.cover{font-size:104px;line-height:1.0;font-weight:900;letter-spacing:-.02em;margin-bottom:56px}
.sub{font-size:42px;line-height:1.3;font-weight:500;color:#D8D2C8;max-width:840px}
.swipe{position:absolute;right:120px;bottom:120px;font-size:34px;font-weight:700;color:#C9B79C}
h2.big{font-size:124px;line-height:1.0;font-weight:900;letter-spacing:-.02em;margin-bottom:56px}
h2.mid{font-size:92px;line-height:1.02;font-weight:900;letter-spacing:-.02em;margin-bottom:48px}
.body{font-size:48px;line-height:1.32;font-weight:500;color:#D8D2C8}
.body.inv,.big.inv{color:#151515}
.num{font-size:260px;line-height:.8;font-weight:900;color:#C9B79C;letter-spacing:-.04em;margin-bottom:36px}
.label{font-size:36px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#8E877D;margin-bottom:24px}
.label.inv{color:#3A342C}
.label.dark{color:#6B655C;margin-bottom:48px}
.quote{color:#F2EEE7;font-weight:700}
ol.recap{list-style:none}
ol.recap li{font-size:54px;line-height:1.1;font-weight:800;letter-spacing:-.01em;padding:30px 0;border-top:3px solid #151515;display:flex;gap:32px}
ol.recap li:last-child{border-bottom:3px solid #151515}
ol.recap span{color:#9A8562;min-width:90px}
.fixline{font-size:46px;line-height:1.3;font-weight:600;margin-top:56px}
.foot{position:absolute;left:120px;right:120px;bottom:64px;display:flex;justify-content:space-between;
 font-size:32px;font-weight:600;color:#8E877D}
section.light .foot{color:#6B655C} section.accent .foot{color:#3A342C}
.cover-sec .foot{bottom:64px}
'''
parts = []
for i,(kind,inner) in enumerate(slides,1):
    foot = f'<div class="foot"><span>{esc(HANDLE)}</span><span>{i}/{N}</span></div>'
    if i == 1: foot = f'<div class="foot"><span>{esc(HANDLE)}</span><span></span></div>'
    parts.append(f'<section class="{kind}" id="s{i}">{inner}{foot}</section>')
open(OUT,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(parts)}</body></html>')
