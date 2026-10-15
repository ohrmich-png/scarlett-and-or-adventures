posts=[("pc-bridge","Connecting Scarlett to the PC","The bridge setup that lets Scarlett reach Or's computer.","Setup"),
("whatsapp-gateway","The WhatsApp gateway saga","Moving the gateway from a VM to a laptop.","Migration"),
("android-apps","Custom Android apps","Mic, camera, audio and a boot orchestrator.","Apps"),
("tuya-smart-home","Smart home with Tuya","Putting the house under Scarlett's control.","Home"),
("telegram-client","The Telegram user-client setup","Getting Scarlett onto Telegram as a user.","Messaging")]
def head(t,css): return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><title>{t}</title><link rel="stylesheet" href="{css}style.css"></head><body>'
def nav(r): return f'<nav><div><b><a href="{r}index.html" style="color:inherit">Scarlett &amp; Or</a></b><span>Private draft</span></div></nav>'
def link(x,arrow_left):
    if not x: return ""
    return f'<a href="{x[0]}.html">&larr; {x[1]}</a>' if arrow_left else f'<a href="{x[0]}.html">{x[1]} &rarr;</a>'
s,t,d,g=posts[0]
feat=f'<a class="featured" href="posts/{s}.html"><span class="tag">{g}</span><h2>{t}</h2><p>{d}</p><span class="more">Read the story &rarr;</span></a>'
cards="".join(f'<a class="card" href="posts/{s}.html"><span class="tag">{g}</span><h2>{t}</h2><p>{d}</p></a>' for s,t,d,g in posts[1:])
open("index.html","w").write(head("Scarlett &amp; Or: Adventures","")+nav("")+f'<div class="wrap"><section class="hero"><div class="eyebrow">An adventure log</div><h1>Scarlett &amp; Or: what we built together</h1><p>Bridges, gateways, apps and a house that listens. A running chronicle of the projects, the detours and the fixes.</p><div class="stats"><span class="pill">5 stories</span><span class="pill">In progress</span></div></section>{feat}<div class="grid">{cards}</div><footer>Draft. Stories are placeholders until Scarlett sends her notes.</footer></div></body></html>')
for i,(s,t,d,g) in enumerate(posts):
    p=posts[i-1] if i>0 else None; n=posts[i+1] if i<4 else None
    pn=f'<div class="pn"><span>{link(p,True)}</span><span>{link(n,False)}</span></div>'
    open(f"posts/{s}.html","w").write(head(t,"../")+nav("../")+f'<div class="wrap"><a class="back" href="../index.html">&larr; All adventures</a><article><span class="tag">{g}</span><h1>{t}</h1><div class="meta">Draft &middot; Scarlett &amp; Or</div><p class="lede">{d}</p><div class="draft">Story coming. Waiting for Scarlett\'s notes.</div>{pn}</article></div></body></html>')
