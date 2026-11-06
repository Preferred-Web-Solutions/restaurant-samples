import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

CFG = dict(
    slug='ashgrove', name='Ashgrove', tagline='Seasonal tasting menu, Cincinnati.',
    logo_html='<span style="letter-spacing:.22em;text-transform:uppercase;font-size:1.15rem">Ashgrove</span>',
    phone='(513) 555-0187', tel='+15135550187', addr1='88 Ash Grove Lane', addr2='Cincinnati, Ohio 45202',
    hours_short=[('Wed & Thu', '5 to 9pm'), ('Fri & Sat', '5 to 10pm'), ('Sun', '5 to 8pm')],
    foot_hours_title='Dinner',
    cta='Reserve a table', cta_href='contact.html#reserve', menu_label='Navigate',
    nav=[('home', 'Home', 'index.html'), ('menu', 'Menu & wine', 'menu.html'), ('private', 'Private dining', 'private.html'), ('about', 'About', 'about.html'), ('contact', 'Visit', 'contact.html')],
    social=['Instagram'],
    fonts=[('Bodoni Moda', 400, 'bodoni-moda-400-normal.woff2'), ('Bodoni Moda', 500, 'bodoni-moda-500-normal.woff2'), ('Jost', 400, 'jost-400-normal.woff2'), ('Jost', 500, 'jost-500-normal.woff2')],
    preload=['bodoni-moda-400-normal.woff2', 'jost-400-normal.woff2'],
    credit=f'Sample website designed by Preferred Web Solutions &middot; <a href="mailto:{EMAIL}">{EMAIL}</a>. Ashgrove is a made-up business used to show what a restaurant site can look like. Menu, prices, hours, address and story are invented. Photos are for demonstration only.',
    invented_list='menu, prices, hours, address, phone number and story',
    cannot_do='You cannot make a reservation, order food or book an event here.',
)

CSS = r"""
:root{--bg:#F3ECDF;--surface:#FBF7EF;--soft:#E9E0CE;--ink:#13201B;--muted:#4D5A53;--line:#D9CEBB;--night:#0F1A16;--moss:#18291F;--ivory:#F3ECDF;--brass:#C9A66B;--brass-deep:#7A5B26;--sage:#B3C2B8;--focus:#7A5B26;
--display:"Bodoni Moda","Didot","Bodoni 72",Georgia,serif;--body:"Jost","Avenir Next","Segoe UI",system-ui,sans-serif;--radius:2px;--banner-bg:#C9A66B;--banner-ink:#0F1A16;
--btn-bg:#C9A66B;--btn-ink:#0F1A16;--head-bg:#0F1A16;--head-ink:#F3ECDF;--head-line:rgba(201,166,107,.35);--foot-bg:#0F1A16;--foot-ink:#F3ECDF;--btn-radius:0px}
body{font-weight:400}
.site-header :focus-visible,.site-footer :focus-visible,.night :focus-visible,.callbar :focus-visible{outline-color:#E5C98F}
.logo{font-weight:500;color:#F3ECDF}
.btn{letter-spacing:.14em;text-transform:uppercase;font-size:.85rem;font-weight:500;border-radius:0}
.btn--ghost{color:inherit}
h1,h2,h3{font-family:var(--display);font-weight:400;line-height:1.08;letter-spacing:.005em}
.eyebrow{font-size:.78rem;letter-spacing:.24em;text-transform:uppercase;color:var(--brass-deep);margin:0 0 1rem;font-weight:500}
.night .eyebrow,.moss .eyebrow{color:#C9A66B}
.lede{font-size:clamp(1.1rem,1.8vw,1.3rem);max-width:34rem;font-weight:400}
.night{background:var(--night);color:var(--ivory)}
.moss{background:var(--moss);color:var(--ivory)}
.rule{border:0;border-top:1px solid var(--brass);margin:0}
/* hero: type panel + full photo */
.hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);min-height:min(40rem,calc(100vh - var(--sb-h) - var(--hd-h)))}
.hero .copy{padding:clamp(2.5rem,6vw,5rem) clamp(1.25rem,5vw,4.5rem) clamp(2.5rem,6vw,5rem) max(20px,calc((100vw - var(--wrap))/2 + 32px));display:flex;flex-direction:column;justify-content:center}
.hero h1{font-size:clamp(3.2rem,7.2vw,6rem);letter-spacing:.02em;line-height:.95;margin-bottom:1.2rem}
.hero .photo{position:relative;min-height:22rem}
.hero .photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.8rem}
@media (max-width:860px){.hero{grid-template-columns:minmax(0,1fr);min-height:0}.hero .copy{padding:2.2rem 20px 2.4rem}.hero .photo{min-height:0;aspect-ratio:3/2}.hero h1{font-size:clamp(3.4rem,17vw,5rem)}}
/* facts row */
.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.5rem 2rem;list-style:none;padding:1.8rem 0}
.facts li{display:flex;flex-direction:column;gap:.15rem}
.facts b{font-weight:500;font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:#C9A66B}
.facts a{display:inline-flex;align-items:center;min-height:44px}
@media (max-width:700px){.facts{grid-template-columns:minmax(0,1fr);gap:.8rem}}
/* tasting card */
.tasting{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(2rem,6vw,5rem);align-items:center}
.card{background:var(--surface);border:1px solid var(--brass-deep);outline:1px solid var(--brass-deep);outline-offset:-9px;padding:clamp(1.8rem,4vw,3rem)}
.card h2{font-size:clamp(1.9rem,4vw,2.8rem);margin-bottom:.4rem}
.price-row{display:flex;gap:2rem;margin:.8rem 0 1.4rem;font-size:.95rem;color:var(--muted)}
.price-row b{display:block;font-family:var(--display);font-weight:400;font-size:1.9rem;color:var(--ink);line-height:1}
.courses{list-style:none;display:grid;gap:1.15rem}
.course{display:grid;grid-template-columns:2.6rem minmax(0,1fr);gap:.4rem .8rem;padding-top:1.1rem;border-top:1px solid var(--line)}
.course .n{font-family:var(--display);font-size:1.5rem;color:var(--brass-deep);line-height:1.1}
.course h3{font-size:1.45rem}
.course p{margin:.15rem 0 0;color:var(--muted)}
.course .tag{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;color:var(--brass-deep);font-weight:500}
.tasting img{width:100%;aspect-ratio:4/5;object-fit:cover}
.cap{font-size:.9rem;color:var(--muted);margin-top:.6rem}
@media (max-width:860px){.tasting{grid-template-columns:minmax(0,1fr)}.tasting img{aspect-ratio:4/3}}
/* split */
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(2rem,6vw,5rem);align-items:center}
.split.rev>:first-child{order:2}
.split img{width:100%;aspect-ratio:5/4;object-fit:cover}
.split h2{font-size:clamp(2rem,4.5vw,3.2rem);margin-bottom:1rem}
@media (max-width:860px){.split{grid-template-columns:minmax(0,1fr)}.split.rev>:first-child{order:0}}
.page-head{background:var(--moss);color:var(--ivory);padding-top:clamp(2.6rem,6vw,4.5rem);padding-bottom:clamp(2.2rem,5vw,3.5rem)}
.page-head h1{font-size:clamp(2.6rem,7vw,5rem);margin-bottom:.8rem;letter-spacing:.01em}
.page-head .eyebrow{color:#C9A66B}
.page-head .lede{margin:0}
.slides{color:var(--ink)}
.slide-stage{background:var(--night);border-radius:0}
.slide figcaption{background:var(--surface)}
.night .slide-ctrl button,.moss .slide-ctrl button{color:var(--ivory)}
.night .slide-ctrl ol button[aria-current="true"],.moss .slide-ctrl ol button[aria-current="true"]{background:var(--brass);color:var(--night);border-color:var(--brass)}
.wine{width:100%;border-collapse:collapse;margin-top:1rem}
.wine th,.wine td{text-align:left;padding:.8rem 0;border-bottom:1px solid var(--line);vertical-align:top}
.wine td:last-child{text-align:right;font-family:var(--display);font-size:1.2rem}
.wine small{display:block;color:var(--muted);font-size:.92rem}
.opts{list-style:none;display:grid;gap:0;margin-top:1.4rem}
.opts li{padding:1.1rem 0;border-top:1px solid var(--brass)}
.opts h3{font-size:1.5rem}
.opts p{margin:.2rem 0 0}
.panel{background:var(--surface);border:1px solid var(--brass-deep);padding:clamp(1.3rem,3vw,2.2rem)}
.panel h2{font-size:clamp(1.8rem,3.5vw,2.5rem);margin-bottom:.6rem}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(2rem,5vw,4.5rem);align-items:start}
@media (max-width:860px){.two{grid-template-columns:minmax(0,1fr)}}
.hours{width:100%;border-collapse:collapse;margin:.6rem 0 1rem}
.hours th,.hours td{text-align:left;padding:.6rem 0;border-bottom:1px solid var(--line);font-weight:400}
.hours td{text-align:right}
.note{margin-top:1.6rem;font-size:.95rem;color:var(--muted)}
.invented{font-size:.9rem;color:var(--muted);font-style:italic}
blockquote{margin:1.6rem 0;padding:0 0 0 1.4rem;border-left:2px solid var(--brass);font-family:var(--display);font-size:clamp(1.3rem,2.5vw,1.8rem);line-height:1.3}
blockquote cite{display:block;font-family:var(--body);font-style:normal;font-size:.9rem;letter-spacing:.14em;text-transform:uppercase;margin-top:.7rem}
.reserve-band{background:var(--moss);color:var(--ivory)}
.reserve-band .wrap{display:flex;flex-wrap:wrap;gap:1.4rem 3rem;align-items:center;justify-content:space-between}
.reserve-band h2{font-size:clamp(1.9rem,4.5vw,3.2rem);max-width:18ch}
.reserve-band :focus-visible{outline-color:#E5C98F}
.field input,.field select,.field textarea{border:1px solid var(--ink);border-radius:0}
.demo-note{color:var(--brass-deep)}
"""

def course(n, name, desc, tag):
    return f'<li class="course"><span class="n" aria-hidden="true">{n}</span><div><span class="tag">{tag}</span><h3><span class="sr-only">{n}. </span>{name}</h3><p>{desc}</p></div></li>'

def pages():
    c = CFG; P = {}
    home = f"""
<section class="hero night"><div class="copy"><p class="eyebrow">Seasonal tasting menu &middot; Cincinnati</p><h1>Ashgrove</h1>
 <p class="lede">Five courses, written each week around what the farms bring in. Thirty-eight seats, one dining room, and a kitchen you can watch from every table. Dinner Wednesday through Sunday.</p>
 <div class="btn-row"><a class="btn" href="contact.html#reserve">Reserve a table</a><a class="btn btn--ghost" href="menu.html">View the menu</a></div></div>
 <div class="photo">{img(c,'ash_candles','Candles and wine glasses glowing along a long dining table in a dark room','(min-width:860px) 52vw, 100vw',eager=True)}</div></section>
<div class="moss"><div class="wrap"><ul class="facts">
 <li><b>Dinner</b><span>Wednesday to Sunday, from 5pm</span></li><li><b>Find us</b><span>88 Ash Grove Lane, Cincinnati</span></li><li><b>Call</b><a href="tel:{c['tel']}">{c['phone']}</a></li></ul></div></div>
<section class="sec" aria-labelledby="t-h"><div class="wrap tasting">
 <div class="card"><p class="eyebrow">The tasting menu</p><h2 id="t-h">This week&rsquo;s five courses.</h2>
 <div class="price-row"><span><b>$95</b>Per guest</span><span><b>$55</b>Wine pairing</span></div>
 <ol class="courses">{course('I','Sweet corn velouté','Brown butter, chive oil, a spoon of crème fraîche.','Late summer')}{course('II','Gulf shrimp','Saffron squash purée, shaved fennel, citrus.','From the coast')}{course('III','Hand-rolled pappardelle','Braised short rib, gremolata, aged Parmesan.','House pasta')}{course('IV','Seared beef filet','Glazed carrots, asparagus, pea shoots, pan jus.','Ohio beef')}{course('V','Honey &amp; lavender panna cotta','Poached pear, toasted hazelnut.','Dessert')}</ol>
 <p class="note">Vegetarian menu available with 48 hours&rsquo; notice. Prices and availability can change. Please tell us about any allergies when you reserve.</p>
 <p><a class="btn" href="contact.html#reserve">Reserve a table</a></p></div>
 <figure style="margin:0">{img(c,'ash_filet','Seared beef filet with glazed carrots, asparagus and pea shoots on a white plate','(min-width:860px) 40vw, 100vw')}<figcaption class="cap">Course IV, seared beef filet.</figcaption></figure>
</div></section>
<section class="sec night" aria-labelledby="k-h"><div class="wrap split">
 <div><p class="eyebrow">The kitchen</p><h2 id="k-h">We cook what arrived that morning.</h2><p class="lede">Early corn in July, the last beets in November. When a farm runs out, the menu changes.</p>
 <p class="invented" style="color:#C9D1CB">Chef Nora Ellison and her story are invented for this sample.</p><a class="link-arrow" href="about.html" style="color:#C9A66B">About Ashgrove &rarr;</a></div>
 {img(c,'ash_shrimp','Seared Gulf shrimp over saffron squash puree with fennel on a blue-green plate','(min-width:860px) 45vw, 100vw')}
</div></section>
<section class="sec" aria-labelledby="r-h"><div class="wrap split rev">
 <div><p class="eyebrow">The room</p><h2 id="r-h">Candlelight, linen, and an open kitchen.</h2><p class="lede">Every table faces the pass, so you can watch your course being plated. The room seats thirty-eight, and we keep it quiet enough to talk.</p>
 <p><a class="link-arrow" href="menu.html#cellar">See the wine list &rarr;</a> &nbsp; <a class="link-arrow" href="private.html">Private dining &rarr;</a></p></div>
 {img(c,'ash_table','A set table with linen napkins, gold chargers and wine glasses by a window','(min-width:860px) 45vw, 100vw')}
</div></section>
<section class="sec reserve-band" aria-labelledby="rb-h"><div class="wrap"><h2 id="rb-h">Join us for dinner.</h2><a class="btn" href="contact.html#reserve">Reserve a table</a></div></section>
"""
    P['home'] = ('index.html', 'Ashgrove | Seasonal tasting menu restaurant in Cincinnati (sample)',
                 'Ashgrove is a fictional Cincinnati restaurant with a five-course seasonal tasting menu, thirty-eight seats and an open kitchen. A design sample by Preferred Web Solutions.', home, 'home', '')
    menu = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Wednesday to Sunday</p><h1>Menu &amp; wine</h1><p class="lede">One tasting menu, five courses, rewritten each week. The wine list is short and chosen for the food.</p></div></section>
<section class="sec" aria-labelledby="m-h"><div class="wrap tasting">
 <div class="card"><h2 id="m-h">The tasting menu</h2><div class="price-row"><span><b>$95</b>Per guest</span><span><b>$55</b>Wine pairing</span><span><b>$32</b>Zero-proof pairing</span></div>
 <ol class="courses">{course('I','Sweet corn velouté','Brown butter, chive oil, a spoon of crème fraîche.','Late summer')}{course('II','Gulf shrimp','Saffron squash purée, shaved fennel, citrus.','From the coast')}{course('III','Hand-rolled pappardelle','Braised short rib, gremolata, aged Parmesan.','House pasta')}{course('IV','Seared beef filet','Glazed carrots, asparagus, pea shoots, pan jus.','Ohio beef')}{course('V','Honey &amp; lavender panna cotta','Poached pear, toasted hazelnut.','Dessert')}</ol>
 <p class="note">Vegetarian menu available with 48 hours&rsquo; notice. Prices and availability can change. Please tell us about any allergies when you reserve.</p></div>
 <figure style="margin:0">{img(c,'ash_shrimp','Seared Gulf shrimp over saffron squash puree with fennel on a blue-green plate','(min-width:860px) 40vw, 100vw')}<figcaption class="cap">Course II, Gulf shrimp, saffron squash.</figcaption></figure>
</div></section>
<section class="sec moss" id="cellar" aria-labelledby="c-h"><div class="wrap split">
 <div><p class="eyebrow">The cellar</p><h2 id="c-h">A short list, chosen for the food.</h2><p class="lede">About forty bottles, mostly from small growers, plus a few pours by the glass that change when the menu does.</p>
 <table class="wine" style="color:var(--ivory)"><caption class="sr-only">Wines by the glass</caption><thead><tr><th scope="col">By the glass</th><th scope="col" style="text-align:right">Price</th></tr></thead><tbody>
 <tr><th scope="row" style="font-weight:400">Dry Riesling<small style="color:#C9D1CB">Finger Lakes, New York</small></th><td>$14</td></tr>
 <tr><th scope="row" style="font-weight:400">Pinot Noir<small style="color:#C9D1CB">Willamette Valley, Oregon</small></th><td>$17</td></tr>
 <tr><th scope="row" style="font-weight:400">Chenin Blanc<small style="color:#C9D1CB">Loire Valley, France</small></th><td>$15</td></tr>
 <tr><th scope="row" style="font-weight:400">Zero-proof pairing<small style="color:#C9D1CB">Shrubs, tea and sparkling cider</small></th><td>$32</td></tr></tbody></table></div>
 {img(c,'ash_wine','A glass of rosé on a tiled table beside a vase of autumn flowers','(min-width:860px) 45vw, 100vw')}
</div></section>
<section class="sec" style="text-align:left"><div class="wrap"><a class="btn" href="contact.html#reserve">Reserve a table</a></div></section>
"""
    P['menu'] = ('menu.html', 'Tasting menu and wine list | Ashgrove, Cincinnati (sample)',
                 'The five-course seasonal tasting menu and short wine list at Ashgrove, a fictional Cincinnati restaurant. Prices are invented for this design sample.', menu, 'menu', '')
    private = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Private dining</p><h1>The whole room, for one evening.</h1><p class="lede">Rehearsal dinners, milestone birthdays, a team that deserves it. We close the room and build the menu with you.</p></div></section>
<section class="sec" aria-label="Private dining options"><div class="wrap two">
 <div><h2 style="font-size:clamp(1.8rem,3.5vw,2.5rem)">Three ways to take the room.</h2>
 <ul class="opts"><li><h3>Chef&rsquo;s table</h3><p>Up to 10 guests, Wednesday and Thursday.</p></li><li><h3>Full buyout</h3><p>Up to 38 seated guests, any evening we are open.</p></li><li><h3>Wine dinners</h3><p>Paired with a visiting grower, by arrangement.</p></li></ul>
 <figure style="margin:2rem 0 0">{img(c,'ash_candles','Candles and wine glasses glowing along a long dining table in a dark room','(min-width:860px) 45vw, 100vw')}</figure></div>
 <div class="panel" id="inquiry"><h2>Start an inquiry</h2>
 {form('priv-form',[('name','Name','text',True,False),('email','Email','email',True,False),('date','Preferred date','date',True,False),('guests','Guests','number',True,False),('msg','Tell us about the evening','textarea',False,True)],'Send inquiry')}</div>
</div></section>
"""
    P['private'] = ('private.html', 'Private dining | Ashgrove, Cincinnati (sample)',
                    'Chef\'s table, full buyouts and wine dinners at Ashgrove, a fictional Cincinnati restaurant. A design sample by Preferred Web Solutions.', private, 'private', '')
    about = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">About Ashgrove</p><h1>Thirty-eight seats, one kitchen.</h1></div></section>
<section class="sec" aria-label="About"><div class="wrap split">
 <div><h2>We cook what arrived that morning.</h2><p class="lede">Chef Nora Ellison writes the menu each week after the farm deliveries, so early corn shows up in July and the last beets in November. When a farm runs out, the menu changes.</p>
 <blockquote>&ldquo;A short menu lets us do each course properly.&rdquo;<cite>Nora Ellison, chef</cite></blockquote>
 <p class="invented">The chef, story and quote are invented for this sample. On a real site, they come from the owner.</p></div>
 {img(c,'ash_wine','A glass of rosé on a tiled table beside a vase of autumn flowers','(min-width:860px) 45vw, 100vw')}
</div></section>
<section class="sec night" aria-labelledby="g-h"><div class="wrap"><p class="eyebrow">Gallery</p><h2 id="g-h" style="font-size:clamp(1.9rem,4vw,2.8rem);margin-bottom:1.5rem">An evening at Ashgrove.</h2>
 {slideshow(c,'An evening at Ashgrove, photo slideshow',[
  ('ash_table','A set table with linen napkins, gold chargers and wine glasses by a window','The table, set for six.'),
  ('ash_shrimp','Seared Gulf shrimp over saffron squash puree with fennel on a blue-green plate','Course II, Gulf shrimp.'),
  ('ash_candles','Candles and wine glasses glowing along a long dining table in a dark room','After dark.'),
  ('ash_filet','Seared beef filet with glazed carrots, asparagus and pea shoots on a white plate','Course IV, beef filet.'),
  ('ash_wine','A glass of rosé on a tiled table beside a vase of autumn flowers','A pour from the cellar.')],'show')}</div></section>
<section class="sec reserve-band" aria-labelledby="ab-h"><div class="wrap"><h2 id="ab-h">Join us for dinner.</h2><a class="btn" href="contact.html#reserve">Reserve a table</a></div></section>
"""
    P['about'] = ('about.html', 'About | Ashgrove, Cincinnati tasting menu restaurant (sample)',
                  'The kitchen and the room at Ashgrove, a fictional Cincinnati restaurant. The chef and story are invented for this design sample by Preferred Web Solutions.', about, 'about', '')
    contact = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Visit</p><h1>Join us for dinner.</h1></div></section>
<section class="sec" aria-label="Reservations and visit details"><div class="wrap two">
 <div class="panel" id="reserve"><h2>Reserve a table</h2><p>Tables open 30 days ahead. For parties over six, see <a href="private.html">private dining</a>. You can also call <a href="tel:{c['tel']}">{c['phone']}</a>.</p>
 {form('res-form',[('name','Name','text',True,False),('email','Email','email',True,False),('date','Date','date',True,False),('time','Time','select:5:00 pm|5:30 pm|6:00 pm|6:30 pm|7:00 pm|7:30 pm|8:00 pm',True,False),('guests','Guests','select:1|2|3|4|5|6',True,False),('notes','Allergies or occasion','textarea',False,True)],'Reserve a table',note='Working demo. Not connected yet.')}</div>
 <div><h2 style="font-size:1.9rem">Dinner hours</h2>
 <table class="hours"><caption class="sr-only">Dinner hours</caption><tbody><tr><th scope="row">Wednesday &amp; Thursday</th><td>5 to 9pm</td></tr><tr><th scope="row">Friday &amp; Saturday</th><td>5 to 10pm</td></tr><tr><th scope="row">Sunday</th><td>5 to 8pm</td></tr><tr><th scope="row">Monday &amp; Tuesday</th><td>Closed</td></tr></tbody></table>
 <h2 style="font-size:1.9rem;margin-top:1.8rem">Find us</h2><p>88 Ash Grove Lane<br>Cincinnati, Ohio 45202<br>Valet on Friday and Saturday. Smart casual dress.</p>
 <p><a class="btn btn--ghost btn--sm" href="#" data-demo="Directions are a demo on this sample." style="color:var(--ink)">Get directions (demo)</a></p>
 <p class="invented">Sample address, hours, phone and policies. On a real site, these are confirmed with the owner.</p>
 <h2 style="font-size:1.9rem;margin-top:1.8rem">Guests &amp; press</h2><p>A real site links to the restaurant&rsquo;s Google, Yelp or OpenTable reviews and any press it has earned, quoted only with permission. We never write reviews or copy them from other sites.</p>
 <p><a class="btn btn--ghost btn--sm" href="#" data-demo="Reviews link is a demo on this sample." style="color:var(--ink)">Read guest reviews (demo)</a></p></div>
</div></section>
<section class="sec moss" aria-labelledby="nl-h"><div class="wrap two"><div><p class="eyebrow">The weekly menu</p><h2 id="nl-h" style="font-size:clamp(1.8rem,3.5vw,2.6rem)">New courses, in your inbox on Mondays.</h2><p>One short email when the menu changes, plus first notice of wine dinners. Unsubscribe any time.</p></div>
 <div class="panel" style="color:var(--ink)">{form('news-form',[('email','Email address','email',True,True)],'Subscribe')}</div></div></section>
"""
    P['contact'] = ('contact.html', 'Reserve a table and visit | Ashgrove, Cincinnati (sample)',
                    'Reserve a table, see dinner hours and find Ashgrove, a fictional Cincinnati restaurant. Sample details are invented for this design sample.', contact, 'contact', '')
    return P

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else None
    CFG['dir'] = os.path.join(REPO, 'ashgrove')
    build(CFG, pages(), CSS, out)
    print('ashgrove built')
