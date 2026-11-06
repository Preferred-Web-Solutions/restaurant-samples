import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from contractor_common import *

CTA = 'Get a free roof inspection'
CTA_HREF = 'contact.html#inspection'

SERVICES = [
 dict(slug='roof-replacement', name='Roof replacement', short='A full tear-off and new roof, with a written price before we start.', kicker='Roofing', art='replace',
  intro='When repairs stop making sense, we strip the roof to the deck, fix what is underneath, and install a new roof with a written price and schedule agreed first.',
  includes=['Free inspection and a written quote', 'Full tear-off and deck check, with any rotted boards replaced and priced before we do it', 'Underlayment, flashing, vents and ridge cap', 'Shingle choice shown in person, with samples', 'Daily cleanup and a magnet sweep for nails', 'Final walk-through before you pay the last invoice'],
  good=['Most replacements take one to two days, weather allowing.', 'You get the quote in writing, with materials and the warranty named.', 'Sample warranty: 5 years on our workmanship. Manufacturer warranties vary.'],
  job=('Gable roof, 28 squares', 'Tear-off, two sheets of deck replaced, new architectural shingles in charcoal, new pipe flashings. Finished in two days.'), related=['roof-repair', 'metal-roofing', 'storm-damage']),
 dict(slug='roof-repair', name='Roof repair', short='Leaks, missing shingles and flashing, fixed and sealed.', kicker='Roofing', art='repair',
  intro='A small problem does not need a new roof. We find where the water is getting in, fix that, and tell you plainly if the roof has more life in it.',
  includes=['Leak tracing from the attic and the roof', 'Missing or lifted shingle replacement', 'Flashing and pipe boot repair', 'Sealing around chimneys, vents and skylights', 'Photos of the problem and the fix', 'A plain answer on repair versus replace'],
  good=['Call early. A small leak is a cheap fix and a big one is not.', 'We quote repairs in writing before we start.', 'If a repair will not hold, we say so.'],
  job=('Chimney flashing leak', 'Water stains traced to failed step flashing. Replaced the flashing and resealed the counter-flashing. The ceiling stain stopped growing.'), related=['roof-replacement', 'gutters-downspouts', 'storm-damage']),
 dict(slug='metal-roofing', name='Metal roofing', short='Standing-seam and metal shingle roofs that last decades.', kicker='Roofing', art='metal',
  intro='Metal costs more up front and lasts longer. We install standing-seam panels and will tell you honestly whether it makes sense for your house.',
  includes=['On-site measuring and a written quote', 'Panel and color samples', 'Underlayment and ice-and-water protection at valleys and eaves', 'Trim, flashing and snow guards where needed', 'Cleanup and a final walk-through'],
  good=['Metal is loud in heavy rain only if the deck is bare. We insulate under it.', 'Color choices are limited by what is in stock. Ask for samples.', 'It is usually installed over a clean, sound deck, so some prep work is common.'],
  job=('Standing-seam on a ranch', 'Charcoal standing-seam panels with matching trim. Four days including prep and snow guards on the north slope.'), related=['roof-replacement', 'flat-roofs', 'gutters-downspouts']),
 dict(slug='storm-damage', name='Storm damage', short='Tarping, inspections and repairs after wind and hail.', kicker='Storm and exterior', art='storm',
  intro='After a storm, the first job is keeping water out. We tarp fast, document the damage with photos, and then repair or replace what the storm took.',
  includes=['Emergency tarping to stop leaks', 'Photo documentation you can give your insurer', 'Inspection of shingles, flashing, vents and gutters', 'A written scope of repair or replacement', 'Permanent repairs once the weather clears'],
  good=['Take your own photos first if it is safe. Do not climb on a wet roof.', 'We can meet your adjuster at the house if you ask.', 'Your insurance decisions are yours. We give you the facts and a clear quote.'],
  job=('Hail and wind, two slopes', 'Tarped the same afternoon. Replaced the two damaged slopes and a ridge vent after the claim was approved.'), related=['roof-repair', 'roof-replacement', 'gutters-downspouts']),
 dict(slug='gutters-downspouts', name='Gutters and downspouts', short='New gutters, repairs and downspouts that move water away.', kicker='Storm and exterior', art='gutter',
  intro='Gutters protect your roof edge, siding and foundation. We install seamless gutters, fix sagging runs, and point downspouts where the water should go.',
  includes=['Seamless aluminum gutters cut to length on site', 'Repairs to sagging, leaking or pulled-away runs', 'Downspout extensions and splash blocks', 'Gutter guards where they make sense', 'Cleanup of old gutters and debris'],
  good=['Gutters that overflow are often undersized or clogged, not broken.', 'We match colors from what is in stock.', 'We check the fascia board behind old gutters and tell you if it is rotted.'],
  job=('Back-of-house gutter run', 'Replaced 60 feet of sagging gutter and added two downspout extensions to carry water off the patio.'), related=['roof-repair', 'storm-damage', 'roof-replacement']),
 dict(slug='flat-roofs', name='Flat and low-slope roofs', short='Membrane roofs for porches, additions and small commercial buildings.', kicker='Storm and exterior', art='flat',
  intro='Flat roofs need different materials and careful seams. We repair and replace low-slope roofs on porches, additions and small commercial buildings.',
  includes=['Inspection of seams, drains and flashing', 'Membrane repair or full replacement', 'Drainage fixes so water does not pool', 'Edge metal and flashing', 'A written quote with the material named'],
  good=['Ponding water shortens a flat roof&rsquo;s life, so drainage matters as much as the membrane.', 'Small commercial work is quoted the same way: in writing, before we start.', 'Ask about repair first. Many flat roofs only need seams redone.'],
  job=('Rear addition, 400 sq ft', 'Replaced a worn rubber membrane, added a tapered edge so water drains, and resealed the wall flashing.'), related=['metal-roofing', 'roof-repair', 'gutters-downspouts']),
]
GROUPS = [('Roofing', ['roof-replacement', 'roof-repair', 'metal-roofing']), ('Storm and exterior', ['storm-damage', 'gutters-downspouts', 'flat-roofs'])]
TOWNS_ALL = ['Blue Ash', 'Mason', 'Loveland', 'Anderson Township', 'Colerain Township', 'Forest Park', 'Springdale', 'Fairfield', 'Montgomery', 'Norwood', 'Sharonville', 'Symmes Township', 'Delhi Township', 'Western Hills', 'Oakley', 'Madeira']

CFG = dict(
    slug='tallow-ridge-roofing', name='Tallow Ridge Roofing', tagline='Roof replacement, repair and storm damage in the Cincinnati area.',
    kind_word='roofing website', fictional_word='roofing company',
    logo_html='<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><path d="M3 18 17 5l14 13" fill="none" stroke="#F26B1D" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/><path d="M8 19v11h18V19" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/></svg><span>Tallow Ridge <b>Roofing</b></span>',
    phone='(513) 555-0119', tel='+15135550119', addr1='Office: 3110 Ridgeline Road', addr2='Cincinnati, Ohio 45236',
    foot_loc_title='Office', foot_hours_title='Office hours',
    hours_short=[('Monday to Friday', '7am to 5pm'), ('Saturday', '8am to noon'), ('Storm calls', 'Phone answered after hours')],
    cta=CTA, cta_href=CTA_HREF, menu_label='Menu',
    nav=[('home', 'Home', 'index.html'), ('services', 'Services', None), ('area', 'Service area', 'area.html'), ('about', 'About', 'about.html'), ('contact', 'Contact', 'contact.html')],
    services_menu=dict(groups=[(t, [(next(s['name'] for s in SERVICES if s['slug'] == sl), f'svc-{sl}.html') for sl in sls]) for t, sls in GROUPS], all=('All services', 'services.html')),
    social=['Facebook'],
    fonts=[('Barlow Condensed', 700, 'barlow-condensed-latin-700-normal.woff2'), ('Barlow Condensed', 800, 'barlow-condensed-latin-800-normal.woff2'), ('Source Sans 3', 400, 'source-sans-3-latin-400-normal.woff2'), ('Source Sans 3', 600, 'source-sans-3-latin-600-normal.woff2'), ('Source Sans 3', 700, 'source-sans-3-latin-700-normal.woff2')],
    preload=['barlow-condensed-latin-800-normal.woff2', 'source-sans-3-latin-400-normal.woff2'],
    services_lede='Six services, each with its own page. Every job starts with a free inspection and a written quote.',
    credit=f'Sample website designed by Preferred Web Solutions &middot; <a href="mailto:{EMAIL}">{EMAIL}</a>. Tallow Ridge Roofing is a made-up business used to show what a roofing website can look like. Services, claims, address, phone number and story are invented. Illustrations are original artwork standing in for job photos. A real site shows only license numbers, warranties and years in business the owner confirms.',
    invented_list='services, claims, address, phone number and story',
    cannot_do='You cannot request a quote, book an inspection or buy anything here.',
    photo_terms='Illustrations are original artwork used for demonstration only.',
    a11y_text='Service details and contact information are real text, not pictures or PDFs.',
    a11y_img='Illustrations that carry meaning have text descriptions, and decorative ones are hidden from screen readers.',
    bar_tail='Illustrations stand in for job photos.',
)

CSS = r"""
:root{--bg:#EEF1F2;--surface:#FFFFFF;--soft:#E1E6E9;--ink:#14181B;--muted:#46535C;--line:#C4CCD2;--slate:#2A3640;--orange:#F26B1D;--focus:#0B5FD0;
--display:"Barlow Condensed","Arial Narrow",Impact,sans-serif;--body:"Source Sans 3","Segoe UI",system-ui,sans-serif;--radius:4px;--banner-bg:#F26B1D;--banner-ink:#14181B;
--btn-bg:#F26B1D;--btn-ink:#14181B;--head-bg:#14181B;--head-ink:#fff;--head-line:rgba(255,255,255,.2);--foot-bg:#14181B;--foot-ink:#fff;--hd-h:76px}
.site-header :focus-visible,.site-footer :focus-visible,.dark :focus-visible,.callbar :focus-visible{outline-color:#FFB27A}
.site-header .dd-menu{color:var(--ink)}
.site-header .dd-menu :focus-visible{outline-color:var(--focus)}
h1,h2,h3{font-family:var(--display);font-weight:800;text-transform:uppercase;letter-spacing:.01em;line-height:1}
.logo{font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.04em;font-size:1.5rem;color:#fff}
.logo b{color:#F26B1D;font-weight:800}
.btn{font-family:var(--display);font-weight:800;text-transform:uppercase;letter-spacing:.06em;font-size:1.12rem;border-radius:4px}
.btn--ghost{color:inherit}
.eyebrow{font-family:var(--display);font-weight:700;text-transform:uppercase;letter-spacing:.14em;font-size:1rem;color:#8F3200;margin:0 0 .7rem}
.dark .eyebrow,.hero .eyebrow,.svc-head .eyebrow{color:#FFB27A}
.svc-head .eyebrow{color:#8F3200}
.lede{font-size:clamp(1.12rem,1.8vw,1.3rem);max-width:36rem}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.5rem}
.dark{background:var(--slate);color:#fff}
.sec--soft{background:var(--soft)}
/* hero */
.hero{background:var(--slate);color:#fff;padding-top:clamp(2.2rem,5vw,4.2rem);padding-bottom:clamp(2.6rem,6vw,5rem)}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(1.5rem,5vw,4.5rem);align-items:center}
.hero h1{font-size:clamp(3rem,8vw,6rem);margin-bottom:1rem}
.hero h1 span{color:#F26B1D}
.hero .btn--ghost{border-color:#fff}
.clip{position:relative;background:#fff;color:var(--ink);border-radius:6px;padding:2.4rem 1.4rem 1.4rem;box-shadow:0 18px 40px rgba(0,0,0,.35);transform:rotate(1.5deg)}
.clip::before{content:"";position:absolute;top:-14px;left:50%;width:7.5rem;height:2.1rem;margin-left:-3.75rem;border-radius:6px;background:#7A858C;box-shadow:inset 0 -5px 0 rgba(0,0,0,.18)}
.clip::after{content:"";position:absolute;top:-6px;left:50%;width:2.6rem;height:.8rem;margin-left:-1.3rem;border-radius:4px;background:#D3D9DD}
.clip h2{font-size:1.5rem;margin-bottom:.2rem}
.clip .sub{font-size:.9rem;color:var(--muted);margin:0 0 .8rem}
.clip ul{list-style:none;display:grid;gap:.1rem}
.clip li{display:flex;align-items:center;gap:.7rem;min-height:2.3rem;border-bottom:1px solid var(--line);font-weight:600}
.clip li::before{content:"";flex:0 0 1.15rem;height:1.15rem;border:2px solid var(--ink);border-radius:3px;background:#fff center/80% no-repeat}
.clip li.on::before{background-color:#F26B1D;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cpath d='M4 10.5l4 4 8-9' fill='none' stroke='%2314181B' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")}
.clip .sig{margin-top:.9rem;font-size:.85rem;color:var(--muted)}
@media (max-width:900px){.hero-grid{grid-template-columns:minmax(0,1fr)}.clip{transform:none;margin-top:1rem}.hero h1{font-size:clamp(2.8rem,14vw,4.4rem)}}
/* trust */
.trust{background:#fff;border-bottom:1px solid var(--line)}
.trust ul{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem 2rem;list-style:none;padding:1.4rem 0 .4rem}
.trust li{display:flex;flex-direction:column;font-size:.98rem}
.trust b{font-family:var(--display);text-transform:uppercase;letter-spacing:.04em;font-size:1.3rem;font-weight:800}
.trust small{display:block;color:var(--muted);padding-bottom:1rem}
@media (max-width:760px){.trust ul{grid-template-columns:repeat(2,minmax(0,1fr))}}
/* cards */
.sec-head{max-width:44rem;margin-bottom:2rem}
.sec-head h2,.h2{font-size:clamp(2.2rem,5vw,3.6rem)}
.svc-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(16rem,1fr));gap:1.2rem;list-style:none}
.svc-card{background:#fff;border:2px solid var(--ink);border-radius:var(--radius);display:flex;flex-direction:column}
.svc-card .art{border-bottom:2px solid var(--ink)}
.svc-card .art svg,.job-art svg,.svc-row-art svg,.svc-art svg{display:block;width:100%;height:auto}
.svc-card .tx{padding:1rem 1.1rem 1.2rem;display:flex;flex-direction:column;gap:.4rem;flex:1}
.svc-card h3{font-size:1.7rem}
.svc-card p{margin:0;color:var(--muted)}
.svc-card .link-arrow{margin-top:auto}
/* process */
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1.2rem;list-style:none;counter-reset:s}
.steps li{counter-increment:s;border-top:4px solid #F26B1D;padding-top:1rem}
.steps li::before{content:counter(s);display:block;font-family:var(--display);font-weight:800;font-size:3rem;line-height:1;color:#F26B1D}
.steps h3{font-size:1.5rem;margin:.3rem 0}
.steps p{margin:0;color:#D6DDE2}
@media (max-width:860px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.steps{grid-template-columns:minmax(0,1fr)}}
/* jobs */
.jobs{display:grid;grid-template-columns:repeat(auto-fit,minmax(17rem,1fr));gap:1.2rem;list-style:none}
.jobc{background:#fff;border:2px solid var(--ink);border-radius:var(--radius);overflow:hidden}
.jobc .tx{padding:1rem 1.1rem 1.2rem}
.jobc h3{font-size:1.5rem;margin:.3rem 0}
.tag{display:inline-block;font-family:var(--display);font-weight:700;letter-spacing:.1em;text-transform:uppercase;font-size:.85rem;padding:.1rem .5rem;border:2px solid var(--ink);border-radius:3px;background:#FFE3D0}
.invented{font-size:.9rem;color:var(--muted);font-style:italic}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:start}
@media (max-width:860px){.two{grid-template-columns:minmax(0,1fr)}}
.panel{background:#fff;border:2px solid var(--ink);border-radius:var(--radius);padding:clamp(1.2rem,3vw,2rem)}
.panel h2{font-size:clamp(1.9rem,3.5vw,2.6rem);margin-bottom:.6rem}
.towns{list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 1.5rem;margin-bottom:.8rem}
.towns li{padding:.45rem 0;border-bottom:1px solid var(--line)}
details.more summary{cursor:pointer;min-height:44px;display:flex;align-items:center;font-weight:700}
.band{background:#F26B1D;color:var(--ink)}
.band .wrap{display:flex;flex-wrap:wrap;gap:1.2rem 2rem;align-items:center;justify-content:space-between}
.band h2{font-size:clamp(2.2rem,5vw,3.8rem);max-width:16ch}
.band .btn{--btn-bg:#14181B;--btn-ink:#fff;border-color:#14181B}
/* inner pages */
.svc-head{background:var(--soft);border-bottom:2px solid var(--ink);padding-top:clamp(1.2rem,3vw,2rem);padding-bottom:clamp(2rem,4vw,3rem)}
.svc-head h1{font-size:clamp(2.8rem,7vw,5rem);margin-bottom:.8rem}
.svc-head .lede{margin:0}
.svc-head-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:center}
@media (max-width:860px){.svc-head-grid{grid-template-columns:minmax(0,1fr)}}
.svc-art{border:2px solid var(--ink);background:#fff;border-radius:var(--radius);overflow:hidden}
.svc-art figcaption{padding:.5rem .8rem;font-size:.88rem;color:var(--muted);border-top:2px solid var(--ink)}
.crumbs{color:var(--muted)}
.svc-body{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:start}
@media (max-width:860px){.svc-body{grid-template-columns:minmax(0,1fr)}}
.svc-body h2{font-size:clamp(1.8rem,3.5vw,2.4rem);margin-bottom:.8rem}
.ticks{list-style:none;display:grid;gap:.6rem}
.ticks li{position:relative;padding-left:1.9rem}
.ticks li::before{content:"";position:absolute;left:0;top:.35rem;width:1.1rem;height:1.1rem;border-radius:3px;background:#F26B1D center/80% no-repeat;border:2px solid var(--ink)}
.job{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:1.2rem;align-items:start;background:#fff;border:2px solid var(--ink);border-radius:var(--radius);padding:1rem}
.job-art{border:2px solid var(--ink);border-radius:3px;overflow:hidden}
.job h3{font-size:1.5rem;margin:.4rem 0}
@media (max-width:640px){.job{grid-template-columns:minmax(0,1fr)}}
.goodbox{background:#fff;border:2px solid var(--ink);border-left:10px solid #F26B1D;border-radius:var(--radius);padding:1.3rem;display:grid;gap:1rem;position:sticky;top:calc(var(--sb-h) + var(--hd-h) + 16px)}
.goodbox h2{margin:0}
@media (max-width:860px){.goodbox{position:static}}
.related{list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1rem}
.related li{background:#fff;border:2px solid var(--ink);border-radius:var(--radius);padding:1rem;display:flex;flex-direction:column;gap:.3rem}
.related a{font-family:var(--display);font-weight:800;text-transform:uppercase;font-size:1.5rem;display:inline-flex;align-items:center;min-height:44px}
.related span{color:var(--muted)}
.svc-group+.svc-group{margin-top:3.5rem}
.svc-group h2{font-size:clamp(2rem,4vw,3rem);margin-bottom:1.2rem;border-bottom:4px solid #F26B1D;display:inline-block;padding-bottom:.2rem}
.svc-rows{list-style:none;display:grid;gap:1.2rem}
.svc-row{display:grid;grid-template-columns:minmax(0,.55fr) minmax(0,1.45fr);gap:1.4rem;align-items:center;background:#fff;border:2px solid var(--ink);border-radius:var(--radius);padding:1rem}
.svc-row h3{font-size:1.9rem}
.svc-row h3 a{text-decoration:none}
.svc-row p{margin:.3rem 0 .4rem;color:var(--muted)}
.svc-row-art{border:2px solid var(--ink);border-radius:3px;overflow:hidden}
@media (max-width:640px){.svc-row{grid-template-columns:minmax(0,1fr)}}
.area-map{width:100%;height:auto;border:2px solid var(--ink);border-radius:var(--radius)}
.hint{font-size:.9rem;color:var(--muted)}
.hours{width:100%;border-collapse:collapse;margin:.6rem 0 1rem}
.hours th,.hours td{text-align:left;padding:.55rem 0;border-bottom:1px solid var(--line);font-weight:400}
.hours td{text-align:right;font-weight:700}
blockquote{margin:1.4rem 0;padding:0 0 0 1.2rem;border-left:8px solid #F26B1D;font-size:1.3rem;font-weight:600;line-height:1.35}
blockquote cite{display:block;font-size:.95rem;font-style:normal;margin-top:.4rem}
.field input,.field select,.field textarea{border-radius:3px}
"""

def art(kind):
    sky = '#DCE6EC'; wall = '#fff'; ink = '#14181B'; o = '#F26B1D'; sl = '#2A3640'
    base = f'<svg viewBox="0 0 320 200" role="img" aria-label="{{}}"><rect width="320" height="200" fill="{sky}"/><rect y="168" width="320" height="32" fill="#B8C4CB"/>'
    house = f'<rect x="70" y="100" width="180" height="70" fill="{wall}" stroke="{ink}" stroke-width="4"/><rect x="95" y="122" width="26" height="26" fill="{sky}" stroke="{ink}" stroke-width="3"/><rect x="199" y="122" width="26" height="26" fill="{sky}" stroke="{ink}" stroke-width="3"/><rect x="146" y="124" width="28" height="46" fill="{o}" stroke="{ink}" stroke-width="3"/>'
    gable = f'<polygon points="54,104 160,34 266,104" fill="{sl}" stroke="{ink}" stroke-width="4" stroke-linejoin="round"/>'
    if kind == 'replace':
        rows = ''.join(f'<path d="M{70+r*6} {92-r*9}H{250-r*6}" stroke="#4C5C69" stroke-width="3"/>' for r in range(0, 6))
        return (base + house + gable + rows + f'<path d="M120 62H200" stroke="{o}" stroke-width="5"/><text x="160" y="196" text-anchor="middle" font-family="sans-serif" font-size="11" fill="{ink}"></text></svg>').format('Illustration of a house with a new shingle roof')
    if kind == 'repair':
        patch = f'<rect x="132" y="64" width="40" height="26" fill="{o}" stroke="{ink}" stroke-width="3" transform="rotate(-8 152 77)"/><path d="M142 78l8 8 14-16" fill="none" stroke="{ink}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>'
        return (base + house + gable + patch + '</svg>').format('Illustration of a house roof with one repaired patch marked in orange')
    if kind == 'metal':
        panels = ''.join(f'<path d="M{80+i*14} {99-abs(i-7)*0}L{80+i*14+0} 100" stroke="#7C8D99" stroke-width="2"/>' for i in range(0)) + ''.join(f'<path d="M{108+i*13} 100L{160+(108+i*13-160)*0.38} 44" stroke="#9DB0BD" stroke-width="3"/>' for i in range(-3, 12))
        return (base + house + f'<polygon points="54,104 160,34 266,104" fill="#44525C" stroke="{ink}" stroke-width="4" stroke-linejoin="round"/>' + ''.join(f'<path d="M{x} 104L{160+(x-160)*0.42} 40" stroke="#B9C7D0" stroke-width="3"/>' for x in range(70, 260, 18)) + '</svg>').format('Illustration of a house with a standing-seam metal roof')
    if kind == 'storm':
        cloud = '<g fill="#8FA0AC" stroke="#14181B" stroke-width="3"><ellipse cx="90" cy="30" rx="44" ry="18"/><ellipse cx="150" cy="24" rx="40" ry="18"/><ellipse cx="220" cy="32" rx="46" ry="18"/></g>'
        rain = ''.join(f'<path d="M{x} {52+ (x%3)*4}l-6 16" stroke="#3E6E94" stroke-width="3" stroke-linecap="round"/>' for x in range(60, 270, 22))
        tarp = f'<polygon points="118,84 160,52 214,92 170,98" fill="{o}" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>'
        return (base + house + gable + tarp + cloud + rain + '</svg>').format('Illustration of a house under a storm cloud with an orange tarp over one damaged section of roof')
    if kind == 'gutter':
        return (base + house + gable + f'<rect x="60" y="102" width="200" height="8" rx="3" fill="#B9C7D0" stroke="{ink}" stroke-width="3"/><rect x="250" y="102" width="8" height="66" fill="#B9C7D0" stroke="{ink}" stroke-width="3"/><path d="M254 168q0 14 -20 14" fill="none" stroke="{o}" stroke-width="5" stroke-linecap="round"/></svg>').format('Illustration of a roof edge with a gutter and downspout carrying water away from the house')
    if kind == 'flat':
        return (base + f'<rect x="60" y="94" width="200" height="76" fill="{wall}" stroke="{ink}" stroke-width="4"/><rect x="52" y="82" width="216" height="14" fill="{sl}" stroke="{ink}" stroke-width="4"/><rect x="104" y="122" width="26" height="26" fill="{sky}" stroke="{ink}" stroke-width="3"/><rect x="190" y="122" width="26" height="26" fill="{sky}" stroke="{ink}" stroke-width="3"/><path d="M80 70h40m10 0h50" stroke="{o}" stroke-width="5" stroke-linecap="round"/><circle cx="236" cy="68" r="9" fill="#B9C7D0" stroke="{ink}" stroke-width="3"/></svg>').format('Illustration of a flat-roofed building with a drain')
    return base + '</svg>'

def pages():
    c = CFG; P = {}
    cards = ''.join(
        f'<li class="svc-card"><div class="art">{art(s["art"])}</div><div class="tx"><h3>{esc(s["name"])}</h3><p>{s["short"]}</p><a class="link-arrow" href="svc-{s["slug"]}.html">Read about {esc(s["name"].lower())}<span aria-hidden="true"> &rarr;</span></a></div></li>'
        for s in SERVICES if s['slug'] in ('roof-replacement', 'roof-repair', 'storm-damage'))
    jobs = ''.join(f'<li class="jobc"><div>{art(s["art"])}</div><div class="tx"><span class="tag">Sample job card</span><h3>{esc(s["job"][0])}</h3><p>{s["job"][1]}</p></div></li>' for s in SERVICES if s['slug'] in ('roof-replacement', 'metal-roofing', 'storm-damage'))
    home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div><p class="eyebrow">Family-owned roofing &middot; Cincinnati area</p>
 <h1>Straight answers about <span>your roof.</span></h1>
 <p class="lede">A free inspection, a written quote you can read, and a crew that cleans up every day. Roof replacement, repair and storm damage.</p>
 <div class="btn-row"><a class="btn" href="{CTA_HREF}">{CTA}</a><a class="btn btn--ghost" href="tel:{c['tel']}">Call {c['phone']}</a></div></div>
 <div class="clip" role="group" aria-label="Sample inspection checklist"><h2>Roof inspection</h2><p class="sub">What we check, and what you get in writing.</p>
 <ul><li class="on">Shingles: cracks, curling, missing</li><li class="on">Flashing at chimneys and walls</li><li class="on">Pipe boots and roof vents</li><li class="on">Valleys and ridge</li><li class="on">Gutters and fascia</li><li>Attic: moisture and decking</li></ul>
 <p class="sig">Photos and a written summary, same day. Free.</p></div>
</div></section>
<div class="trust"><div class="wrap"><ul>
 <li><b>Free written estimates</b>Price in writing before work starts.</li><li><b>Licensed &amp; insured*</b>License number shown once the owner provides it.</li>
 <li><b>5-year workmanship warranty*</b>On our installation work.</li><li><b>Daily cleanup</b>Magnet sweep for nails, every day.</li></ul>
 <small>*Sample claims for a fictional company. A real site shows only what the owner confirms.</small></div></div>
<section class="sec" aria-labelledby="sv-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Services</p><h2 id="sv-h">What we fix and replace.</h2></div>
 <ul class="svc-cards">{cards}</ul><p style="margin-top:1.6rem"><a class="link-arrow" href="services.html">See all six services &rarr;</a></p></div></section>
<section class="sec dark" aria-labelledby="pr-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">How a job goes</p><h2 id="pr-h">Four steps, no surprises.</h2></div>
 <ol class="steps"><li><h3>Inspect</h3><p>We look at the roof and attic and take photos. It is free.</p></li><li><h3>Quote</h3><p>You get a written quote with materials and the warranty named.</p></li><li><h3>Install</h3><p>A crew arrives on the day we said, and cleans up every evening.</p></li><li><h3>Walk through</h3><p>We go over the finished roof with you before you pay the last invoice.</p></li></ol></div></section>
<section class="sec" aria-labelledby="jb-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Recent work</p><h2 id="jb-h">Jobs from the last few months.</h2><p class="invented">Sample job cards with illustrations. Real photos and before/after pairs from the owner go here.</p></div><ul class="jobs">{jobs}</ul></div></section>
<section class="sec sec--soft"><div class="wrap two"><div class="panel"><p class="eyebrow">Where we work</p><h2>Cincinnati and the towns around it.</h2><p>Blue Ash, Mason, Loveland, Anderson, Colerain and more. If you are not sure we cover you, ask.</p><a class="link-arrow" href="area.html">See the service area &rarr;</a></div>
 <div class="panel"><p class="eyebrow">Reviews</p><h2>Your neighbors, in their words.</h2><p>A real site links to the company&rsquo;s own Google and Facebook reviews and shows its actual rating. We never write reviews or copy them from other sites.</p><a class="btn btn--ghost btn--sm" style="color:var(--ink)" href="#" data-demo="Reviews link is a demo on this sample.">Read reviews on Google (demo)</a></div></div></section>
<section class="sec band" aria-labelledby="cb-h"><div class="wrap"><h2 id="cb-h">Not sure what your roof needs?</h2><a class="btn" href="{CTA_HREF}">{CTA}</a></div></section>
"""
    P['home'] = ('index.html', 'Tallow Ridge Roofing | Roof replacement and repair in Cincinnati (sample)',
                 'Tallow Ridge Roofing is a fictional Cincinnati-area roofer: free inspections, written quotes, roof replacement, repair and storm damage. A design sample by Preferred Web Solutions.', home, 'home', '')
    P['services'] = ('services.html', 'Roofing services | Tallow Ridge Roofing, Cincinnati (sample)',
                     'Roof replacement, roof repair, metal roofing, storm damage, gutters and flat roofs from Tallow Ridge Roofing, a fictional Cincinnati roofer.',
                     services_overview(c, GROUPS, SERVICES, art, CTA, CTA_HREF), 'services', '')
    for s in SERVICES:
        P['svc-' + s['slug']] = (f'svc-{s["slug"]}.html', f'{s["name"]} in Cincinnati | Tallow Ridge Roofing (sample)',
                                 f'{s["name"]} from Tallow Ridge Roofing, a fictional Cincinnati-area roofer. {s["short"]} A design sample by Preferred Web Solutions.',
                                 service_page(c, s, SERVICES, art, CTA, CTA_HREF), 'svc-' + s['slug'], '')
    tm = [('Mason', 380, 70), ('Loveland', 480, 120), ('Blue Ash', 360, 150), ('Anderson', 470, 230), ('Cincinnati', 300, 250), ('Colerain', 150, 190), ('Fairfield', 190, 90), ('Springdale', 250, 140)]
    P['area'] = ('area.html', 'Service area | Tallow Ridge Roofing, Cincinnati (sample)',
                 'The Cincinnati-area towns served by Tallow Ridge Roofing, a fictional roofer. A design sample by Preferred Web Solutions.',
                 area_page(c, tm, TOWNS_ALL, 'Schematic map of the Cincinnati area showing the towns served, with the service area shaded', lambda t, l: area_map(t, l, '#F26B1D', '#14181B', '#14181B', '#EEF1F2'), CTA, CTA_HREF,
                           'We roof homes and small buildings in Cincinnati and the towns around it. Not on the list? Ask. We will tell you straight whether we can get there.', 'Service area and towns are sample details. A real site lists the towns the owner confirms.'), 'area', '')
    about = f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('About',None)])}<p class="eyebrow">About us</p><h1>A small crew that answers its phone.</h1></div></section>
<section class="sec"><div class="wrap two">
 <div><h2 style="font-size:clamp(2rem,4vw,3rem);margin-bottom:1rem">Why we started.</h2><p class="lede">Dale Harlan roofed for other companies for twelve years before starting Tallow Ridge. He wanted to give homeowners what he never saw enough of: a straight answer, a written price, and a crew that shows up when it said it would.</p>
 <blockquote>&ldquo;If the roof does not need replacing, we will tell you that and fix what is wrong.&rdquo;<cite>Dale Harlan, owner</cite></blockquote>
 <p class="invented">The owner, story and quote are invented for this sample. On a real site, they come from the owner.</p></div>
 <div class="panel"><h2>How we work</h2><ul class="ticks"><li>Free inspection with photos.</li><li>A written quote before any work starts.</li><li>The same crew from start to finish.</li><li>Cleanup every day, with a magnet sweep for nails.</li><li>A final walk-through before the last invoice.</li></ul>
 <p style="margin-top:1.2rem"><a class="btn" href="{CTA_HREF}">{CTA}</a></p></div></div></section>
"""
    P['about'] = ('about.html', 'About | Tallow Ridge Roofing, Cincinnati (sample)',
                  'The owner and the way Tallow Ridge Roofing, a fictional Cincinnati roofer, works. The story is invented for this design sample.', about, 'about', '')
    contact = f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('Contact',None)])}<p class="eyebrow">Contact</p><h1>Start with a free inspection.</h1><p class="lede">Tell us what is going on. We will call you back to set a time. Or call <a href="tel:{c['tel']}">{c['phone']}</a>.</p></div></section>
<section class="sec"><div class="wrap two">
 <div class="panel" id="inspection"><h2>{CTA}</h2>
 {form('insp-form',[('name','Name','text',True,False),('phone','Phone','tel',True,False),('email','Email','email',False,False),('town','Town','text',True,False),('issue','What is going on?','select:A leak|Missing or damaged shingles|Storm damage|A replacement quote|Not sure',True,True),('msg','Anything else we should know?','textarea',False,True)],CTA)}</div>
 <div><h2 style="font-size:1.9rem">Office hours</h2><table class="hours"><caption class="sr-only">Office hours</caption><tbody><tr><th scope="row">Monday to Friday</th><td>7am to 5pm</td></tr><tr><th scope="row">Saturday</th><td>8am to noon</td></tr><tr><th scope="row">Storm calls</th><td>Phone answered after hours</td></tr></tbody></table>
 <h2 style="font-size:1.9rem;margin-top:1.6rem">Office</h2><p>3110 Ridgeline Road<br>Cincinnati, Ohio 45236<br><a href="tel:{c['tel']}">{c['phone']}</a></p>
 <p class="invented">Sample address, hours and phone number. License number: shown here once the owner provides it.</p></div></div></section>
"""
    P['contact'] = ('contact.html', 'Contact and free roof inspection | Tallow Ridge Roofing (sample)',
                    'Request a free roof inspection from Tallow Ridge Roofing, a fictional Cincinnati-area roofer. Sample details are invented for this design sample.', contact, 'contact', '')
    return P

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, 'contractors')
    CFG['dir'] = os.path.join(out, CFG['slug'])
    d = build(CFG, pages(), CSS, out)
    import shutil, glob
    src = '/tmp/claude-0/-home-claude/24020632-5365-5511-b200-acc6842a5608/scratchpad/fontsrc/node_modules/@fontsource'
    os.makedirs(os.path.join(d, 'fonts'), exist_ok=True)
    for fam, w, f in CFG['fonts']:
        pkg = f.rsplit('-latin', 1)[0]
        shutil.copy(os.path.join(src, pkg, 'files', f), os.path.join(d, 'fonts', f))
    for pkg in ('barlow-condensed', 'source-sans-3'):
        shutil.copy(os.path.join(src, pkg, 'LICENSE'), os.path.join(d, 'fonts', f'LICENSE-{pkg}.txt'))
    print('roofing built')
