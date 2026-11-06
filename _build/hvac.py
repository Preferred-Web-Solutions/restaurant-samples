import os, sys, re, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
from contractor_common import *
import roofing as R

CTA = 'Schedule service'
CTA_HREF = 'contact.html#schedule'

SERVICES = [
 dict(slug='furnaces', name='Furnace repair and install', short='Heat back on fast, or a new furnace sized right for your home.', kicker='Heating and cooling', art='furnace',
  intro='A furnace that will not light is a cold-house problem. We diagnose it, tell you what it costs to fix, and tell you honestly when replacing it is the better deal.',
  includes=['Diagnosis with the price quoted before any repair', 'Ignitor, flame sensor, blower and control board repairs', 'Gas furnace replacement with a load calculation, not a guess', 'Venting, filter and thermostat checks', 'Haul-away of the old unit', 'A test of the new system before we leave'],
  good=['A furnace past 15 years old with repeated repairs is usually worth replacing.', 'Sizing matters. Too big a furnace short-cycles and wears out sooner.', 'No-heat calls get the next open slot, with a phone line answered after hours.'],
  job=('No-heat call, 14-year-old furnace', 'Failed ignitor and dirty flame sensor. Replaced both the same visit and the furnace ran through the weekend.'), related=['maintenance-plans', 'heat-pumps', 'ductwork']),
 dict(slug='air-conditioning', name='Air conditioning', short='Repairs and replacements for central air, done before the heat wave.', kicker='Heating and cooling', art='ac',
  intro='When the house will not cool, we find out why: refrigerant, a failed capacitor, a frozen coil. We fix what is wrong and quote it first.',
  includes=['Cooling diagnosis and written repair quote', 'Capacitor, contactor, fan motor and coil repairs', 'Refrigerant leak checks', 'Central air replacement with correct sizing', 'Condensate drain cleaning', 'Thermostat setup and a walk-through'],
  good=['Replace the filter before you call. A clogged one freezes coils.', 'Book maintenance in spring. Summer slots fill up.', 'We tell you if a repair is not worth the money.'],
  job=('Frozen coil, second-floor bedrooms', 'Dirty filter and a blocked condensate drain. Cleared both, rebalanced airflow, and the room cooled within the hour.'), related=['maintenance-plans', 'heat-pumps', 'air-quality']),
 dict(slug='heat-pumps', name='Heat pumps', short='One system for heating and cooling, with lower running costs.', kicker='Heating and cooling', art='pump',
  intro='A heat pump heats and cools your home from a single outdoor unit. We tell you whether one fits your house and what it will cost to run.',
  includes=['Home assessment and sizing', 'Ducted and ductless options', 'Installation, line sets and electrical hookup', 'Thermostat and backup-heat setup', 'A plain-language walk-through of how to run it'],
  good=['Modern heat pumps work in Cincinnati winters, often with backup heat for the coldest days.', 'Ask about rebates. We will tell you which ones to check, and you apply for them.', 'Savings depend on your current fuel and electric rates. We give a range, not a promise.'],
  job=('Ductless mini-split, sunroom', 'One indoor head and one outdoor unit for a room the old furnace never heated well.'), related=['air-conditioning', 'furnaces', 'maintenance-plans']),
 dict(slug='maintenance-plans', name='Maintenance plans', short='Two tune-ups a year to catch problems before they cost you.', kicker='Care and comfort', art='tune',
  intro='A yearly check on your furnace and a yearly check on your AC is the cheapest way to avoid an emergency call. Our plan covers both.',
  includes=['One heating and one cooling tune-up each year', 'Filter change at each visit', 'Priority scheduling', 'A written checklist after every visit', 'Discounted repair labor for members'],
  good=['Plan price is shown here once the owner sets it.', 'Cancel any time. No contract trap.', 'We note small issues early so they stay small.'],
  job=('Spring AC tune-up', 'Cleaned the coil, tested the capacitor, caught a weak fan motor before July.'), related=['furnaces', 'air-conditioning', 'air-quality']),
 dict(slug='air-quality', name='Indoor air quality', short='Filters, humidity control and cleaner air in every room.', kicker='Care and comfort', art='air',
  intro='Dry winter air, stuffy bedrooms and dust that returns a day after cleaning are often system problems. We look at filtration and humidity first.',
  includes=['Upgraded media filters', 'Whole-home humidifier and dehumidifier installation', 'Duct sealing where air is leaking', 'UV and air-cleaner options, with honest limits', 'Follow-up check after a month'],
  good=['A better filter is often the cheapest fix.', 'We do not sell fear. We say what a product does and does not do.', 'Humidity between 30 and 50 percent is the usual indoor target.'],
  job=('Whole-home humidifier', 'Installed a bypass humidifier to stop winter dryness and static in a 1960s ranch.'), related=['ductwork', 'maintenance-plans', 'furnaces']),
 dict(slug='ductwork', name='Ductwork', short='Sealing, repair and new runs for rooms that never get comfortable.', kicker='Care and comfort', art='duct',
  intro='If one room is always hot or cold, the equipment may be fine and the ducts may not be. We test, seal and fix airflow.',
  includes=['Airflow and pressure testing', 'Duct sealing and insulation', 'New runs for additions and finished basements', 'Return air upgrades', 'Written findings with photos'],
  good=['Leaky ducts can waste a large share of heated or cooled air.', 'We show you the leak, not just the invoice.', 'Some fixes are small: a damper or a sealed joint.'],
  job=('Cold back bedroom', 'A disconnected duct in the crawlspace. Reconnected, sealed and insulated it, and the room caught up.'), related=['air-quality', 'furnaces', 'air-conditioning']),
]
GROUPS = [('Heating and cooling', ['furnaces', 'air-conditioning', 'heat-pumps']), ('Care and comfort', ['maintenance-plans', 'air-quality', 'duct' 'work'])]

CFG = dict(R.CFG)
CFG.update(
    slug='juniper-lane-heating-air', name='Juniper Lane Heating & Air', tagline='Furnace, air conditioning and heat pump service in the Cincinnati area.',
    kind_word='heating and cooling website', fictional_word='HVAC company',
    logo_html='<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><circle cx="17" cy="17" r="13" fill="none" stroke="#F4B03E" stroke-width="3.5"/><path d="M17 17 24 10" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><circle cx="17" cy="17" r="2.6" fill="#fff"/></svg><span>Juniper Lane <b>Heating &amp; Air</b></span>',
    phone='(513) 555-0126', tel='+15135550126', addr1='Shop: 640 Juniper Lane', addr2='Cincinnati, Ohio 45215',
    foot_loc_title='Shop', hours_short=[('Monday to Friday', '7am to 5pm'), ('Saturday', '8am to noon'), ('No-heat and no-cool calls', 'Phone answered after hours')],
    cta=CTA, cta_href=CTA_HREF,
    nav=[('home', 'Home', 'index.html'), ('services', 'Services', None), ('area', 'Service area', 'area.html'), ('about', 'About', 'about.html'), ('contact', 'Contact', 'contact.html')],
    services_menu=dict(groups=[(t, [(next(s['name'] for s in SERVICES if s['slug'] == sl), f'svc-{sl}.html') for sl in sls]) for t, sls in GROUPS], all=('All services', 'services.html')),
    social=['Facebook'],
    fonts=[('DM Serif Display', 400, 'dm-serif-display-latin-400-normal.woff2'), ('DM Sans', 400, 'dm-sans-latin-400-normal.woff2'), ('DM Sans', 500, 'dm-sans-latin-500-normal.woff2'), ('DM Sans', 700, 'dm-sans-latin-700-normal.woff2')],
    preload=['dm-serif-display-latin-400-normal.woff2', 'dm-sans-latin-400-normal.woff2'],
    services_lede='Six services, each with its own page. We quote every repair in writing before we start.',
    credit=f'Sample website designed by Preferred Web Solutions &middot; <a href="mailto:{EMAIL}">{EMAIL}</a>. Juniper Lane Heating &amp; Air is a made-up business used to show what a heating and cooling website can look like. Services, claims, address, phone number and story are invented. Illustrations are original artwork standing in for job photos. A real site shows only license numbers, warranties and years in business the owner confirms.',
    bar_tail='Illustrations stand in for job photos.',
)
GROUPS[1] = ('Care and comfort', ['maintenance-plans', 'air-quality', 'ductwork'])
CFG['services_menu']['groups'] = [(t, [(next(s['name'] for s in SERVICES if s['slug'] == sl), f'svc-{sl}.html') for sl in sls]) for t, sls in GROUPS]

# palette + type swap on roofing CSS
css = R.CSS
for a, b in [('#8F3200', '#6E4A00'), ('#B84400', '#6E4A00'), ('#FFB27A', '#F4B03E'), ('#FFE3D0', '#FBE7BE'), ('#F26B1D', '#F4B03E'),
             ('#14181B', '#14231F'), ('#2A3640', '#14403A'), ('#EEF1F2', '#F5F2EA'), ('#E1E6E9', '#E5EADF'), ('#C4CCD2', '#C9D0C4'), ('#46535C', '#44524D'),
             ('#D6DDE2', '#D9E4DE'), ('Barlow Condensed', 'DM Serif Display'), ('Source Sans 3', 'DM Sans'), ('"Arial Narrow",Impact,sans-serif', 'Georgia,serif')]:
    css = css.replace(a, b)
css = css.replace('.clip', '.dialcard')
css += r"""
h1,h2,h3,.logo,.btn,.eyebrow,.tag,.related a,.trust b{text-transform:none;letter-spacing:0;font-weight:400}
h1,h2,h3{line-height:1.05}
.btn,.eyebrow,.tag{font-family:var(--body);font-weight:700}
.btn{letter-spacing:.01em;font-size:1.05rem;border-radius:999px}
.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:.82rem}
.logo{font-size:1.25rem;font-weight:400}
.logo b{font-weight:400;font-style:italic}
.hero h1{font-size:clamp(2.8rem,7vw,5.2rem)}
.svc-card h3,.svc-row h3,.related a{font-size:1.6rem}
.trust b{font-size:1.2rem;font-family:var(--display)}
.steps li::before{font-family:var(--display);font-weight:400}
.band{background:#F4B03E}
.dialcard{transform:none;border-radius:28px;padding:2rem 1.4rem 1.6rem;text-align:center;box-shadow:0 18px 40px rgba(0,0,0,.35)}
.dialcard::before,.dialcard::after{display:none}
.dial{width:min(15rem,70%);margin:.4rem auto 1rem;display:block}
.dialcard h2{font-size:1.7rem}
.dialcard .sub{margin:.2rem 0 .4rem}
.dialcard .read{font-weight:700;display:flex;justify-content:center;gap:1.4rem;flex-wrap:wrap}
.dialcard .read span{display:flex;flex-direction:column;font-size:.85rem;color:var(--muted)}
.dialcard .read b{font-family:var(--display);font-size:2rem;font-weight:400;color:var(--ink);line-height:1}
.svc-card,.jobc,.panel,.svc-row,.job,.goodbox,.related li{border-radius:18px;border-width:1px}
.svc-card .art{border-bottom-width:1px}
.svc-art,.svc-row-art,.job-art,.area-map{border-width:1px;border-radius:14px}
.ticks li::before{border-radius:50%;border-width:0;background-color:#14403A}
.goodbox{border-left-width:1px}
blockquote{font-family:var(--display);font-weight:400;border-left-color:#F4B03E}
@media (max-width:520px){.logo{font-size:1.02rem;gap:.4rem}.logo svg{width:28px;height:28px}.logo span{white-space:normal;line-height:1.05}}
"""

def art(kind):
    sky = '#E2EBE4'; ink = '#14231F'; a = '#F4B03E'; g = '#14403A'; wh = '#fff'
    b = f'<svg viewBox="0 0 320 200" role="img" aria-label="{{}}"><rect width="320" height="200" fill="{sky}"/><rect y="170" width="320" height="30" fill="#C6D3CA"/>'
    st = f'stroke="{ink}" stroke-width="3" stroke-linejoin="round"'
    if kind == 'furnace':
        s = b + f'<rect x="100" y="40" width="120" height="130" rx="6" fill="{wh}" {st}/><rect x="116" y="58" width="88" height="40" rx="4" fill="{g}" {st}/><circle cx="160" cy="128" r="14" fill="{a}" {st}/><path d="M160 134c-6-4-4-10 0-14 4 4 6 10 0 14z" fill="{ink}"/><rect x="136" y="20" width="48" height="20" fill="#B9C7BF" {st}/>'
        return (s + '</svg>').format('Illustration of a gas furnace with a lit burner')
    if kind == 'ac':
        fan = ''.join(f'<path d="M160 100l{dx} {dy}" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>' for dx, dy in ((0, -34), (30, 18), (-30, 18)))
        s = b + f'<rect x="90" y="52" width="140" height="118" rx="10" fill="{wh}" {st}/><circle cx="160" cy="100" r="42" fill="{sky}" {st}/>' + fan + f'<circle cx="160" cy="100" r="6" fill="{a}" {st}/>'
        return (s + '</svg>').format('Illustration of an outdoor air conditioner unit with a fan')
    if kind == 'pump':
        s = b + f'<rect x="60" y="100" width="90" height="70" rx="8" fill="{wh}" {st}/><circle cx="105" cy="135" r="24" fill="{sky}" {st}/><rect x="190" y="40" width="80" height="26" rx="8" fill="{wh}" {st}/><path d="M200 56h60" stroke="{a}" stroke-width="5" stroke-linecap="round"/><path d="M150 140h30q10 0 10-10V70" fill="none" stroke="{g}" stroke-width="4"/>'
        return (s + '</svg>').format('Illustration of an outdoor heat pump connected to an indoor wall unit')
    if kind == 'tune':
        s = b + f'<rect x="100" y="30" width="120" height="140" rx="8" fill="{wh}" {st}/>' + ''.join(f'<rect x="116" y="{50+i*32}" width="16" height="16" rx="3" fill="{a if i<3 else wh}" {st}/><path d="M144 {58+i*32}h56" stroke="{ink}" stroke-width="4" stroke-linecap="round"/>' for i in range(4))
        return (s + '</svg>').format('Illustration of a maintenance checklist with three of four items checked')
    if kind == 'air':
        s = b + f'<rect x="80" y="60" width="160" height="90" rx="8" fill="{wh}" {st}/>' + ''.join(f'<path d="M96 {80+i*18}h128" stroke="{g}" stroke-width="3"/>' for i in range(4)) + ''.join(f'<path d="M{40+i*10} {40+i*28}c20 -10 30 10 50 0" fill="none" stroke="{a}" stroke-width="4" stroke-linecap="round"/>' for i in range(3))
        return (s + '</svg>').format('Illustration of an air filter with clean air flowing through it')
    s = b + f'<path d="M30 110h110v-40h80v40h70" fill="none" stroke="{g}" stroke-width="22" stroke-linejoin="round"/><path d="M30 110h110v-40h80v40h70" fill="none" stroke="{wh}" stroke-width="12" stroke-linejoin="round"/><path d="M60 110h30M170 70h30M250 110h30" stroke="{a}" stroke-width="6" stroke-linecap="round"/>'
    return (s + '</svg>').format('Illustration of ductwork running through a house')

def dial():
    return ('<svg class="dial" viewBox="0 0 200 200" role="img" aria-label="Illustration of a thermostat dial set to 70 degrees"><circle cx="100" cy="100" r="92" fill="#14403A" stroke="#14231F" stroke-width="4"/>'
            + ''.join(f'<path d="M100 14v12" stroke="#fff" stroke-width="3" stroke-linecap="round" transform="rotate({a} 100 100)"/>' for a in range(-120, 121, 30))
            + '<path d="M100 100 L100 36" stroke="#F4B03E" stroke-width="6" stroke-linecap="round" transform="rotate(35 100 100)"/><circle cx="100" cy="100" r="46" fill="#F5F2EA" stroke="#14231F" stroke-width="3"/>'
            '<text x="100" y="112" text-anchor="middle" font-family="DM Serif Display,Georgia,serif" font-size="38" fill="#14231F">70&#176;</text></svg>')

R.art = art  # reuse roofing page builders with new art
def pages():
    P = R.pages.__wrapped__() if hasattr(R.pages, '__wrapped__') else None
    return P

def build_pages():
    c = CFG; P = {}
    pick = ('furnaces', 'air-conditioning', 'maintenance-plans')
    cards = ''.join(f'<li class="svc-card"><div class="art">{art(s["art"])}</div><div class="tx"><h3>{esc(s["name"])}</h3><p>{s["short"]}</p><a class="link-arrow" href="svc-{s["slug"]}.html">Read about {esc(s["name"].lower())}<span aria-hidden="true"> &rarr;</span></a></div></li>' for s in SERVICES if s['slug'] in pick)
    jobs = ''.join(f'<li class="jobc"><div>{art(s["art"])}</div><div class="tx"><span class="tag">Sample job card</span><h3>{esc(s["job"][0])}</h3><p>{s["job"][1]}</p></div></li>' for s in SERVICES if s['slug'] in ('furnaces', 'heat-pumps', 'ductwork'))
    home = f"""
<section class="hero"><div class="wrap hero-grid">
 <div><p class="eyebrow">Heating &amp; cooling &middot; Cincinnati area</p>
 <h1>Comfortable in every season, <em>priced up front.</em></h1>
 <p class="lede">Furnace and air conditioning repair, replacement and tune-ups. You get the price in writing before we start, and a tech who explains what they found.</p>
 <div class="btn-row"><a class="btn" href="{CTA_HREF}">{CTA}</a><a class="btn btn--ghost" href="tel:{c['tel']}">Call {c['phone']}</a></div></div>
 <div class="dialcard" role="group" aria-label="Sample comfort panel">{dial()}<h2>Set it and forget it.</h2><p class="sub">A tuned-up system keeps the house steady.</p>
 <div class="read"><span><b>7am&ndash;5pm</b>Weekday service</span><span><b>After hours</b>No-heat calls</span></div></div>
</div></section>
<div class="trust"><div class="wrap"><ul>
 <li><b>Upfront pricing</b>Written quote before any repair.</li><li><b>Licensed &amp; insured*</b>License number shown once the owner provides it.</li>
 <li><b>Tune-up plans</b>Two visits a year, heating and cooling.</li><li><b>Clean work</b>Shoe covers, drop cloths, tidy van.</li></ul>
 <small>*Sample claims for a fictional company. A real site shows only what the owner confirms.</small></div></div>
<section class="sec" aria-labelledby="sv-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Services</p><h2 id="sv-h">Heating, cooling and the air in between.</h2></div>
 <ul class="svc-cards">{cards}</ul><p style="margin-top:1.6rem"><a class="link-arrow" href="services.html">See all six services &rarr;</a></p></div></section>
<section class="sec dark" aria-labelledby="pr-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">How a visit goes</p><h2 id="pr-h">Four steps, no pressure.</h2></div>
 <ol class="steps"><li><h3>Schedule</h3><p>Pick a window. We call when the tech is on the way.</p></li><li><h3>Diagnose</h3><p>The tech finds the cause and shows you.</p></li><li><h3>Quote</h3><p>You see the price and the options before any work starts.</p></li><li><h3>Fix</h3><p>We repair, test the system, and clean up.</p></li></ol></div></section>
<section class="sec" aria-labelledby="jb-h"><div class="wrap"><div class="sec-head"><p class="eyebrow">Recent work</p><h2 id="jb-h">Jobs from the last few months.</h2><p class="invented">Sample job cards with illustrations. Real photos from the owner go here.</p></div><ul class="jobs">{jobs}</ul></div></section>
<section class="sec sec--soft"><div class="wrap two"><div class="panel"><p class="eyebrow">Where we work</p><h2>Cincinnati and the towns around it.</h2><p>Blue Ash, Mason, Loveland, Anderson, Colerain and more. If you are not sure we cover you, ask.</p><a class="link-arrow" href="area.html">See the service area &rarr;</a></div>
 <div class="panel"><p class="eyebrow">Reviews</p><h2>Your neighbors, in their words.</h2><p>A real site links to the company&rsquo;s own Google and Facebook reviews and shows its actual rating. We never write reviews or copy them from other sites.</p><a class="btn btn--ghost btn--sm" style="color:var(--ink)" href="#" data-demo="Reviews link is a demo on this sample.">Read reviews on Google (demo)</a></div></div></section>
<section class="sec band" aria-labelledby="cb-h"><div class="wrap"><h2 id="cb-h">Is your system ready for the season?</h2><a class="btn" href="{CTA_HREF}">{CTA}</a></div></section>
"""
    P['home'] = ('index.html', 'Juniper Lane Heating & Air | Furnace and AC service in Cincinnati (sample)', 'Juniper Lane Heating & Air is a fictional Cincinnati-area company: furnace and air conditioning repair, heat pumps and tune-up plans. A design sample by Preferred Web Solutions.', home, 'home', '')
    P['services'] = ('services.html', 'Heating and cooling services | Juniper Lane Heating & Air (sample)', 'Furnace, air conditioning, heat pump, maintenance plan, air quality and ductwork services from Juniper Lane Heating & Air, a fictional Cincinnati company.', services_overview(c, GROUPS, SERVICES, art, CTA, CTA_HREF), 'services', '')
    for s in SERVICES:
        P['svc-' + s['slug']] = (f'svc-{s["slug"]}.html', f'{s["name"]} in Cincinnati | Juniper Lane Heating & Air (sample)', f'{s["name"]} from Juniper Lane Heating & Air, a fictional Cincinnati-area company. {s["short"]} A design sample by Preferred Web Solutions.', service_page(c, s, SERVICES, art, CTA, CTA_HREF), 'svc-' + s['slug'], '')
    tm = [('Mason', 380, 70), ('Loveland', 480, 120), ('Blue Ash', 360, 150), ('Anderson', 470, 230), ('Cincinnati', 300, 250), ('Colerain', 150, 190), ('Fairfield', 190, 90), ('Springdale', 250, 140)]
    P['area'] = ('area.html', 'Service area | Juniper Lane Heating & Air, Cincinnati (sample)', 'The Cincinnati-area towns served by Juniper Lane Heating & Air, a fictional company. A design sample by Preferred Web Solutions.',
                 area_page(c, tm, R.TOWNS_ALL, 'Schematic map of the Cincinnati area showing the towns served, with the service area shaded', lambda t, l: area_map(t, l, '#F4B03E', '#14231F', '#14231F', '#F5F2EA'), CTA, CTA_HREF,
                           'We service homes in Cincinnati and the towns around it. Not on the list? Ask. We will tell you straight whether we can get there.', 'Service area and towns are sample details. A real site lists the towns the owner confirms.'), 'area', '')
    about = f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('About',None)])}<p class="eyebrow">About us</p><h1>A small shop that explains what it finds.</h1></div></section>
<section class="sec"><div class="wrap two">
 <div><h2 style="font-size:clamp(2rem,4vw,3rem);margin-bottom:1rem">Why we started.</h2><p class="lede">Maria Okafor spent ten years as a service tech and kept hearing the same thing: &ldquo;Nobody told me what was wrong.&rdquo; She started Juniper Lane to show customers the problem, quote the price first, and let them decide.</p>
 <blockquote>&ldquo;If a repair is not worth it, we will tell you, and we will tell you what is.&rdquo;<cite>Maria Okafor, owner</cite></blockquote>
 <p class="invented">The owner, story and quote are invented for this sample. On a real site, they come from the owner.</p></div>
 <div class="panel"><h2>How we work</h2><ul class="ticks"><li>Diagnosis first, with photos.</li><li>A written quote before any repair.</li><li>Options, not pressure.</li><li>Shoe covers and a tidy van.</li><li>A test of the system before we leave.</li></ul>
 <p style="margin-top:1.2rem"><a class="btn" href="{CTA_HREF}">{CTA}</a></p></div></div></section>
"""
    P['about'] = ('about.html', 'About | Juniper Lane Heating & Air, Cincinnati (sample)', 'The owner and the way Juniper Lane Heating & Air, a fictional Cincinnati company, works. The story is invented for this design sample.', about, 'about', '')
    contact = f"""
<section class="svc-head"><div class="wrap">{crumbs([('Home','index.html'),('Contact',None)])}<p class="eyebrow">Contact</p><h1>Schedule a visit.</h1><p class="lede">Tell us what is going on. We will call to set a time. Or call <a href="tel:{c['tel']}">{c['phone']}</a>.</p></div></section>
<section class="sec"><div class="wrap two">
 <div class="panel" id="schedule"><h2>{CTA}</h2>
 {form('sched-form',[('name','Name','text',True,False),('phone','Phone','tel',True,False),('email','Email','email',False,False),('town','Town','text',True,False),('issue','What do you need?','select:No heat|No cooling|A tune-up|A new system quote|Not sure',True,True),('msg','Anything else we should know?','textarea',False,True)],CTA)}</div>
 <div><h2 style="font-size:1.9rem">Hours</h2><table class="hours"><caption class="sr-only">Hours</caption><tbody><tr><th scope="row">Monday to Friday</th><td>7am to 5pm</td></tr><tr><th scope="row">Saturday</th><td>8am to noon</td></tr><tr><th scope="row">No-heat and no-cool calls</th><td>Phone answered after hours</td></tr></tbody></table>
 <h2 style="font-size:1.9rem;margin-top:1.6rem">Shop</h2><p>640 Juniper Lane<br>Cincinnati, Ohio 45215<br><a href="tel:{c['tel']}">{c['phone']}</a></p>
 <p class="invented">Sample address, hours and phone number. License number: shown here once the owner provides it.</p></div></div></section>
"""
    P['contact'] = ('contact.html', 'Contact and scheduling | Juniper Lane Heating & Air (sample)', 'Schedule service with Juniper Lane Heating & Air, a fictional Cincinnati-area company. Sample details are invented for this design sample.', contact, 'contact', '')
    return P

if __name__ == '__main__':
    out = os.path.join(REPO, 'contractors')
    d = build(CFG, build_pages(), css, out)
    src = '/tmp/claude-0/-home-claude/24020632-5365-5511-b200-acc6842a5608/scratchpad/fontsrc/node_modules/@fontsource'
    os.makedirs(os.path.join(d, 'fonts'), exist_ok=True)
    for fam, w, f in CFG['fonts']:
        pkg = f.rsplit('-latin', 1)[0]
        shutil.copy(os.path.join(src, pkg, 'files', f), os.path.join(d, 'fonts', f))
    for pkg in ('dm-serif-display', 'dm-sans'):
        shutil.copy(os.path.join(src, pkg, 'LICENSE'), os.path.join(d, 'fonts', f'LICENSE-{pkg}.txt'))
    print('hvac built')
