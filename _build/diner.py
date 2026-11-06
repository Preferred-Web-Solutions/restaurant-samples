import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

CFG = dict(
    slug='diner', name='Hollis Street Diner', tagline='Breakfast and lunch counter, since 1962.',
    logo_html='Hollis Street<span class="logo-sfx" style="font-size:.7em;opacity:.85;margin-left:.45rem;font-family:var(--body);font-weight:700;letter-spacing:.06em">DINER</span>',
    phone='(513) 555-0142', tel='+15135550142', addr1='412 Hollis Street', addr2='Cincinnati, Ohio 45202',
    hours_short=[('Monday to Friday', '6am to 3pm'), ('Saturday', '7am to 3pm'), ('Sunday', '7am to 2pm')],
    cta='Order online', cta_href='menu.html#order', menu_label='Navigate',
    nav=[('home', 'Home', 'index.html'), ('menu', 'Menu', 'menu.html'), ('pies', 'Pies', 'pies.html'), ('about', 'About', 'about.html'), ('contact', 'Contact', 'contact.html')],
    order_dropdown=[('Pickup (demo)', 'Ready in about 15 minutes', 'Pickup ordering is a demo on this sample. Nothing is connected yet.'),
                    ('Delivery (demo)', 'Through a delivery partner', 'Delivery ordering is a demo on this sample. Nothing is connected yet.')],
    social=['Instagram'],
    fonts=[('Shrikhand', 400, 'shrikhand-400-normal.woff2'), ('Work Sans', 400, 'work-sans-400-normal.woff2'), ('Work Sans', 600, 'work-sans-600-normal.woff2'), ('Work Sans', 800, 'work-sans-800-normal.woff2')],
    preload=['shrikhand-400-normal.woff2', 'work-sans-400-normal.woff2'],
    credit=f'Sample website designed by Preferred Web Solutions &middot; <a href="mailto:{EMAIL}">{EMAIL}</a>. Hollis Street Diner is a made-up business used to show what a restaurant site can look like. Menu, prices, hours, address and story are invented. Photos are for demonstration only.',
)

CSS = r"""
:root{--bg:#F7EEDB;--surface:#FFFBF2;--soft:#EFE3C8;--ink:#1C2529;--muted:#4A5459;--line:#DCCFB2;--accent:#B5301C;--mustard:#EFAE2C;--sage:#A9C2A6;--deep:#1E4945;--focus:#1E6FD9;
--display:"Shrikhand",Georgia,serif;--body:"Work Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--radius:10px;--banner-bg:#1C2529;--banner-ink:#F7EEDB;
--btn-bg:#B5301C;--btn-ink:#fff;--head-bg:#1E4945;--head-ink:#F7EEDB;--head-line:rgba(255,255,255,.2);--foot-bg:#1C2529;--foot-ink:#F7EEDB}
.site-header :focus-visible,.site-footer :focus-visible,.dark :focus-visible,.callbar :focus-visible{outline-color:#FFD76A}
.site-header .logo{color:#FFD76A}
.site-header .btn{border-color:#fff}
h1,h2{font-family:var(--display);font-weight:400;line-height:1.05}
.eyebrow{font-weight:800;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 .8rem}
.dark .eyebrow{color:#FFD76A}
.lede{font-size:clamp(1.1rem,2vw,1.3rem);max-width:34rem}
/* hero */
.hero{padding-top:clamp(2rem,5vw,4rem);padding-bottom:clamp(3.5rem,7vw,5.5rem)}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(1.5rem,4vw,4rem);align-items:center}
.hero h1{font-size:clamp(2.6rem,7vw,5.2rem);margin-bottom:1.1rem}
.hero h1 em{color:var(--accent);font-style:normal}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.4rem}
.btn-row .btn--ghost{color:var(--ink)}
.photo-frame{position:relative;border-radius:var(--radius);border:3px solid var(--ink);box-shadow:8px 8px 0 var(--mustard)}
.photo-frame img{width:100%;aspect-ratio:4/3.4;object-fit:cover;border-radius:7px}
.check{position:absolute;left:-10px;bottom:-34px;width:min(15.5rem,70%);padding:1rem 1.1rem 1.7rem;background:#fff;color:#1C2529;font-family:"Courier New",ui-monospace,monospace;font-size:.88rem;line-height:1.45;transform:rotate(-2.5deg);box-shadow:0 10px 22px rgba(0,0,0,.25);-webkit-mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/14px 100%;mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/14px 100%}
.check b{display:block}
.check .row{display:flex;justify-content:space-between;gap:.5rem;border-top:1px dashed #1C2529;margin-top:.45rem;padding-top:.4rem;font-weight:700}
@media (max-width:860px){.hero-grid{grid-template-columns:minmax(0,1fr)}.check{left:8px;bottom:-30px}.photo-frame{margin-bottom:2.4rem}}
/* facts strip */
.strip{background:var(--mustard);color:var(--ink)}
.strip ul{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem 2rem;list-style:none;padding:1.1rem 0}
.strip li{display:flex;flex-direction:column;font-size:1.02rem}
.strip b{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase}
.strip a{font-weight:800;display:inline-flex;align-items:center;min-height:44px}
@media (max-width:640px){.strip ul{grid-template-columns:minmax(0,1fr);gap:.2rem}.strip li{flex-direction:row;gap:.8rem;align-items:center;min-height:44px}}
/* rail */
.rail-sec h2{font-size:clamp(2rem,5vw,3.4rem);max-width:22ch}
.rail-sec .lede{margin-top:.8rem}
.rail{margin-top:2.6rem;position:relative;padding-top:1.4rem}
.rail::before{content:"";position:absolute;left:0;right:0;top:0;height:10px;border-radius:5px;background:linear-gradient(#c9ced1,#7c8489);box-shadow:0 3px 6px rgba(0,0,0,.25)}
.checks{display:grid;grid-template-columns:repeat(auto-fit,minmax(11.5rem,1fr));gap:1rem;list-style:none}
.rail .check-c{position:relative;background:#fff;padding:1.2rem 1rem 2rem;font-family:"Courier New",ui-monospace,monospace;font-size:.9rem;line-height:1.45;-webkit-mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/14px 100%;mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/14px 100%;box-shadow:0 8px 14px rgba(0,0,0,.12)}
.rail .check-c::before{content:"";position:absolute;top:-4px;left:50%;width:34px;height:12px;margin-left:-17px;border-radius:3px;background:#8a9297}
.check-c .day{display:block;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);font-size:.8rem}
.check-c h3{font-family:var(--body);font-weight:800;font-size:1.1rem;margin:.25rem 0}
.check-c .price{font-weight:800;margin-top:.6rem;display:block}
/* weekend feature */
.dark{background:var(--deep);color:#F7EEDB}
.feature{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(1.5rem,5vw,4.5rem);align-items:center}
.feature img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:var(--radius);border:3px solid #F7EEDB}
.feature h2{font-size:clamp(2rem,5vw,3.3rem);margin-bottom:1rem}
.dark .btn{--btn-bg:#EFAE2C;--btn-ink:#1C2529;border-color:#EFAE2C}
.dark .btn--ghost{--btn-bg:transparent;--btn-ink:#F7EEDB;border-color:#F7EEDB;background:transparent;color:#F7EEDB}
@media (max-width:860px){.feature{grid-template-columns:minmax(0,1fr)}.feature img{aspect-ratio:4/3}}
/* teasers */
.teasers{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.2rem}
.tease{background:var(--surface);border:2px solid var(--ink);border-radius:var(--radius);padding:1.6rem;display:flex;flex-direction:column;gap:.6rem;align-items:flex-start}
.tease h2{font-size:clamp(1.7rem,3.5vw,2.3rem)}
.tease p{margin:0;max-width:30rem}
@media (max-width:760px){.teasers{grid-template-columns:minmax(0,1fr)}}
.order-band{background:var(--accent);color:#fff}
.order-band .wrap{display:flex;flex-wrap:wrap;gap:1.2rem 2rem;align-items:center;justify-content:space-between}
.order-band h2{font-size:clamp(1.9rem,4.5vw,3rem);max-width:20ch}
.order-band .btn{--btn-bg:#fff;--btn-ink:#7f1f10;border-color:#fff}
.order-band :focus-visible{outline-color:#fff}
/* page head */
.page-head{background:var(--soft);border-bottom:2px solid var(--ink);padding-top:clamp(2.2rem,5vw,3.8rem);padding-bottom:clamp(2rem,4vw,3rem)}
.page-head h1{font-size:clamp(2.4rem,6vw,4.2rem);margin-bottom:.7rem}
.page-head .lede{margin:0}
.jump{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;margin-top:1.3rem}
.jump a{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border:2px solid var(--ink);border-radius:999px;font-weight:700;text-decoration:none;background:var(--surface)}
.jump a:hover{background:var(--mustard)}
/* order panel */
.order-panel{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin-top:2rem}
.order-panel .op{border:2px solid var(--ink);border-radius:var(--radius);background:var(--surface);padding:1.3rem;display:flex;flex-direction:column;gap:.5rem;align-items:flex-start}
.order-panel h3{font-size:1.2rem;font-weight:800}
.order-panel p{margin:0}
@media (max-width:640px){.order-panel{grid-template-columns:minmax(0,1fr)}}
/* menu */
.menu-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3rem 4rem;margin-top:2.4rem}
@media (max-width:900px){.menu-grid{grid-template-columns:minmax(0,1fr)}}
.msec h2{font-size:clamp(1.8rem,3.5vw,2.4rem)}
.msec .sub{color:var(--muted);margin:.2rem 0 1rem}
.mi{padding:.7rem 0;border-top:1px dotted var(--ink)}
.mi:first-of-type{border-top:2px solid var(--ink)}
.mi .top{display:flex;justify-content:space-between;gap:1rem;font-weight:800;font-size:1.08rem}
.mi p{margin:.15rem 0 0;color:var(--muted)}
.note{margin-top:2.4rem;padding:1rem 1.2rem;border-left:6px solid var(--mustard);background:var(--surface)}
.side-photo{margin-top:2.4rem}
.side-photo img{width:100%;aspect-ratio:21/9;object-fit:cover;border-radius:var(--radius);border:3px solid var(--ink)}
/* about */
.story{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(1.5rem,5vw,4rem);align-items:start}
.story img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:var(--radius);border:3px solid var(--ink)}
.story h2{font-size:clamp(2rem,4.5vw,3rem);margin-bottom:1rem}
blockquote{margin:1.6rem 0;padding:0 0 0 1.2rem;border-left:6px solid var(--accent);font-size:1.35rem;font-weight:600;line-height:1.35}
blockquote cite{display:block;font-size:.95rem;font-style:normal;font-weight:700;margin-top:.5rem}
.invented{font-size:.9rem;color:var(--muted);font-style:italic}
.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;margin-top:2rem;list-style:none}
.facts li{background:var(--surface);border:2px solid var(--ink);border-radius:var(--radius);padding:1rem}
.facts b{display:block;font-family:var(--display);font-size:2rem;font-weight:400;color:var(--accent);line-height:1}
@media (max-width:860px){.story{grid-template-columns:minmax(0,1fr)}.story img{aspect-ratio:16/10}.facts{grid-template-columns:minmax(0,1fr)}}
.slide-stage{border:3px solid var(--ink);background:var(--surface)}
.dark .slide-ctrl ol button[aria-current="true"]{background:#EFAE2C;color:#1C2529;border-color:#EFAE2C}
.slide figcaption{background:var(--surface);color:var(--ink);font-weight:600}
/* pies */
.pies{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1rem;margin-top:2rem;list-style:none}
.pie{background:var(--surface);border:2px solid var(--ink);border-radius:var(--radius);padding:1.2rem}
.pie h3{font-family:var(--body);font-weight:800;font-size:1.15rem}
.pie p{margin:.3rem 0 0}
.pie .price{font-weight:800;color:var(--accent)}
.pie-art{width:min(100%,22rem);height:auto;justify-self:center}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:start}
@media (max-width:860px){.two{grid-template-columns:minmax(0,1fr)}}
.panel{background:var(--surface);border:2px solid var(--ink);border-radius:var(--radius);padding:clamp(1.2rem,3vw,2rem)}
.panel h2{font-size:clamp(1.7rem,3.5vw,2.3rem);margin-bottom:.6rem}
/* contact */
.hours{width:100%;border-collapse:collapse;margin:.6rem 0 1rem}
.hours th,.hours td{text-align:left;padding:.55rem 0;border-bottom:1px dotted var(--ink)}
.hours td{text-align:right;font-weight:700}
.map-art{width:100%;height:auto;border:2px solid var(--ink);border-radius:var(--radius);background:var(--surface)}
"""

def pie_svg():
    return ('<svg class="pie-art" viewBox="0 0 240 200" role="img" aria-label="Illustration of a whole pie with a lattice top"><ellipse cx="120" cy="170" rx="96" ry="14" fill="#1C2529" opacity=".15"/>'
            '<ellipse cx="120" cy="112" rx="104" ry="62" fill="#D9A04A" stroke="#1C2529" stroke-width="4"/><ellipse cx="120" cy="104" rx="96" ry="54" fill="#B5301C" stroke="#1C2529" stroke-width="4"/>'
            '<g stroke="#EFAE2C" stroke-width="9" stroke-linecap="round" fill="none"><path d="M52 92 L186 124"/><path d="M70 74 L204 108"/><path d="M96 62 L190 84"/><path d="M60 118 L150 146"/><path d="M188 88 L102 138"/><path d="M168 74 L72 112"/><path d="M144 64 L62 96"/></g>'
            '<ellipse cx="120" cy="104" rx="96" ry="54" fill="none" stroke="#1C2529" stroke-width="4"/></svg>')

def map_svg():
    return ('<svg class="map-art" viewBox="0 0 400 240" role="img" aria-label="Simple sketch map: Hollis Street runs left to right, the diner sits on the north side with a parking lot behind it, and a side street crosses on the right"><rect width="400" height="240" fill="#F7EEDB"/>'
            '<rect x="0" y="100" width="400" height="44" fill="#fff" stroke="#1C2529" stroke-width="3"/><path d="M0 122H400" stroke="#EFAE2C" stroke-width="3" stroke-dasharray="14 10"/>'
            '<rect x="300" y="0" width="44" height="240" fill="#fff" stroke="#1C2529" stroke-width="3"/>'
            '<rect x="110" y="38" width="90" height="52" fill="#B5301C" stroke="#1C2529" stroke-width="3"/><rect x="30" y="22" width="76" height="68" fill="#A9C2A6" stroke="#1C2529" stroke-width="3"/>'
            '<text x="155" y="68" font-family="Work Sans,sans-serif" font-weight="800" font-size="13" text-anchor="middle" fill="#fff">DINER</text>'
            '<text x="68" y="60" font-family="Work Sans,sans-serif" font-weight="700" font-size="12" text-anchor="middle" fill="#1C2529">Parking</text>'
            '<text x="12" y="170" font-family="Work Sans,sans-serif" font-weight="700" font-size="13" fill="#1C2529">Hollis Street</text>'
            '<text x="322" y="226" font-family="Work Sans,sans-serif" font-weight="700" font-size="12" text-anchor="middle" fill="#1C2529" transform="rotate(-90 322 226)">Main</text></svg>')

def mi(name, price, desc):
    return f'<div class="mi"><div class="top"><span>{name}</span><span>{price}</span></div><p>{desc}</p></div>'

def pages():
    c = CFG; P = {}
    # ---------------- HOME
    home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div><p class="eyebrow">Breakfast &amp; lunch &middot; Cincinnati</p>
 <h1>Eggs, stacks &amp; <em>bottomless</em> coffee.</h1>
 <p class="lede">Griddle breakfast all day, hand-pattied burgers at lunch, and a pie case that is empty by two. Grab a stool at the counter or order ahead.</p>
 <div class="btn-row"><a class="btn" href="menu.html#order">Order online</a><a class="btn btn--ghost" href="menu.html">See the menu</a></div></div>
 <div class="photo-frame">{img(c,'diner_eggs','Two sunny-side-up eggs, crispy hash browns, bacon and buttered toast on a white plate','(min-width:860px) 46vw, 100vw',eager=True)}
 <div class="check" aria-hidden="true"><b>Table 4 &nbsp; #0214</b>The No. 1<br>Two eggs any style, hash browns, bacon, toast<br>Bottomless coffee<div class="row"><span>Total</span><span>$9.25</span></div></div></div>
</div></section>
<div class="strip"><div class="wrap"><ul>
 <li><b>Open today</b><span>6am to 3pm</span></li>
 <li><b>Call</b><a href="tel:{c['tel']}">{c['phone']}</a></li>
 <li><b>Parking</b><span>Free lot out back</span></li></ul></div></div>
<section class="sec rail-sec" aria-labelledby="rail-h"><div class="wrap">
 <p class="eyebrow">On the rail this week</p><h2 id="rail-h">Daily specials, hung up fresh every morning.</h2>
 <p class="lede">One special a day, written on a guest check and clipped to the rail above the griddle. When the check comes down, it is gone.</p>
 <div class="rail"><ul class="checks">
  <li class="check-c"><span class="day">Monday</span><h3>Meatloaf Plate</h3>Glazed meatloaf, mashed potatoes, green beans.<span class="price">$12.50</span></li>
  <li class="check-c"><span class="day">Tuesday</span><h3>Biscuits &amp; Gravy</h3>Two biscuits, peppery sausage gravy, two eggs.<span class="price">$9.75</span></li>
  <li class="check-c"><span class="day">Wednesday</span><h3>Patty Melt</h3>Rye, Swiss, grilled onions, fries.<span class="price">$11.25</span></li>
  <li class="check-c"><span class="day">Thursday</span><h3>Hot Turkey</h3>Open-face roast turkey, gravy, cranberry.<span class="price">$12.00</span></li>
  <li class="check-c"><span class="day">Friday</span><h3>Fish Sandwich</h3>Beer-battered cod, slaw, tartar, fries.<span class="price">$12.75</span></li>
 </ul></div></div></section>
<section class="sec dark" aria-labelledby="wk-h"><div class="wrap feature">
 {img(c,'diner_chicken','Crispy fried chicken on a golden waffle with syrup pouring over it, orange juice behind','(min-width:860px) 40vw, 100vw')}
 <div><p class="eyebrow">Weekends only</p><h2 id="wk-h">Chicken &amp; waffles, Saturday and Sunday.</h2>
 <p class="lede">Buttermilk fried chicken on a malted waffle with hot honey and warm syrup. We make 60 a day, and when they are gone, they are gone.</p>
 <div class="btn-row"><a class="btn" href="menu.html#order">Order online</a><a class="btn btn--ghost" href="menu.html">Read the whole menu</a></div></div>
</div></section>
<section class="sec" aria-label="More from Hollis Street"><div class="wrap teasers">
 <div class="tease"><p class="eyebrow">From the pie case</p><h2>Whole pies for your table.</h2><p>Baked every morning. Order a whole pie two days ahead and pick it up warm.</p><a class="link-arrow" href="pies.html">See the pies &rarr;</a></div>
 <div class="tease"><p class="eyebrow">Our story</p><h2>Same counter since 1962.</h2><p>Eight stools, one griddle, and pancake batter still mixed by hand before sunrise.</p><a class="link-arrow" href="about.html">Read our story &rarr;</a></div>
</div></section>
<section class="sec order-band" aria-labelledby="ob-h"><div class="wrap"><h2 id="ob-h">Skip the wait. Pick it up in about 15 minutes.</h2><a class="btn" href="menu.html#order">Order online</a></div></section>
"""
    P['home'] = ('index.html', 'Hollis Street Diner | Breakfast, burgers and pie in Cincinnati (sample)',
                 'Hollis Street Diner is a fictional Cincinnati diner: griddle breakfast all day, lunch plates, daily specials and whole pies. A design sample by Preferred Web Solutions.', home, 'home', '')
    # ---------------- MENU
    menu = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Printed fresh, like the one on the counter</p><h1>The menu</h1>
 <p class="lede">The favorites, typed out so they are easy to read on any phone. A real site carries the restaurant&rsquo;s full, current menu.</p>
 <ul class="jump" aria-label="Jump to a menu section"><li><a href="#order">Order online</a></li><li><a href="#breakfast">Breakfast</a></li><li><a href="#griddle">Griddle &amp; sweets</a></li><li><a href="#lunch">Lunch plates</a></li></ul></div></section>
<section class="sec" id="order" aria-labelledby="ord-h" style="padding-bottom:0"><div class="wrap">
 <h2 id="ord-h" style="font-size:clamp(1.9rem,4vw,2.8rem)">Order online, skip the wait.</h2>
 <p class="lede">Pick it up at the counter in about 15 minutes, or have it brought to you. Rather call? <a href="tel:{c['tel']}">{c['phone']}</a></p>
 <div class="order-panel"><div class="op"><h3>Pickup (demo)</h3><p>Order ahead, grab it at the counter.</p><a class="btn btn--sm" href="#" data-demo="Pickup ordering is a demo on this sample. Nothing is connected yet.">Order online</a></div>
 <div class="op"><h3>Delivery (demo)</h3><p>Through a delivery partner.</p><a class="btn btn--sm" href="#" data-demo="Delivery ordering is a demo on this sample. Nothing is connected yet.">Order online</a></div></div></div></section>
<section class="sec" aria-label="Menu"><div class="wrap">
 <div class="menu-grid">
  <div class="msec" id="breakfast"><h2>Breakfast</h2><p class="sub">Served all day, every hour we are open.</p>
   {mi('Two-Egg Plate','$8.50','Eggs any style, hash browns, toast, bacon or sausage.')}
   {mi('Corned Beef Hash','$11.00','Crispy house hash, two eggs, rye toast.')}
   {mi('Western Omelet','$10.50','Ham, peppers, onion, cheddar, hash browns.')}
   {mi('Biscuits &amp; Gravy','$8.00','Two biscuits under sausage gravy.')}</div>
  <div class="msec" id="griddle"><h2>Griddle &amp; sweets</h2><p class="sub">Add berries or chocolate chips, $1.50.</p>
   {mi('Short Stack','$7.25','Three buttermilk pancakes, whipped butter, warm syrup.')}
   {mi('Malted Waffle','$8.25','Crisp outside, soft inside, powdered sugar.')}
   {mi('French Toast','$9.00','Thick-cut challah, cinnamon, maple.')}
   {mi('Slice of Pie','$4.50','Whatever is in the case today. Add a scoop, $1.75.')}</div>
  <div class="msec" id="lunch"><h2>Lunch plates</h2><p class="sub">From 11am until close. Comes with fries or a cup of soup.</p>
   {mi('Hollis Burger','$10.50','Griddled patty, American cheese, pickles, onion.')}
   {mi('Club Sandwich','$11.75','Turkey, bacon, lettuce, tomato, triple-decker.')}
   {mi('Grilled Cheese &amp; Tomato Soup','$8.75','Sourdough, sharp cheddar, a bowl of soup.')}
   {mi('Thick Shake','$5.75','Vanilla, chocolate or strawberry.')}</div>
  <div class="msec"><h2>Weekends only</h2><p class="sub">Saturday and Sunday.</p>
   {mi('Chicken &amp; Waffles','$14.00','Buttermilk fried chicken on a malted waffle, hot honey, warm syrup. Sixty a day.')}
   {mi('Bottomless Coffee','$2.75','Refills until you wave us off.')}</div>
 </div>
 <p class="note"><b>Good to know:</b> prices and availability can change. Please tell us about any allergies before ordering.</p>
 <div class="side-photo">{img(c,'diner_booth','Fried eggs, sausage and toast beside a plate of powdered pancakes on a checkered table','(min-width:1200px) 1136px, 100vw')}</div>
</div></section>
"""
    P['menu'] = ('menu.html', 'Menu | Hollis Street Diner, Cincinnati breakfast and lunch (sample)',
                 'Breakfast served all day, griddle favorites and lunch plates at Hollis Street Diner, a fictional Cincinnati diner. Prices are invented for this design sample.', menu, 'menu', '')
    # ---------------- PIES
    pies = f"""
<section class="page-head"><div class="wrap two" style="align-items:center"><div><p class="eyebrow">From the pie case</p><h1>Whole pies for your table.</h1>
 <p class="lede">Baked every morning. Order a whole pie two days ahead and pick it up warm. Holiday dates fill up fast.</p></div>{pie_svg()}</div></section>
<section class="sec" aria-labelledby="pl-h"><div class="wrap"><h2 id="pl-h" style="font-size:clamp(1.9rem,4vw,2.8rem)">This month&rsquo;s pies</h2>
 <ul class="pies">
  <li class="pie"><h3>Dutch Apple</h3><p>Brown sugar crumb, cinnamon.</p><p class="price">$22 whole</p></li>
  <li class="pie"><h3>Sour Cherry</h3><p>Lattice top, a little tart.</p><p class="price">$24 whole</p></li>
  <li class="pie"><h3>Chocolate Cream</h3><p>Dark chocolate, whipped cream.</p><p class="price">$24 whole</p></li>
  <li class="pie"><h3>Pumpkin (fall)</h3><p>Warm spice, whipped cream.</p><p class="price">$20 whole</p></li></ul>
 <p class="note">Prices and availability can change. Please tell us about any allergies when you order.</p></div></section>
<section class="sec" style="padding-top:0"><div class="wrap two">
 <div class="panel" id="order-pie"><h2>Order a whole pie</h2>
 {form('pie-form',[('name','Name','text',True,False),('phone','Phone','tel',True,False),('date','Pickup date','date',True,False),('pie','Pie','select:Dutch Apple|Sour Cherry|Chocolate Cream|Pumpkin',True,False)],'Request my pie')}</div>
 <div class="panel"><h2>Pie of the month</h2><p>One short email a month with the new pie and holiday order dates. Unsubscribe any time.</p>
 {form('news-form',[('email','Email address','email',True,True)],'Sign me up')}</div>
</div></section>
"""
    P['pies'] = ('pies.html', 'Whole pies and pie orders | Hollis Street Diner, Cincinnati (sample)',
                 'Order a whole pie two days ahead at Hollis Street Diner, a fictional Cincinnati diner. Apple, cherry, chocolate cream and pumpkin. A design sample by Preferred Web Solutions.', pies, 'pies', '')
    # ---------------- ABOUT
    about = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Our story</p><h1>Same counter since 1962.</h1></div></section>
<section class="sec" aria-label="Our story"><div class="wrap story">
 <div><h2>Eight stools, one griddle.</h2>
 <p class="lede">Ruth Hollis opened the counter with eight stools and one griddle. Her grandson Danny runs it now, and the pancake batter is still mixed by hand before the sun comes up.</p>
 <blockquote>&ldquo;Half our regulars order before they sit down. The other half just nod, and we know.&rdquo;<cite>Danny Hollis, owner</cite></blockquote>
 <p class="invented">This story and quote are invented for the sample. On a real site, they come from the owner.</p>
 <ul class="facts"><li><b>6:02am</b>Coffee&rsquo;s on before the door unlocks.</li><li><b>60</b>Chicken &amp; waffles a day, weekends only.</li><li><b>1</b>Special a day, on a guest check.</li></ul></div>
 {img(c,'diner_stools','Row of chrome diner stools with sage green seats along a wood-paneled counter, with a white table and leather chairs','(min-width:860px) 40vw, 100vw')}
</div></section>
<section class="sec dark" aria-labelledby="gal-h"><div class="wrap"><p class="eyebrow">A morning at Hollis Street</p><h2 id="gal-h" style="font-size:clamp(1.9rem,4vw,2.8rem);margin-bottom:1.5rem">From the first pot to the last slice.</h2>
 {slideshow(c,'A morning at Hollis Street, photo slideshow',[
  ('diner_counter','Chrome condiment caddy and a white coffee cup on the diner counter','Everything within reach. Ketchup, hot sauce and a fresh cup.'),
  ('diner_pancakes','Overhead view of a buttered pancake and a plate of scrambled eggs and hash browns on a diner table','The short stack. Buttermilk batter, mixed every morning.'),
  ('diner_lamps','Glass pendant lamps hanging over the counter and kitchen shelves','Under the pendant lamps. Same counter, new neighbors every morning.'),
  ('diner_chicken','Crispy fried chicken on a golden waffle with syrup pouring over it, orange juice behind','Weekend chicken &amp; waffles. Sixty a day, until they are gone.'),
  ('diner_booth','Fried eggs, sausage and toast beside a plate of powdered pancakes on a checkered table','Booths by the window. Room for the whole family and the Sunday paper.')],'show')}
</div></section>
<section class="sec order-band" aria-labelledby="ab-h"><div class="wrap"><h2 id="ab-h">Come on in, or order ahead.</h2><a class="btn" href="menu.html#order">Order online</a></div></section>
"""
    about = about.replace("&amp;amp;", "&amp;")
    P['about'] = ('about.html', 'Our story | Hollis Street Diner, Cincinnati (sample)',
                  'The story of Hollis Street Diner, a fictional Cincinnati counter open since 1962. The story is invented for this design sample by Preferred Web Solutions.', about, 'about', '')
    # ---------------- CONTACT
    contact = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Come on in</p><h1>Find us on Hollis Street.</h1></div></section>
<section class="sec" aria-label="Hours and location"><div class="wrap two">
 <div><h2 style="font-size:1.8rem">Hours</h2>
 <table class="hours"><caption class="sr-only">Opening hours</caption><tbody><tr><th scope="row">Monday to Friday</th><td>6am to 3pm</td></tr><tr><th scope="row">Saturday</th><td>7am to 3pm</td></tr><tr><th scope="row">Sunday</th><td>7am to 2pm</td></tr></tbody></table>
 <p>Breakfast is served every hour we are open.</p>
 <h2 style="font-size:1.8rem;margin-top:1.6rem">Location</h2>
 <p>412 Hollis Street<br>Cincinnati, Ohio 45202<br>Free lot behind the building. Street parking on Hollis.</p>
 <p><a class="btn btn--ghost btn--sm" href="#" data-demo="Directions are a demo on this sample.">Get directions (demo)</a></p>
 <h2 style="font-size:1.8rem;margin-top:1.6rem">Order &amp; contact</h2>
 <p><a href="tel:{c['tel']}">{c['phone']}</a><br>Walk-ins welcome. Groups of 8 or more, please call ahead.</p>
 <p><a class="btn" href="menu.html#order">Order online</a></p>
 <p class="invented">Sample address, hours and phone number. On a real site, these are confirmed with the owner.</p></div>
 <div>{map_svg()}
 <div class="panel" style="margin-top:1.5rem"><h2>Send us a note</h2>
 {form('contact-form',[('name','Name','text',True,False),('email','Email','email',True,False),('msg','Your message','textarea',True,True)],'Send message')}</div></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="tease"><p class="eyebrow">What neighbors say</p><h2>Real reviews, straight from Google.</h2>
 <p>A real site links to the restaurant&rsquo;s own Google and Yelp pages and shows its actual star rating. We never write reviews or copy them from other sites.</p>
 <a class="btn btn--ghost btn--sm" href="#" data-demo="Reviews link is a demo on this sample.">Read reviews on Google (demo)</a></div></div></section>
"""
    P['contact'] = ('contact.html', 'Hours and location | Hollis Street Diner, Cincinnati (sample)',
                    'Hours, address and contact for Hollis Street Diner, a fictional Cincinnati diner. Sample details are invented for this design sample by Preferred Web Solutions.', contact, 'contact', '')
    return P

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else None
    CFG['dir'] = os.path.join(REPO, 'diner')
    build(CFG, pages(), CSS, out)
    print('diner built')
