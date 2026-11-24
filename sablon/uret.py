import sys, json, math, pathlib, urllib.parse
F="/tmp/claude-0/-home-claude/e4078794-d118-58c8-ae91-574e45574d6e/scratchpad/sablon/fonts"
C=dict(zemin="#0B1B32",kutu="#112440",izgara="#132846",cizgi="#203E68",yumusak="#A6B8D2",turuncu="#F28C28",metin="#0E2442",gri="#7A869A")
COL0,COL1=181.49,413.78; W=180.0; L=round((COL0+COL1)/2-W/2,2); R=L+W; CW=COL1-COL0
BADGE_W=78.0
def grid():
    g=[f'<rect width="{CW:.2f}" height="841.89" fill="{C["zemin"]}"/>']
    x=0.0
    while x<CW: g.append(f'<line x1="{x:.3f}" y1="0" x2="{x:.3f}" y2="841.89" stroke="{C["izgara"]}" stroke-width="0.35"/>'); x+=6.977
    y=0.0
    while y<842: g.append(f'<line x1="0" y1="{y:.3f}" x2="{CW:.2f}" y2="{y:.3f}" stroke="{C["izgara"]}" stroke-width="0.35"/>'); y+=6.977
    return f'<svg class="col" viewBox="0 0 {CW:.2f} 841.89" width="{CW:.2f}pt" height="841.89pt">{"".join(g)}</svg>'
GRID=grid()
dot=urllib.parse.quote(f'<svg xmlns="http://www.w3.org/2000/svg" width="8.02" height="8.02" viewBox="0 0 8.02 8.02"><circle cx="3.5" cy="3.5" r="0.4" fill="#fff" fill-opacity="0.2"/></svg>')
# zorluk group: centred in free space between badge end and R
gap_l=L+BADGE_W; zw=15+5+4*7.3+4.9; zx0=(gap_l+R)/2-zw/2
circ="".join(f'<div class="c" style="left:{zx0+20+i*7.3:.2f}pt"></div>' for i in range(5))
def page(q):
    left=""
    if q.get("cozum"):
        left=f'<div class="sol"><div class="sh">ÇÖZÜM · SORU {q["no"]}</div>'+"".join(f'<p>{l}</p>' for l in q["cozum"])+'</div>'
    ans=f'<div class="ans"><div class="al">DOĞRU CEVAP</div><div class="av">{q["cevap"]}</div><div class="ak">{q.get("kaynak","")}</div></div>' if q.get("cevap") else ""
    ch="".join(f'<span><b>{k})</b> {v}</span>' for k,v in q["secenek"])
    tag=f'<div class="tag">ÖSYM · {q["etiket"]}</div>' if q.get("etiket") else ""
    return f'''<div class="pg">{left}{ans}{GRID}<div class="edge" style="left:{COL0}pt"></div><div class="edge" style="left:{COL1-1.4:.2f}pt"></div>
<div class="badge" style="left:{L}pt">EKSEN MATEMATİK</div>
<div class="z" style="left:{zx0:.2f}pt">ZORLUK</div>{circ}
<div class="stack"><div class="card">{q["govde"]}<div class="ch {q.get('chcls','')}">{ch}</div>{tag}</div><div class="lb">ÇÖZÜM</div><div class="box"><svg width="100%" height="100%"><defs><pattern id="d" width="8.02" height="8.02" patternUnits="userSpaceOnUse"><circle cx="3.5" cy="3.5" r="0.4" fill="#fff" fill-opacity="0.2"/></pattern></defs><rect width="100%" height="100%" fill="url(#d)"/></svg></div></div>
</div>'''
def build(qs,out):
    css=f'''
@font-face{{font-family:AB;src:url(file://{F}/fontsource-archivo-black-5.0.13/files/archivo-black-latin-ext-400-normal.woff2);}}
@font-face{{font-family:AB;src:url(file://{F}/fontsource-archivo-black-5.0.13/files/archivo-black-latin-400-normal.woff2);unicode-range:U+0000-00FF;}}
@font-face{{font-family:JB;font-weight:700;src:url(file://{F}/fontsource-jetbrains-mono-5.0.20/files/jetbrains-mono-latin-700-normal.woff2);}}
@font-face{{font-family:JB;font-weight:700;src:url(file://{F}/fontsource-jetbrains-mono-5.0.20/files/jetbrains-mono-latin-ext-700-normal.woff2);unicode-range:U+0100-024F;}}
@page{{size:595.28pt 841.89pt;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
.pg{{position:relative;width:595.28pt;height:841.89pt;overflow:hidden;page-break-after:always;background:#fff;font-family:Inter}}
.pg>*{{position:absolute}}
.col{{left:{COL0}pt;top:0}}
.edge{{top:0;width:1.4pt;height:841.89pt;background:{C['turuncu']}}}
.badge{{top:49.2pt;width:{BADGE_W}pt;height:11.5pt;border-radius:1.6pt;background:{C['turuncu']};color:{C['zemin']};font:6.4pt/11.5pt AB;text-align:center;letter-spacing:.25pt}}
.z{{top:52.6pt;font:700 3.7pt/1 JB;letter-spacing:.3pt;color:{C['yumusak']}}}
.c{{top:51.8pt;width:4.9pt;height:4.9pt;border:0.35pt solid {C['yumusak']};border-radius:50%}}
.stack{{left:{L}pt;top:68pt;width:{W}pt;height:{317.4-68}pt;display:flex;flex-direction:column}}
.card{{position:relative;background:#fff;box-shadow:2pt 2pt 0 {C['turuncu']};padding:8pt 9pt 9pt 9pt;color:{C['metin']};font-size:6.3pt;line-height:1.42}}
.card p{{margin-bottom:3pt}}
.card .q{{font-weight:700;margin-top:4pt}}
.card i{{font-style:italic}}
.card svg{{display:block;margin:2pt auto 5pt auto}}
.ch{{display:flex;justify-content:space-between;align-items:center;margin-top:6pt}}
.ch>span{{display:inline-flex;align-items:center;gap:1.5pt}}
.ch.iki,.ch.uc{{flex-wrap:wrap;justify-content:center;row-gap:3.5pt}}
.ch.iki>span{{width:50%}}
.ch.uc>span{{width:33.33%}}
.fr{{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;font-size:.92em;line-height:1.15;margin:0 .8pt}}
.fr>span:first-child{{border-bottom:0.45pt solid currentColor;padding:0 1pt}}
.eq{{text-align:center;margin:4pt 0 5pt 0}}
.eq div{{margin:2.5pt 0}}
.ch b{{color:{C['turuncu']};font-weight:600}}
.tag{{position:absolute;right:6pt;bottom:2.6pt;font-size:4.2pt;color:{C['gri']};letter-spacing:.2pt}}
.lb{{margin-top:4.8pt;font:700 3.7pt/1 JB;letter-spacing:.3pt;color:{C['yumusak']}}}
.box svg{{display:block}}
.box{{margin-top:3.6pt;flex:1;min-height:140pt;background:{C['kutu']};overflow:hidden;border:0.35pt solid {C['cizgi']}}}
.sol{{left:16pt;top:46pt;width:156pt;color:{C['metin']};font-size:6.6pt;line-height:1.5}}
.sol .sh{{color:{C['turuncu']};font-weight:700;font-size:6pt;margin-bottom:6pt}}
.sol p{{margin-bottom:2.6pt}}
.ans{{left:428pt;top:40pt;width:96pt;border:0.6pt solid #C7CFDB;padding:5pt 7pt}}
.al{{font-size:4.6pt;color:{C['gri']};letter-spacing:.3pt}}
.av{{font:20pt/1.1 AB;color:{C['turuncu']};margin-top:3pt}}
.ak{{font-size:4.4pt;color:{C['gri']};margin-top:2pt}}
'''
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(page(q) for q in qs)}</body></html>'
    pathlib.Path(out).write_text(html)
if __name__=="__main__":
    build(json.load(open(sys.argv[1])),sys.argv[2])
