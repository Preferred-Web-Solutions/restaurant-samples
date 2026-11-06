import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

CFG = dict(
    slug='zafiro', name='Cantina Zafiro', tagline='Tacos, tamales & margaritas.',
    logo_html='<span style="display:inline-grid;place-items:center;width:2.1rem;height:2.1rem;border-radius:50%;background:#F4A300;color:#1D1B4D;font-size:.9rem;margin-right:.1rem" aria-hidden="true">CZ</span>Cantina Zafiro',
    phone='(513) 555-0163', tel='+15135550163', addr1='1207 Mercado Street', addr2='Cincinnati, Ohio 45202',
    hours_short=[('Tue to Thu', '11am to 9pm'), ('Fri & Sat', '11am to 11pm'), ('Sun', '10am to 8pm')],
    cta='Order online', cta_href='menu.html#order', menu_label='Navigate',
    nav=[('home', 'Home', 'index.html'), ('menu', 'Menu & drinks', 'menu.html'), ('catering', 'Catering & parties', 'catering.html'), ('about', 'About', 'about.html'), ('contact', 'Visit', 'contact.html')],
    order_dropdown=[('Pickup (demo)', 'Ready in about 20 minutes', 'Pickup ordering is a demo on this sample. Nothing is connected yet.'),
                    ('Delivery (demo)', 'Through a delivery partner', 'Delivery ordering is a demo on this sample. Nothing is connected yet.')],
    social=['Instagram', 'TikTok'],
    fonts=[('Rozha One', 400, 'rozha-one-400-normal.woff2'), ('Karla', 400, 'karla-400-normal.woff2'), ('Karla', 700, 'karla-700-normal.woff2'), ('Karla', 800, 'karla-800-normal.woff2')],
    preload=['rozha-one-400-normal.woff2', 'karla-400-normal.woff2'],
    credit=f'Sample website designed by Preferred Web Solutions &middot; <a href="mailto:{EMAIL}">{EMAIL}</a>. Cantina Zafiro is a made-up business used to show what a restaurant site can look like. Menu, prices, hours, address and story are invented. Photos are for demonstration only.',
    cannot_do='You cannot order food, book the back room or buy anything here.',
)

CSS = r"""
:root{--bg:#FFF3DC;--surface:#FFFFFF;--soft:#FBE6BE;--ink:#1D1B4D;--muted:#4A4870;--line:#E7D6B4;--magenta:#C2185B;--marigold:#F4A300;--teal:#0A7480;--lime:#8CC63F;--focus:#C2185B;
--display:"Rozha One","Playfair Display",Georgia,serif;--body:"Karla","Trebuchet MS",system-ui,sans-serif;--radius:14px;--banner-bg:#1D1B4D;--banner-ink:#FFF3DC;
--btn-bg:#C2185B;--btn-ink:#fff;--head-bg:#1D1B4D;--head-ink:#FFF3DC;--head-line:rgba(255,255,255,.2);--foot-bg:#1D1B4D;--foot-ink:#FFF3DC}
.site-header :focus-visible,.site-footer :focus-visible,.dark :focus-visible,.callbar :focus-visible{outline-color:#FFC94D}
.site-header .logo{color:#FFF3DC}
.site-header .btn{border-color:#FFF3DC}
h1,h2{font-family:var(--display);font-weight:400;line-height:1.04}
.eyebrow{font-weight:800;font-size:.82rem;letter-spacing:.14em;text-transform:uppercase;color:var(--magenta);margin:0 0 .8rem}
.dark .eyebrow{color:#FFC94D}
.lede{font-size:clamp(1.1rem,2vw,1.3rem);max-width:34rem}
.hero{padding-top:clamp(2rem,5vw,4rem);padding-bottom:clamp(3rem,6vw,5rem);overflow:hidden}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:center}
.hero h1{font-size:clamp(2.6rem,6.6vw,5rem);margin-bottom:1.1rem}
.hero h1 em{font-style:normal;color:var(--magenta)}
.btn-row{display:flex;flex-wrap:wrap;gap:.8rem;margin-top:1.4rem}
.btn-row .btn--ghost{color:var(--ink)}
.deck{position:relative;min-height:27rem}
.lcard{position:absolute;width:min(14rem,46%);background:#fff;border:3px solid var(--ink);border-radius:14px;padding:.5rem;box-shadow:6px 6px 0 var(--ink)}
.lcard img{width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:8px}
.lcard .lab{display:flex;justify-content:space-between;align-items:baseline;gap:.4rem;padding:.4rem .2rem 0;font-weight:800;font-size:.95rem}
.lcard .lab span:first-child{font-family:var(--display);font-weight:400;font-size:1.05rem}
.lcard:nth-child(1){left:2%;top:6%;transform:rotate(-6deg);background:#FFE9B8}
.lcard:nth-child(2){left:27%;top:0;transform:rotate(2deg);z-index:2;background:#CBEAEE}
.lcard:nth-child(3){right:1%;top:14%;transform:rotate(7deg);background:#F9CFE0}
@media (max-width:860px){.hero-grid{grid-template-columns:minmax(0,1fr)}.deck{min-height:20rem}.lcard{width:min(10.5rem,34%)}.lcard .lab span:last-child{display:none}.lcard .lab span:first-child{font-size:.9rem}}
.strip{background:var(--teal);color:#fff}
.strip ul{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem 2rem;list-style:none;padding:1.1rem 0}
.strip li{display:flex;flex-direction:column}
.strip b{font-size:.78rem;letter-spacing:.14em;text-transform:uppercase}
.strip a{font-weight:800;display:inline-flex;align-items:center;min-height:44px}
@media (max-width:640px){.strip ul{grid-template-columns:minmax(0,1fr);gap:.2rem}.strip li{flex-direction:row;gap:.8rem;align-items:center;min-height:44px}}
.sec-head{max-width:40rem;margin-bottom:2.2rem}
.sec-head h2{font-size:clamp(2rem,5vw,3.4rem)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(18.5rem,1fr));gap:1.4rem;list-style:none}
.mcard{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);box-shadow:6px 6px 0 var(--ink);overflow:hidden;display:flex;flex-direction:column}
.mcard .ph{position:relative}
.mcard .ph img{width:100%;aspect-ratio:4/3;object-fit:cover}
.mcard .no{position:absolute;left:.7rem;top:.7rem;background:var(--marigold);color:var(--ink);border:2px solid var(--ink);border-radius:999px;padding:.1rem .7rem;font-weight:800;font-size:.85rem}
.mcard .tx{padding:1rem 1.1rem 1.2rem;display:flex;flex-direction:column;gap:.25rem;flex:1}
.mcard h3{font-family:var(--display);font-weight:400;font-size:1.5rem}
.mcard p{margin:0;color:var(--muted)}
.mcard .meta{display:flex;justify-content:space-between;gap:1rem;margin-top:auto;padding-top:.7rem;font-weight:800}
.dark{background:var(--ink);color:#FFF3DC}
.dark .btn{--btn-bg:#F4A300;--btn-ink:#1D1B4D;border-color:#F4A300}
.dark .btn--ghost{--btn-bg:transparent;background:transparent;color:#FFF3DC;border-color:#FFF3DC}
.feature{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(1.5rem,5vw,4.5rem);align-items:center}
.feature img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--radius);border:3px solid #FFF3DC}
.feature h2{font-size:clamp(2rem,5vw,3.3rem);margin-bottom:1rem}
.feature ul{margin:1rem 0 1.4rem 1.2rem}.feature li{margin-bottom:.3rem}
@media (max-width:860px){.feature{grid-template-columns:minmax(0,1fr)}}
.band{background:var(--magenta);color:#fff}
.band .wrap{display:flex;flex-wrap:wrap;gap:1.2rem 2rem;align-items:center;justify-content:space-between}
.band h2{font-size:clamp(1.9rem,4.5vw,3rem);max-width:20ch}
.band .btn{--btn-bg:#fff;--btn-ink:#8a0f40;border-color:#fff}
.band :focus-visible{outline-color:#fff}
.page-head{background:var(--marigold);border-bottom:3px solid var(--ink);padding-top:clamp(2.2rem,5vw,3.8rem);padding-bottom:clamp(2rem,4vw,3rem)}
.page-head h1{font-size:clamp(2.4rem,6vw,4.2rem);margin-bottom:.7rem}
.page-head .eyebrow{color:var(--ink)}
.page-head .lede{margin:0}
.jump{display:flex;flex-wrap:wrap;gap:.5rem;list-style:none;margin-top:1.3rem}
.jump a{display:inline-flex;align-items:center;min-height:44px;padding:0 1rem;border:2px solid var(--ink);border-radius:999px;font-weight:800;text-decoration:none;background:#fff}
.jump a:hover{background:var(--ink);color:#fff}
.order-panel{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin-top:1.6rem}
.op{border:3px solid var(--ink);border-radius:var(--radius);background:#fff;padding:1.3rem;display:flex;flex-direction:column;gap:.5rem;align-items:flex-start;box-shadow:5px 5px 0 var(--ink)}
.op h3{font-size:1.2rem;font-weight:800}.op p{margin:0}
@media (max-width:640px){.order-panel{grid-template-columns:minmax(0,1fr)}}
.more{list-style:none;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 3rem}
.more li{display:flex;justify-content:space-between;gap:1rem;padding:.8rem 0;border-bottom:2px dotted var(--ink)}
.more b{display:block}.more span{color:var(--muted)}
@media (max-width:760px){.more{grid-template-columns:minmax(0,1fr)}}
.drinks{display:grid;grid-template-columns:repeat(auto-fill,minmax(17rem,1fr));gap:1rem;list-style:none}
.drink{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:1rem 1.1rem}
.drink h3{font-family:var(--display);font-weight:400;font-size:1.35rem;display:flex;justify-content:space-between;gap:1rem}
.drink p{margin:.3rem 0 0;color:var(--muted)}
.note{margin-top:2rem;padding:1rem 1.2rem;border-left:6px solid var(--teal);background:#fff}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(1.5rem,4vw,3.5rem);align-items:start}
@media (max-width:860px){.two{grid-template-columns:minmax(0,1fr)}}
.panel{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:clamp(1.2rem,3vw,2rem);box-shadow:6px 6px 0 var(--ink)}
.panel h2{font-size:clamp(1.7rem,3.5vw,2.3rem);margin-bottom:.6rem}
.pkgs{list-style:none;display:grid;gap:.8rem;margin:1.2rem 0}
.pkgs li{background:#fff;border:3px solid var(--ink);border-radius:var(--radius);padding:1rem 1.1rem}
.pkgs b{font-family:var(--display);font-weight:400;font-size:1.3rem;display:block}
.story-img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:var(--radius);border:3px solid var(--ink)}
blockquote{margin:1.6rem 0;padding:0 0 0 1.2rem;border-left:6px solid var(--magenta);font-size:1.35rem;font-weight:700;line-height:1.35}
blockquote cite{display:block;font-size:.95rem;font-style:normal;margin-top:.5rem}
.invented{font-size:.9rem;color:var(--muted);font-style:italic}
.loteria{width:min(100%,17rem);height:auto;justify-self:center}
.slide-stage{border:3px solid #FFF3DC}
.slide figcaption{background:#fff;color:var(--ink);font-weight:700}
.dark .slide-ctrl button{color:#FFF3DC}
.dark .slide-ctrl ol button[aria-current="true"]{background:#F4A300;color:#1D1B4D;border-color:#F4A300}
.hours{width:100%;border-collapse:collapse;margin:.6rem 0 1rem}
.hours th,.hours td{text-align:left;padding:.55rem 0;border-bottom:2px dotted var(--ink)}
.hours td{text-align:right;font-weight:800}
"""

def lot_svg():
    return ('<svg class="loteria" viewBox="0 0 200 290" role="img" aria-label="Illustrated loteria card number 27, El Zafiro, a blue gem with sun rays">'
            '<rect x="6" y="6" width="188" height="278" rx="16" fill="#FFE9B8" stroke="#1D1B4D" stroke-width="5"/><rect x="18" y="18" width="164" height="254" rx="10" fill="none" stroke="#C2185B" stroke-width="3"/>'
            '<text x="30" y="52" font-family="Karla,sans-serif" font-weight="800" font-size="20" fill="#1D1B4D">No. 27</text>'
            '<g stroke="#F4A300" stroke-width="6" stroke-linecap="round"><path d="M100 70V44"/><path d="M60 88L42 70"/><path d="M140 88L158 70"/><path d="M44 130H18"/><path d="M156 130H182"/></g>'
            '<polygon points="100,78 150,112 100,208 50,112" fill="#0A7480" stroke="#1D1B4D" stroke-width="5" stroke-linejoin="round"/><polygon points="50,112 150,112 100,78" fill="#46A9B5" stroke="#1D1B4D" stroke-width="4" stroke-linejoin="round"/><path d="M100 112V208M75 112L100 208M125 112L100 208" stroke="#1D1B4D" stroke-width="3" fill="none"/>'
            '<text x="100" y="250" text-anchor="middle" font-family="Rozha One,Georgia,serif" font-size="24" fill="#1D1B4D">EL ZAFIRO</text></svg>')

def mcard(no, kind, imgname, alt, name, desc, qty, price, c):
    return (f'<li class="mcard"><div class="ph">{img(c,imgname,alt,"(min-width:900px) 24vw, (min-width:600px) 45vw, 100vw")}<span class="no">No. {no} &middot; {kind}</span></div>'
            f'<div class="tx"><h3>{name}</h3><p>{desc}</p><div class="meta"><span>{qty}</span><span>{price}</span></div></div></li>')

def more(n, d, p): return f'<li><div><b>{n}</b><span>{d}</span></div><b>{p}</b></li>'
def drink(n, d, p): return f'<li class="drink"><h3><span>{n}</span><span>{p}</span></h3><p>{d}</p></li>'

def pages():
    c = CFG; P = {}
    A = dict(
     pastor='Al pastor tacos topped with onion and cilantro on a wooden board, with red salsa and lime',
     crispy='Three crispy chicken tacos with lettuce, crema and salsa in a metal rack',
     soft='Soft flour tacos filled with chicken, tomato, lettuce and avocado',
     dorados='Golden fried tacos topped with cabbage, radish and crumbled cheese on a wooden board',
     asada='Steak and avocado tacos in a rack with pickled red onions',
     chil='Chilaquiles in red salsa topped with a fried egg, cotija and cilantro, with beans and green crema')
    home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div><p class="eyebrow">Family kitchen &middot; Cincinnati, Ohio</p>
 <h1>Tacos, tamales &amp; <em>agua fresca</em>, made fresh.</h1>
 <p class="lede">Corn tortillas pressed to order, salsas made every morning, and a margarita list that goes way past lime.</p>
 <div class="btn-row"><a class="btn" href="menu.html#order">Order online</a><a class="btn btn--ghost" href="menu.html">See the menu</a></div></div>
 <div class="deck" role="group" aria-label="Three favorites from the menu">
  <div class="lcard">{img(c,'zaf_pastor',A['pastor'],'(min-width:860px) 15vw, 30vw',eager=True)}<div class="lab"><span>Al Pastor</span><span>No. 1</span></div></div>
  <div class="lcard">{img(c,'zaf_crispy',A['crispy'],'(min-width:860px) 15vw, 30vw',eager=True)}<div class="lab"><span>Pollo Crujiente</span><span>No. 2</span></div></div>
  <div class="lcard">{img(c,'zaf_dorados',A['dorados'],'(min-width:860px) 15vw, 30vw',eager=True)}<div class="lab"><span>Dorados</span><span>No. 4</span></div></div>
 </div></div></section>
<div class="strip"><div class="wrap"><ul><li><b>Open</b><span>Tue to Sun from 11am</span></li><li><b>Find us</b><span>1207 Mercado Street, Cincinnati</span></li><li><b>Call</b><a href="tel:{c['tel']}">{c['phone']}</a></li></ul></div></div>
<section class="sec" aria-labelledby="el-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Elige tu carta</p><h2 id="el-h">Pick a card. Every one is a plate.</h2>
 <p class="lede">Our favorites, dealt like a loter&iacute;a game. Every taco comes on fresh corn tortillas unless you ask for flour.</p></div>
 <ul class="cards">
 {mcard(5,'Plato','zaf_asada',A['asada'],'Carne Asada','Grilled steak, avocado, pickled red onion, salsa macha.','Three tacos','$14.50',c)}
 {mcard(3,'Taco','zaf_soft',A['soft'],'Pollo Suave','Soft flour tortilla, chicken, tomato, lettuce, avocado.','Three tacos','$10.50',c)}
 {mcard(6,'Desayuno','zaf_chilaquiles',A['chil'],'Chilaquiles','Tortilla chips in red salsa, a fried egg, queso fresco, beans.','Weekends until 2pm','$12.00',c)}</ul>
 <p style="margin-top:2rem"><a class="btn btn--ghost" style="color:var(--ink)" href="menu.html">See all the cards</a></p></div></section>
<section class="sec dark" aria-labelledby="cat-h"><div class="wrap feature">
 {img(c,'zaf_pastor',A['pastor'],'(min-width:860px) 45vw, 100vw')}
 <div><p class="eyebrow">Catering</p><h2 id="cat-h">A taco bar for your next event.</h2><p class="lede">We bring the comal, the salsas and the cooks. Office lunches, graduations and backyard parties, from 20 to 200 guests.</p>
 <div class="btn-row"><a class="btn" href="catering.html">Plan my catering</a></div></div></div></section>
<section class="sec band" aria-labelledby="ob-h"><div class="wrap"><h2 id="ob-h">Come hungry. Pickup in about 20 minutes.</h2><a class="btn" href="menu.html#order">Order online</a></div></section>
"""
    P['home'] = ('index.html', 'Cantina Zafiro | Tacos, tamales and margaritas in Cincinnati (sample)',
                 'Cantina Zafiro is a fictional Cincinnati family kitchen serving tacos pressed to order, tamales, agua fresca and margaritas. A design sample by Preferred Web Solutions.', home, 'home', '')
    menu = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Elige tu carta</p><h1>Menu &amp; drinks</h1><p class="lede">Every taco comes on fresh corn tortillas unless you ask for flour. A real site carries the full, current menu.</p>
 <ul class="jump" aria-label="Jump to a section"><li><a href="#order">Order online</a></li><li><a href="#cartas">Tacos &amp; plates</a></li><li><a href="#mas">M&aacute;s del men&uacute;</a></li><li><a href="#bebidas">Bebidas</a></li></ul></div></section>
<section class="sec" id="order" style="padding-bottom:0" aria-labelledby="o-h"><div class="wrap"><h2 id="o-h" style="font-size:clamp(1.9rem,4vw,2.8rem)">Order online.</h2><p class="lede">Pickup in about 20 minutes, or delivery through a partner. Rather call? <a href="tel:{c['tel']}">{c['phone']}</a></p>
 <div class="order-panel"><div class="op"><h3>Pickup (demo)</h3><p>Ready in about 20 minutes.</p><a class="btn btn--sm" href="#" data-demo="Pickup ordering is a demo on this sample. Nothing is connected yet.">Order online</a></div>
 <div class="op"><h3>Delivery (demo)</h3><p>Through a delivery partner.</p><a class="btn btn--sm" href="#" data-demo="Delivery ordering is a demo on this sample. Nothing is connected yet.">Order online</a></div></div></div></section>
<section class="sec" id="cartas" aria-labelledby="c-h"><div class="wrap"><div class="sec-head"><h2 id="c-h">Tacos &amp; plates</h2></div><ul class="cards">
 {mcard(1,'Taco','zaf_pastor',A['pastor'],'Al Pastor','Marinated pork, pineapple, onion, cilantro, lime.','Three tacos','$11.50',c)}
 {mcard(2,'Taco','zaf_crispy',A['crispy'],'Pollo Crujiente','Crispy tortilla, grilled chicken, lettuce, crema, salsa roja.','Three tacos','$11.00',c)}
 {mcard(3,'Taco','zaf_soft',A['soft'],'Pollo Suave','Soft flour tortilla, chicken, tomato, lettuce, avocado.','Three tacos','$10.50',c)}
 {mcard(4,'Antojito','zaf_dorados',A['dorados'],'Tacos Dorados','Fried golden, cabbage, radish, cotija, lime and salsa.','Plate of three','$12.00',c)}
 {mcard(5,'Plato','zaf_asada',A['asada'],'Carne Asada','Grilled steak, avocado, pickled red onion, salsa macha.','Three tacos','$14.50',c)}
 {mcard(6,'Desayuno','zaf_chilaquiles',A['chil'],'Chilaquiles','Tortilla chips in red salsa, a fried egg, queso fresco, beans.','Weekends until 2pm','$12.00',c)}</ul></div></section>
<section class="sec" id="mas" style="padding-top:0" aria-labelledby="m-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">M&aacute;s del men&uacute;</p><h2 id="m-h">And everything else.</h2></div><ul class="more">
 {more('Tamales','Red pork or poblano &amp; cheese, with crema','$9.50')}{more('Elote','Grilled corn, lime crema, cotija, chile','$5')}{more('Guacamole','Made when you order, with warm chips','$9')}{more('Enchiladas verdes','Chicken, tomatillo salsa, rice, black beans','$14.50')}{more('Salsa bar','Roja, verde, macha and habanero, free with any order','Free')}{more('Para los ni&ntilde;os','Cheese quesadilla with rice','$6')}{more('Churros','Cinnamon sugar, chocolate for dipping','$6')}</ul></div></section>
<section class="sec dark" id="bebidas" aria-labelledby="b-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Bebidas</p><h2 id="b-h">Way past the lime.</h2><p class="lede">Fresh-squeezed and shaken to order. Every margarita can be made without alcohol.</p></div><ul class="drinks" style="color:var(--ink)">
 {drink('House Margarita','Blanco tequila, fresh lime, agave. Rocks or up.','$10')}{drink('Tamarindo','Tamarind, chile-salt rim, reposado.','$12')}{drink('Paloma','Grapefruit, lime, soda, a pinch of salt.','$11')}{drink('Agua Fresca','Hibiscus, horchata or watermelon.','$4')}{drink('Mexican Hot Chocolate','Cinnamon and a little heat.','$5')}</ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><p class="note"><b>Good to know:</b> prices and availability can change. Please tell us about any allergies before ordering.</p></div></section>
"""
    P['menu'] = ('menu.html', 'Menu and drinks | Cantina Zafiro, Cincinnati tacos and margaritas (sample)',
                 'Tacos, tamales, antojitos and margaritas at Cantina Zafiro, a fictional Cincinnati family kitchen. Prices are invented for this design sample.', menu, 'menu', '')
    cat = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Catering &amp; parties</p><h1>Taco bar, tamales, and the back room.</h1><p class="lede">We bring the comal, the salsas and the cooks. Office lunches, graduations and backyard parties, from 20 to 200 guests.</p></div></section>
<section class="sec" aria-label="Catering"><div class="wrap two">
 <div>{img(c,'zaf_asada',A['asada'],'(min-width:860px) 45vw, 100vw',style='border-radius:14px;border:3px solid #1D1B4D;aspect-ratio:4/3;object-fit:cover;width:100%')}
 <ul class="pkgs"><li><b>Build-your-own taco bar</b>Two proteins, tortillas, salsas and toppings.</li><li><b>Trays of tamales, rice and beans</b>Red pork or poblano &amp; cheese.</li><li><b>Agua fresca by the gallon</b>Hibiscus, horchata or watermelon.</li><li><b>The back room</b>Seats 40, with its own margarita pitcher service.</li></ul></div>
 <div class="panel"><h2>Tell us about your event</h2><p>Tell us about your event and we will call you back.</p>
 {form('cat-form',[('name','Name','text',True,False),('phone','Phone','tel',True,False),('type','What are you planning?','select:Catering delivered to me|Party in the back room',True,True),('msg','Date and guest count','textarea',False,True)],'Plan my catering')}</div>
</div></section>
"""
    P['catering'] = ('catering.html', 'Catering and parties | Cantina Zafiro, Cincinnati (sample)',
                     'Taco bar catering for 20 to 200 guests and a 40-seat back room at Cantina Zafiro, a fictional Cincinnati restaurant. A design sample by Preferred Web Solutions.', cat, 'catering', '')
    about = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Nuestra historia</p><h1>Recipes from our family table.</h1></div></section>
<section class="sec" aria-label="Our story"><div class="wrap two" style="align-items:center">
 <div><p class="lede">The Zafiro family brought their recipes from Puebla in 1998 and sold tamales from a cooler on Saturday mornings. The cantina opened in 2011, and the tortilla press has not stopped since.</p>
 <blockquote>&ldquo;If the tortilla is not fresh, nothing else matters.&rdquo;<cite>Lupe Zafiro, owner</cite></blockquote>
 <p class="invented">Family, story and quote are invented for this sample. On a real site, they come from the owner.</p></div>
 {lot_svg()}</div></section>
<section class="sec dark" aria-labelledby="g-h"><div class="wrap"><p class="eyebrow">La galer&iacute;a</p><h2 id="g-h" style="font-size:clamp(1.9rem,4vw,2.8rem);margin-bottom:1.5rem">Fresh off the comal.</h2>
 {slideshow(c,'Fresh off the comal, photo slideshow',[('zaf_soft',A['soft'],'Pollo suave.'),('zaf_chilaquiles',A['chil'],'Weekend chilaquiles.'),('zaf_dorados',A['dorados'],'Tacos dorados.'),('zaf_asada',A['asada'],'Carne asada.'),('zaf_crispy',A['crispy'],'Pollo crujiente.')],'show')}</div></section>
<section class="sec band" aria-labelledby="ab-h"><div class="wrap"><h2 id="ab-h">Come hungry.</h2><a class="btn" href="menu.html#order">Order online</a></div></section>
"""
    P['about'] = ('about.html', 'Our story | Cantina Zafiro, Cincinnati family kitchen (sample)',
                  'The story of Cantina Zafiro, a fictional Cincinnati family kitchen. The family and story are invented for this design sample by Preferred Web Solutions.', about, 'about', '')
    contact = f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Ven a comer</p><h1>Come hungry.</h1></div></section>
<section class="sec" aria-label="Hours and location"><div class="wrap two">
 <div><h2 style="font-size:1.9rem">Hours</h2>
 <table class="hours"><caption class="sr-only">Opening hours</caption><tbody><tr><th scope="row">Tuesday to Thursday</th><td>11am to 9pm</td></tr><tr><th scope="row">Friday &amp; Saturday</th><td>11am to 11pm</td></tr><tr><th scope="row">Sunday</th><td>10am to 8pm</td></tr><tr><th scope="row">Monday</th><td>Closed</td></tr></tbody></table>
 <h2 style="font-size:1.9rem;margin-top:1.6rem">Location</h2><p>1207 Mercado Street<br>Cincinnati, Ohio 45202<br>Free parking lot next door.</p>
 <p><a class="btn btn--ghost btn--sm" style="color:var(--ink)" href="#" data-demo="Directions are a demo on this sample.">Get directions (demo)</a></p>
 <h2 style="font-size:1.9rem;margin-top:1.6rem">Order</h2><p><a href="tel:{c['tel']}">{c['phone']}</a><br>Pickup in about 20 minutes, or delivery through a partner.</p><p><a class="btn" href="menu.html#order">Order online</a></p>
 <p class="invented">Sample address, hours and phone number. On a real site, these are confirmed with the owner.</p></div>
 <div><div class="panel"><h2>Send us a note</h2>{form('contact-form',[('name','Name','text',True,False),('email','Email','email',True,False),('msg','Your message','textarea',True,True)],'Send message')}</div>
 <div class="panel" style="margin-top:1.6rem"><h2>Taco Tuesday list</h2><p>One email a week with the Tuesday special and new margaritas. Unsubscribe any time.</p>{form('news-form',[('email','Email address','email',True,True)],'Join the list')}</div></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="panel"><p class="eyebrow">Lo que dicen</p><h2>Real reviews from real neighbors.</h2><p>A real site links to the restaurant&rsquo;s own Google and Yelp pages and shows its actual star rating. We never write reviews or copy them from other sites.</p>
 <a class="btn btn--ghost btn--sm" style="color:var(--ink)" href="#" data-demo="Reviews link is a demo on this sample.">Read reviews on Google (demo)</a></div></div></section>
"""
    P['contact'] = ('contact.html', 'Hours and location | Cantina Zafiro, Cincinnati (sample)',
                    'Hours, address and contact for Cantina Zafiro, a fictional Cincinnati family kitchen. Sample details are invented for this design sample.', contact, 'contact', '')
    return P

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else None
    CFG['dir'] = os.path.join(REPO, 'zafiro')
    build(CFG, pages(), CSS, out)
    print('zafiro built')
