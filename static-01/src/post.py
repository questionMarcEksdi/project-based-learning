import sys, html
HANDLE = sys.argv[1] if len(sys.argv) > 1 else "@fist_funnel"
OUT = sys.argv[2]
comments = [
  "That slip, body shot, cross combo is fantastic 🔥",
  "That jab snaps back so fast I almost didn't see it 🔥",
  "Love the hip turn on the hook and the timing too 🔥",
]
bubbles = "".join(f'''<div class="c"><div class="av"></div><div class="ct"><div class="un"></div><div class="tx">{html.escape(t, quote=False)}</div></div><div class="hr">&#9825;</div></div>''' for t in comments)
css = '''
*{margin:0;padding:0;box-sizing:border-box}
section{width:1080px;height:1350px;position:relative;overflow:hidden;padding:130px 120px 160px;
 display:flex;flex-direction:column;justify-content:center;background:#151515;color:#F2EEE7;
 font-family:"Inter Display","Inter","Noto Color Emoji",sans-serif}
.kicker{font-size:40px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#C9B79C;margin-bottom:22px}
.intro{font-size:54px;line-height:1.08;font-weight:900;letter-spacing:-.015em;margin-bottom:34px}
.c{display:flex;align-items:flex-start;gap:24px;background:#222120;border:2px solid #2E2C29;border-radius:28px;padding:20px 26px;margin-bottom:16px}
.av{width:52px;height:52px;border-radius:50%;background:#3A3733;flex:none}
.ct{flex:1}
.un{width:150px;height:14px;border-radius:7px;background:#3A3733;margin:4px 0 10px}
.tx{font-family:"Inter","Noto Color Emoji",sans-serif;font-size:34px;line-height:1.28;font-weight:500;color:#E8E3DB}
.hr{font-size:40px;color:#6B655C;line-height:1;margin-top:4px}
.big{font-size:84px;line-height:1.0;font-weight:900;letter-spacing:-.025em;color:#C9B79C;margin-top:34px}
.why{font-size:52px;font-weight:800;margin-top:18px}
.foot{position:absolute;left:120px;right:120px;bottom:64px;display:flex;justify-content:space-between;font-size:32px;font-weight:600;color:#8E877D}
'''
body = f'''<section id="s1">
<div class="kicker">Boxing coaches:</div>
<div class="intro">Your reels got 100s of comments like these:</div>
{bubbles}
<div class="big">But none of them paid you.</div>
<div class="why">Here's why:</div>
<div class="foot"><span>{html.escape(HANDLE)}</span><span></span></div>
</section>'''
open(OUT,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body style="margin:0">{body}</body></html>')
