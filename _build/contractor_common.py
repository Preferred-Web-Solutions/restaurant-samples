"""Shared page generators for the contractor samples (service pages, area map, job cards)."""
from common import *

def crumbs(items):
    li = ''.join(f'<li>{"<a href=%s>%s</a>" % (chr(34)+h+chr(34), l) if h else "<span aria-current=%spage%s>%s</span>" % (chr(34), chr(34), l)}</li>' for l, h in items)
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{li}</ol></nav>'

def service_page(cfg, svc, services, art, cta_label, cta_href):
    """svc: dict(slug,name,intro,includes[],good[],job=(title,desc),related[slugs],kicker)"""
    by = {s['slug']: s for s in services}
    inc = ''.join(f'<li>{x}</li>' for x in svc['includes'])
    good = ''.join(f'<li>{x}</li>' for x in svc['good'])
    rel = ''.join(f'<li><a href="svc-{r}.html">{esc(by[r]["name"])}</a><span>{esc(by[r]["short"])}</span></li>' for r in svc['related'])
    jt, jd = svc['job']
    return f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('Services','services.html'),(svc['name'],None)])}
 <div class="svc-head-grid"><div><p class="eyebrow">{esc(svc['kicker'])}</p><h1>{esc(svc['name'])}</h1><p class="lede">{svc['intro']}</p>
 <div class="btn-row"><a class="btn" href="{cta_href}">{esc(cta_label)}</a><a class="btn btn--ghost" href="tel:{cfg['tel']}">Call {esc(cfg['phone'])}</a></div></div>
 <figure class="svc-art" style="margin:0">{art(svc['art'])}<figcaption>Illustration. A photo of one of your own jobs goes here.</figcaption></figure></div></div></section>
<section class="sec" aria-labelledby="inc-h"><div class="wrap svc-body">
 <div><h2 id="inc-h">What is included</h2><ul class="ticks">{inc}</ul>
 <h2 style="margin-top:2.4rem">A recent job</h2>
 <div class="job"><div class="job-art">{art(svc['art'])}</div><div><span class="tag">Sample job card</span><h3>{esc(jt)}</h3><p>{jd}</p><p class="invented">Invented for the sample. Real jobs, photos and before/after pairs come from the owner.</p></div></div></div>
 <aside class="goodbox" aria-labelledby="gd-h"><h2 id="gd-h">Good to know</h2><ul class="ticks">{good}</ul><a class="btn" href="{cta_href}">{esc(cta_label)}</a></aside>
</div></section>
<section class="sec sec--soft" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h" style="margin-bottom:1.2rem">Related services</h2><ul class="related">{rel}</ul></div></section>
"""

def services_overview(cfg, groups, services, art, cta_label, cta_href):
    by = {s['slug']: s for s in services}
    out = ''
    for title, slugs in groups:
        rows = ''.join(f'<li class="svc-row"><div class="svc-row-art">{art(by[s]["art"])}</div><div><h3><a href="svc-{s}.html">{esc(by[s]["name"])}</a></h3><p>{by[s]["short"]}</p><a class="link-arrow" href="svc-{s}.html">Read about {esc(by[s]["name"].lower())}<span aria-hidden="true"> &rarr;</span></a></div></li>' for s in slugs)
        out += f'<div class="svc-group"><h2>{esc(title)}</h2><ul class="svc-rows">{rows}</ul></div>'
    return f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('Services',None)])}<p class="eyebrow">What we do</p><h1>Services</h1>
 <p class="lede">{cfg['services_lede']}</p><div class="btn-row"><a class="btn" href="{cta_href}">{esc(cta_label)}</a></div></div></section>
<section class="sec"><div class="wrap">{out}</div></section>
"""

def area_map(towns, label, fill, stroke, text, bg):
    """Schematic (not geographic) map: towns around a center, area shaded. towns: [(name,x,y)] in 0..600 x 0..380"""
    dots = ''.join(f'<g><circle cx="{x}" cy="{y}" r="6" fill="{stroke}"/><text x="{x+11}" y="{y+5}" font-family="sans-serif" font-size="14" font-weight="700" fill="{text}">{esc(n)}</text></g>' for n, x, y in towns)
    return (f'<svg class="area-map" viewBox="0 0 600 380" role="img" aria-label="{esc(label)}"><rect width="600" height="380" fill="{bg}"/>'
            f'<path d="M70 210 C60 120 160 50 290 56 C420 50 540 110 530 210 C536 300 430 346 300 336 C170 340 78 300 70 210Z" fill="{fill}" fill-opacity=".28" stroke="{stroke}" stroke-width="3" stroke-dasharray="10 7"/>'
            f'<path d="M20 240 C150 200 260 260 580 150" fill="none" stroke="{stroke}" stroke-opacity=".5" stroke-width="10"/>'
            f'<path d="M300 20 C310 120 280 250 320 370" fill="none" stroke="{stroke}" stroke-opacity=".5" stroke-width="10"/>{dots}</svg>')

def area_page(cfg, towns_map, towns_all, map_label, map_fn, cta_label, cta_href, intro, extra_towns_note):
    ls = ''.join(f'<li>{esc(t)}</li>' for t in towns_all[:10])
    rest = ''.join(f'<li>{esc(t)}</li>' for t in towns_all[10:])
    return f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('Service area',None)])}<p class="eyebrow">Where we work</p><h1>Service area</h1><p class="lede">{intro}</p></div></section>
<section class="sec"><div class="wrap two">
 <div>{map_fn(towns_map, map_label)}<p class="hint" style="margin-top:.6rem">Illustration of the area we serve. Not to scale and not a survey. A real site can use a proper map of the owner&rsquo;s area.</p></div>
 <div><h2 style="font-size:1.8rem;margin-bottom:.8rem">Towns we serve</h2><ul class="towns">{ls}</ul>
 <details class="more"><summary>See all towns</summary><ul class="towns">{rest}</ul></details>
 <p style="margin-top:1.2rem">{extra_towns_note}</p><p><a class="btn" href="{cta_href}">{esc(cta_label)}</a></p></div></div></section>
"""
