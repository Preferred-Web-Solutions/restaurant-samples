"""Shared framework for the PWS sample sites (restaurants and contractors).
Each site module defines CFG + PAGES and calls build(). Output goes to <repo>/<slug>/ (or an alternate root).
"""
import os, re, html, shutil, json
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "preferredwebsolutions@gmail.com"
DATE = "November 5, 2026"
VERSION = "1.1"
FORMSPREE = "https://formspree.io/f/xgavryzg"

# ---------------------------------------------------------------- base CSS
BASE_CSS = r"""
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;text-size-adjust:100%;scroll-padding-top:calc(var(--sb-h) + var(--hd-h) + 12px)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
:root{--sb-h:36px;--hd-h:72px;--callbar:0px;--wrap:1200px;--sec:clamp(3rem,7vw,6rem)}
body{margin:0;padding-top:var(--sb-h);background:var(--bg);color:var(--ink);font-family:var(--body);font-size:1.0625rem;line-height:1.6}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-underline-offset:3px}
button,input,select,textarea{font:inherit;color:inherit}
h1,h2,h3,h4{margin:0;text-wrap:balance}
p{margin:0 0 1em}
ul{margin:0;padding:0}
:focus-visible{outline:3px solid var(--focus);outline-offset:3px}
.sr-only{position:absolute!important;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.skip{position:absolute;left:12px;top:-100px;z-index:300;background:var(--ink);color:var(--bg);padding:.75rem 1rem;font-weight:700;text-decoration:none;border-radius:6px;min-height:44px}
.skip:focus{top:calc(var(--sb-h) + 8px)}
.wrap{width:100%;max-width:var(--wrap);margin-left:auto;margin-right:auto;padding-left:20px;padding-right:20px}
@media (min-width:768px){.wrap{padding-left:32px;padding-right:32px}}
.sec{padding-top:var(--sec);padding-bottom:var(--sec)}
.sample-bar{position:fixed;top:0;left:0;right:0;z-index:200;height:var(--sb-h);display:flex;align-items:center;justify-content:center;background:var(--banner-bg);color:var(--banner-ink);font-size:.8rem;line-height:1.25;text-align:center;padding:0 12px}
.sb-short{display:none}
@media (max-width:640px){.sb-long,.sb-lead{display:none}.sb-short{display:inline}.sample-bar{font-size:.8rem;font-weight:600}}
/* header */
.site-header{position:sticky;top:var(--sb-h);z-index:100;height:var(--hd-h);background:var(--head-bg,var(--bg));color:var(--head-ink,var(--ink));border-bottom:1px solid var(--head-line,var(--line))}
.site-header .bar{height:100%;display:flex;align-items:center;justify-content:space-between;gap:1rem}
.logo{white-space:nowrap;display:inline-flex;align-items:center;gap:.6rem;min-height:44px;text-decoration:none;font-family:var(--display);font-size:1.45rem;line-height:1}
.nav{display:flex;align-items:center;gap:.25rem}
.nav a:not(.btn){display:inline-flex;align-items:center;min-height:44px;padding:0 .8rem;text-decoration:none;font-weight:600;font-size:.97rem}
.nav a:not(.btn):hover{text-decoration:underline;text-decoration-thickness:2px}
.nav a[aria-current="page"]{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:8px}
.menu-btn{display:none;align-items:center;gap:.5rem;min-height:44px;min-width:44px;padding:.3rem .85rem;border:2px solid currentColor;background:transparent;border-radius:var(--radius);cursor:pointer;font-weight:700}
.menu-btn i,.menu-btn i::before,.menu-btn i::after{display:block;width:18px;height:2px;background:currentColor;position:relative;content:""}
.menu-btn i::before{position:absolute;top:-6px}.menu-btn i::after{position:absolute;top:6px}
.nav-end{display:flex;align-items:center;gap:.5rem}
@media (max-width:520px){.logo{font-size:1.2rem}.logo-sfx{display:none}}
@media (max-width:980px){
 .menu-btn{display:inline-flex}
 .nav{position:absolute;top:100%;left:0;right:0;display:none;flex-direction:column;align-items:stretch;gap:0;background:var(--head-bg,var(--bg));border-bottom:1px solid var(--head-line,var(--line));padding:.5rem 20px 1rem;box-shadow:0 12px 24px rgba(0,0,0,.12)}
 .nav.open{display:flex}
 .nav a:not(.btn){padding:0 .25rem;min-height:48px;border-bottom:1px solid var(--head-line,var(--line))}
 .site-header .bar>.btn,.site-header .bar>.dd{display:none}
 .nav .m-cta{display:block;margin-top:.9rem}
}
@media (min-width:981px){.nav .m-cta{display:none}}
/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:.5rem;min-height:48px;padding:.55rem 1.35rem;border:2px solid var(--btn-bg);background:var(--btn-bg);color:var(--btn-ink);border-radius:var(--btn-radius,var(--radius));font-weight:800;font-size:1rem;line-height:1.2;text-decoration:none;cursor:pointer;text-align:center}
.btn:hover{background:var(--btn-hover,var(--btn-bg));filter:brightness(1.08)}
.btn--ghost{background:transparent;color:inherit;border-color:currentColor}
.btn--ghost:hover{background:rgba(127,127,127,.14);filter:none}
.btn--sm{min-height:44px;padding:.35rem 1rem;font-size:.95rem}
.link-arrow{display:inline-flex;align-items:center;min-height:44px;font-weight:700}
/* dropdown */
.dd{position:relative}
.dd-menu{position:absolute;right:0;top:calc(100% + 8px);min-width:17rem;margin:0;padding:.4rem;list-style:none;background:var(--surface);color:var(--ink);border:2px solid var(--ink);border-radius:var(--radius);box-shadow:0 14px 30px rgba(0,0,0,.2);z-index:120}
.dd-menu a{display:block;padding:.65rem .8rem;min-height:44px;text-decoration:none;border-radius:calc(var(--radius) - 2px)}
.dd-menu a:hover{background:var(--soft,rgba(0,0,0,.06))}
.dd-menu b{display:block}.dd-menu span{font-size:.88rem;color:var(--muted)}
.dd-btn::after{content:"";width:.5rem;height:.5rem;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.dd-btn[aria-expanded="true"]::after{transform:rotate(225deg)}
/* footer */
.site-footer{background:var(--foot-bg,var(--ink));color:var(--foot-ink,var(--bg));padding-top:3.5rem;padding-bottom:2rem}
.foot-grid{display:grid;grid-template-columns:minmax(0,1.3fr) repeat(3,minmax(0,1fr));gap:2.25rem}
@media (max-width:900px){.foot-grid{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
@media (max-width:560px){.foot-grid{grid-template-columns:minmax(0,1fr)}}
.site-footer h2{font-family:var(--body);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;font-weight:800;margin-bottom:.8rem;opacity:.85}
.site-footer p,.site-footer li{margin:0 0 .35rem;list-style:none}
.site-footer a{display:inline-flex;align-items:center;min-height:44px}
.foot-name{font-family:var(--display);font-size:1.7rem;line-height:1.1;margin-bottom:.6rem}
.foot-legal{margin-top:2.25rem;padding-top:1.25rem;border-top:1px solid rgba(255,255,255,.25)}
.foot-legal ul{display:flex;flex-wrap:wrap;gap:0 1.25rem}
.foot-legal button{background:none;border:0;padding:0;min-height:44px;cursor:pointer;text-decoration:underline;text-underline-offset:3px;color:inherit}
.credit{font-size:.88rem;opacity:.9;margin-top:1rem;max-width:62rem}
/* call bar */
.callbar{display:none}
@media (max-width:720px){
 :root{--callbar:4.5rem}
 body{padding-bottom:var(--callbar)}
 .callbar{display:flex;gap:.6rem;position:fixed;left:0;right:0;bottom:0;z-index:150;background:var(--ink);padding:.6rem 16px calc(.6rem + env(safe-area-inset-bottom,0px));box-shadow:0 -1px 0 rgba(255,255,255,.2)}
 .callbar .btn{flex:1;min-height:48px;font-size:.98rem;padding:.4rem .6rem}
 .callbar .btn--call{flex:0 0 auto;background:transparent;color:#fff;border-color:#fff}
}
/* consent */
.consent{position:fixed;right:16px;bottom:16px;z-index:260;width:min(26rem,calc(100% - 32px))}
.consent-card{background:#fff;color:#14161a;border:2px solid #14161a;border-radius:12px;padding:1rem 1.1rem;box-shadow:0 18px 40px rgba(0,0,0,.28)}
.consent-card h2{font-family:var(--body);font-size:1.05rem;font-weight:800;margin-bottom:.35rem}
.consent-card p{font-size:.9rem;line-height:1.5;margin:0 0 .5rem}
.consent-card a{color:#0b4f9c}
.consent-prefs{margin:.5rem 0;display:grid;gap:.4rem}
.consent-prefs label{display:flex;gap:.6rem;align-items:flex-start;font-size:.88rem;min-height:44px}
.consent-prefs input{margin-top:.25rem;width:20px;height:20px;flex:0 0 auto}
.consent-prefs b{display:block}
.consent-btns{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.6rem}
.consent-btns .cbtn{flex:1 1 auto;min-height:44px;padding:.4rem .9rem;border-radius:8px;border:2px solid #14161a;background:#14161a;color:#fff;font-weight:700;cursor:pointer;font-size:.92rem}
.consent-btns .cbtn.alt{background:#fff;color:#14161a}
@media (max-width:720px){.consent{left:10px;right:10px;width:auto;bottom:calc(var(--callbar) + 10px)}.consent-card{padding:.8rem .9rem}.consent-card p{font-size:.84rem;line-height:1.4}.consent-btns{gap:.4rem;margin-top:.4rem}.consent-btns .cbtn{font-size:.88rem;padding:.3rem .5rem}}
/* slideshow */
.slides{position:relative}
.slide-stage{position:relative;overflow:hidden;border-radius:var(--radius);background:#000}
.slide{display:none;margin:0}
.slide.on{display:block}
.slide img{width:100%;aspect-ratio:16/10;object-fit:cover}
.slide figcaption{padding:.8rem 1rem;font-size:.98rem}
.slide-ctrl{display:flex;flex-wrap:wrap;align-items:center;gap:.6rem;margin-top:.8rem}
.slide-ctrl button{min-height:44px;min-width:44px;padding:.3rem .9rem;border:2px solid currentColor;background:transparent;border-radius:var(--radius);cursor:pointer;font-weight:700}
.slide-ctrl ol{display:flex;gap:.4rem;list-style:none;margin:0;padding:0}
.slide-ctrl ol button[aria-current="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
/* forms */
.form-grid{display:grid;gap:1rem;grid-template-columns:repeat(2,minmax(0,1fr))}
@media (max-width:600px){.form-grid{grid-template-columns:minmax(0,1fr)}}
.field{display:grid;gap:.35rem;min-width:0}
.field.full{grid-column:1/-1}
.field label{font-weight:700;font-size:.95rem}
.field input,.field select,.field textarea{width:100%;min-height:48px;padding:.6rem .8rem;border:2px solid var(--ink);border-radius:var(--radius);background:#fff;color:#14161a}
.field textarea{min-height:7.5rem;resize:vertical}
.hint{font-size:.9rem;color:var(--muted)}
.demo-note{display:inline-block;font-size:.82rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:.15rem .55rem;border:2px solid currentColor;border-radius:999px;margin-bottom:.8rem}
.form-status{min-height:1.5em;font-weight:700;margin:.8rem 0 0}
.toast{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(var(--callbar) + 18px);z-index:280;max-width:min(32rem,calc(100% - 32px));background:#14161a;color:#fff;padding:.8rem 1.1rem;border-radius:10px;font-weight:600;box-shadow:0 12px 30px rgba(0,0,0,.35)}
/* legal */
.simple-head{background:var(--ink);color:var(--bg)}
.simple-head .bar{display:flex;align-items:center;justify-content:space-between;gap:1rem;min-height:var(--hd-h)}
.simple-head a{display:inline-flex;align-items:center;min-height:44px;font-weight:700}
.doc{max-width:48rem;padding-top:3rem;padding-bottom:4rem}
.doc h1{font-family:var(--display);font-size:clamp(2rem,5vw,3rem);line-height:1.1;margin-bottom:.5rem}
.doc h2{font-family:var(--body);font-size:1.3rem;font-weight:800;margin:2rem 0 .6rem}
.doc .meta{color:var(--muted);font-size:.95rem}
.doc ul{padding-left:1.3rem}.doc li{margin-bottom:.4rem}
.doc a{color:inherit;font-weight:600}
.table-wrap{overflow-x:auto}
.table-wrap table{border-collapse:collapse;min-width:36rem;width:100%;font-size:.95rem}
.table-wrap th,.table-wrap td{text-align:left;vertical-align:top;border:1px solid var(--line);padding:.55rem .65rem}
.doc .confirm{padding:1.2rem;border:2px solid var(--ink);border-radius:var(--radius);background:var(--surface);margin-top:1rem}
.doc .btn{margin-top:.5rem}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
"""

SITE_JS = r"""/* Shared sample-site script. No cookies, no storage except the consent choice, no third-party requests. */
(function(){
  var hdr=document.querySelector('.site-header'),btn=document.querySelector('.menu-btn'),nav=document.getElementById('site-nav');
  function setNav(o,refocus){if(!nav||!btn)return;nav.classList.toggle('open',o);btn.setAttribute('aria-expanded',o?'true':'false');if(!o&&refocus)btn.focus()}
  if(btn&&nav){
    btn.addEventListener('click',function(){setNav(!nav.classList.contains('open'),false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&nav.classList.contains('open'))setNav(false,true)});
    document.addEventListener('click',function(e){if(nav.classList.contains('open')&&!hdr.contains(e.target))setNav(false,false)});
    hdr.addEventListener('focusout',function(e){var t=e.relatedTarget;if(t&&!hdr.contains(t))setNav(false,false)});
    window.addEventListener('resize',function(){if(window.innerWidth>980)setNav(false,false)});
  }
  /* dropdowns (Order online) */
  document.querySelectorAll('.dd').forEach(function(dd){
    var b=dd.querySelector('.dd-btn'),m=dd.querySelector('.dd-menu');if(!b||!m)return;
    function set(o,rf){m.hidden=!o;b.setAttribute('aria-expanded',o?'true':'false');if(!o&&rf)b.focus()}
    b.addEventListener('click',function(){set(m.hidden,false)});
    dd.addEventListener('keydown',function(e){if(e.key==='Escape'&&!m.hidden){set(false,true)}});
    document.addEventListener('click',function(e){if(!m.hidden&&!dd.contains(e.target))set(false,false)});
    dd.addEventListener('focusout',function(e){var t=e.relatedTarget;if(t&&!dd.contains(t))set(false,false)});
  });
  /* demo links and forms announce honestly */
  var toast=null,tt=null;
  function say(msg){
    var live=document.getElementById('demo-live');if(live){live.textContent='';setTimeout(function(){live.textContent=msg},30)}
    if(!toast){toast=document.createElement('div');toast.className='toast';toast.setAttribute('aria-hidden','true');document.body.appendChild(toast)}
    toast.textContent=msg;toast.hidden=false;clearTimeout(tt);tt=setTimeout(function(){toast.hidden=true},4500);
  }
  document.querySelectorAll('[data-demo]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();say(a.getAttribute('data-demo')||'This is a demo link. It is not connected yet.')})});
  document.querySelectorAll('form[data-demo-form]').forEach(function(f){
    var st=f.querySelector('.form-status');
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var bad=f.querySelector(':invalid');
      if(bad){st.textContent='Please fill in the required fields. '+(bad.labels&&bad.labels[0]?'Start with: '+bad.labels[0].textContent.replace(/\(required\)/,'').trim()+'.':'');bad.focus();return}
      st.textContent='This is a working demo and is not connected yet, so nothing was sent.';
    });
  });
  /* slideshows */
  document.querySelectorAll('.slides').forEach(function(root){
    var slides=[].slice.call(root.querySelectorAll('.slide')),nums=[].slice.call(root.querySelectorAll('.slide-ctrl ol button')),
        prev=root.querySelector('[data-prev]'),next=root.querySelector('[data-next]'),pp=root.querySelector('[data-pp]'),stage=root.querySelector('.slide-stage'),
        i=0,timer=null,playing=false,reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function show(n){i=(n+slides.length)%slides.length;slides.forEach(function(s,k){s.classList.toggle('on',k===i)});nums.forEach(function(b,k){if(k===i)b.setAttribute('aria-current','true');else b.removeAttribute('aria-current')})}
    function play(){if(playing)return;playing=true;pp.textContent='Pause';pp.setAttribute('aria-pressed','false');stage.setAttribute('aria-live','off');timer=setInterval(function(){show(i+1)},7000)}
    function pause(user){playing=false;clearInterval(timer);pp.textContent='Play';pp.setAttribute('aria-pressed','true');stage.setAttribute('aria-live','polite')}
    prev.addEventListener('click',function(){show(i-1)});next.addEventListener('click',function(){show(i+1)});
    nums.forEach(function(b,k){b.addEventListener('click',function(){show(k)})});
    pp.addEventListener('click',function(){playing?pause():play()});
    root.addEventListener('mouseenter',function(){if(playing){clearInterval(timer)}});
    root.addEventListener('mouseleave',function(){if(playing){clearInterval(timer);timer=setInterval(function(){show(i+1)},7000)}});
    root.addEventListener('focusin',function(){if(playing){clearInterval(timer)}});
    root.addEventListener('focusout',function(){if(playing){clearInterval(timer);timer=setInterval(function(){show(i+1)},7000)}});
    show(0);if(reduce)pause();else play();
  });
  /* report form posts to Formspree */
  var rf=document.getElementById('report-form');
  if(rf){
    var st=rf.querySelector('.form-status'),conf=document.getElementById('report-confirm');
    rf.addEventListener('submit',function(e){
      e.preventDefault();
      var msg=rf.querySelector('#r-msg');
      if(!msg.value.trim()){st.textContent='Please tell us what happened before sending.';msg.focus();return}
      st.textContent='Sending...';
      var fd=new FormData(rf);
      fetch(rf.action,{method:'POST',body:fd,headers:{'Accept':'application/json'}}).then(function(r){
        if(!r.ok)throw new Error('bad');
        rf.hidden=true;conf.hidden=false;var h=conf.querySelector('h2');h.focus();
      }).catch(function(){st.textContent='Sorry, that did not send. Please email '+rf.getAttribute('data-email')+' instead.'});
    });
  }
  /* a new page opens at the top, except Back/Forward or a #hash link */
  function top(){window.scrollTo(0,0);document.documentElement.scrollTop=0}
  try{
    var nt=performance.getEntriesByType&&performance.getEntriesByType('navigation')[0],back=nt&&nt.type==='back_forward';
    if(!location.hash&&!back){
      if('scrollRestoration' in history)history.scrollRestoration='manual';
      top();document.addEventListener('DOMContentLoaded',top);
      window.addEventListener('load',function(){top();setTimeout(top,60)});
    }
    window.addEventListener('pageshow',function(e){if(!e.persisted&&!location.hash&&!back)top()});
  }catch(e){}
})();
"""

CONSENT_JS = r"""/* Consent banner. This site sets no cookies and loads no analytics or marketing scripts.
   The only thing stored is the visitor's own choice, in localStorage under "pws-consent". */
(function(){
  var KEY='pws-consent',VERSION='1.0';
  function read(){try{var v=JSON.parse(localStorage.getItem(KEY)||'null');return v&&v.v===VERSION?v:null}catch(e){return null}}
  function save(a,m){try{localStorage.setItem(KEY,JSON.stringify({v:VERSION,ts:new Date().toISOString(),analytics:!!a,marketing:!!m}))}catch(e){}}
  var root=document.createElement('div');root.className='consent';root.hidden=true;
  root.innerHTML=
   '<div class="consent-card" role="dialog" aria-labelledby="consent-title">'+
   '<h2 id="consent-title" tabindex="-1">Cookie choices</h2>'+
   '<p id="consent-text">This site stores one small item in your browser to remember this choice. It does not use analytics, advertising or tracking tools. If any are added later, they only load if you accept. <a href="cookies.html">Read the Cookie Policy</a></p>'+
   '<div class="consent-prefs" id="consent-prefs" hidden>'+
    '<label><input type="checkbox" checked disabled><span><b>Essential</b>Remembers this choice. Always on.</span></label>'+
    '<label><input type="checkbox" id="c-an"><span><b>Analytics</b>Not used on this site today.</span></label>'+
    '<label><input type="checkbox" id="c-mk"><span><b>Marketing</b>Not used on this site today.</span></label>'+
   '</div>'+
   '<div class="consent-btns"><button type="button" class="cbtn" id="c-all">Accept all</button><button type="button" class="cbtn" id="c-rej">Reject non-essential</button><button type="button" class="cbtn alt" id="c-man" aria-expanded="false" aria-controls="consent-prefs">Manage choices</button></div>'+
   '</div>';
  var opener=null;
  function show(focus){var s=read();root.querySelector('#c-an').checked=!!(s&&s.analytics);root.querySelector('#c-mk').checked=!!(s&&s.marketing);root.hidden=false;
    if(focus){var p=root.querySelector('#consent-prefs'),m=root.querySelector('#c-man');p.hidden=false;m.setAttribute('aria-expanded','true');m.textContent='Save choices';root.querySelector('#consent-title').focus()}}
  function hide(){root.hidden=true;if(opener){try{opener.focus()}catch(e){}opener=null}}
  function init(){
    var skip=document.querySelector('.skip');
    if(skip&&skip.parentNode===document.body)document.body.insertBefore(root,skip.nextSibling);else document.body.insertBefore(root,document.body.firstChild);
    var prefs=root.querySelector('#consent-prefs'),man=root.querySelector('#c-man');
    function reset(){prefs.hidden=true;man.setAttribute('aria-expanded','false');man.textContent='Manage choices'}
    root.querySelector('#c-all').addEventListener('click',function(){save(true,true);reset();hide()});
    root.querySelector('#c-rej').addEventListener('click',function(){save(false,false);reset();hide()});
    man.addEventListener('click',function(){
      if(prefs.hidden){prefs.hidden=false;man.setAttribute('aria-expanded','true');man.textContent='Save choices'}
      else{save(root.querySelector('#c-an').checked,root.querySelector('#c-mk').checked);reset();hide()}
    });
    root.addEventListener('keydown',function(e){if(e.key==='Escape'&&read()){reset();hide()}});
    document.querySelectorAll('[data-cookie-settings]').forEach(function(b){b.addEventListener('click',function(){opener=b;show(true)})});
    if(!read())show(false);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
"""

# ---------------------------------------------------------------- helpers
def esc(s): return html.escape(s, quote=True)

_dims = {}
def dims(site_dir, name):
    key = (site_dir, name)
    if key not in _dims:
        p = os.path.join(site_dir, 'img', f'{name}-1600.jpg')
        with Image.open(p) as im: _dims[key] = im.size
    return _dims[key]

def img(cfg, name, alt, sizes="100vw", cls="", eager=False, style=""):
    w, h = dims(cfg['dir'], name)
    attrs = f'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    st = f' style="{style}"' if style else ''
    return (f'<img{c}{st} src="img/{name}-800.jpg" srcset="img/{name}-800.jpg 800w, img/{name}-1600.jpg 1600w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}" {attrs}>')

def slideshow(cfg, label, items, sid):
    """items: [(imgname, alt, caption)]"""
    figs = ''.join(
        f'<figure class="slide{" on" if k == 0 else ""}">{img(cfg, n, a, "(min-width:1000px) 1000px, 100vw")}<figcaption>{c}</figcaption></figure>'
        for k, (n, a, c) in enumerate(items))
    nums = ''.join(f'<li><button type="button"><span class="sr-only">Photo </span>{k+1}</button></li>' for k in range(len(items)))
    return (f'<div class="slides" role="group" aria-roledescription="carousel" aria-label="{esc(label)}">'
            f'<div class="slide-stage" aria-live="off">{figs}</div>'
            f'<div class="slide-ctrl"><button type="button" data-prev>Previous</button><button type="button" data-next>Next</button>'
            f'<ol aria-label="Choose a photo">{nums}</ol><button type="button" data-pp aria-pressed="false">Pause</button></div></div>')

def form(fid, fields, button, note="Working demo. Not connected yet."):
    """fields: list of (id,label,type,required,full,extra) ; type 'textarea' or 'select:opt|opt' or input type"""
    out = [f'<form id="{fid}" data-demo-form novalidate><span class="demo-note">{esc(note)}</span><div class="form-grid">']
    for f in fields:
        id_, label, typ, req, full = f[:5]
        r = ' required aria-required="true"' if req else ''
        lab = f'{esc(label)}' + (' <span class="hint">(required)</span>' if req else '')
        cls = 'field full' if full else 'field'
        if typ == 'textarea': ctl = f'<textarea id="{fid}-{id_}" name="{id_}"{r}></textarea>'
        elif typ.startswith('select:'):
            opts = ''.join(f'<option>{esc(o)}</option>' for o in typ[7:].split('|'))
            ctl = f'<select id="{fid}-{id_}" name="{id_}"{r}>{opts}</select>'
        else:
            ac = {'email': 'email', 'tel': 'tel'}.get(typ, 'off')
            ctl = f'<input id="{fid}-{id_}" name="{id_}" type="{typ}"{r} autocomplete="{ac if id_ not in ("name",) else "name"}">'
        out.append(f'<div class="{cls}"><label for="{fid}-{id_}">{lab}</label>{ctl}</div>')
    out.append(f'</div><button class="btn" type="submit" style="margin-top:1.1rem">{esc(button)}</button><p class="form-status" role="status" aria-live="polite"></p></form>')
    return ''.join(out)

LEGAL = [('privacy', 'Privacy Policy'), ('terms', 'Terms & Conditions'), ('cookies', 'Cookie Policy'),
         ('accessibility', 'Accessibility statement'), ('report', 'Report a website issue')]

def legal_body(key, cfg):
    n = cfg['name']; kind = cfg.get('kind_word', 'restaurant'); fict = cfg.get('fictional_word', 'restaurant')
    meta = f'<p class="meta">Version {VERSION} &middot; Last updated {DATE}</p>'
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    if key == 'privacy':
        return f"""<h1>Privacy Policy</h1>{meta}
<p>This Privacy Policy explains what information this website collects and how it is used. {esc(n)} is a fictional {fict}. This site is a design sample made by Preferred Web Solutions (PWS), and PWS is responsible for it.</p>
<h2>What this site collects</h2>
<p><b>Your cookie choice.</b> When you choose an option in the cookie banner, your choice, the date and the policy version are saved in your own browser (local storage). It is not sent to us. See the <a href="cookies.html">Cookie Policy</a>.</p>
<p><b>Demo forms.</b> The forms on this sample are demos. They are not connected, and nothing you type in them is sent anywhere.</p>
<p><b>Website issue reports.</b> If you use the <a href="report.html">Report a website issue</a> form, what you enter (your message, the page, and your name and email if you choose to give them) is sent to PWS through Formspree, a form-processing service. Formspree processes it on our behalf under its own privacy policy. We use it only to fix the problem and reply to you.</p>
<p><b>Hosting.</b> The company that hosts this site may keep standard server logs (such as IP address, browser type and the time of a request) for security and reliability. We do not use those logs to identify you.</p>
<h2>What this site does not do</h2>
<p>This site does not use analytics, advertising pixels, social media trackers or third-party fonts. It does not sell or share personal information.</p>
<h2>Your choices and rights</h2>
<p>Depending on where you live, you may have rights to ask what personal information we hold about you, to correct it, or to have it deleted. To make a request, email {mail}. We will reply within 30 days. You can change your cookie choice at any time with the Cookie settings button at the bottom of every page.</p>
<h2>Children</h2>
<p>This site is not aimed at children under 13, and we do not knowingly collect their information.</p>
<h2>Changes to this policy</h2>
<p>If this policy changes, we will update the version number and date above. If the change affects cookies, the site will ask for your choice again.</p>
<h2>Contact</h2>
<p>Preferred Web Solutions, {mail}.</p>"""
    if key == 'terms':
        return f"""<h1>Terms &amp; Conditions</h1>{meta}
<p>By using this website you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>This is a sample site</h2>
<p>{esc(n)} is a fictional {fict} created by Preferred Web Solutions (PWS) to show what a {kind} website can look like. The {cfg.get('invented_list','menu, prices, hours, address, phone number and story')} are invented. {cfg.get('cannot_do','You cannot order food, make a reservation, book an event or buy anything here.')} Buttons for those actions are clearly marked as demos.</p>
<h2>Content</h2>
<p>The design and written content of this site belong to PWS. {cfg.get('photo_terms','Photos are used for demonstration only.')} You may view and share links to this page, but please do not copy the site's design, text or images for other use without permission.</p>
<h2>No warranties</h2>
<p>This site is provided as it is, for demonstration. We try to keep it working and accessible but do not promise that it will always be available or free of errors.</p>
<h2>Limitation of liability</h2>
<p>To the extent the law allows, PWS is not responsible for any loss that comes from using or relying on this sample site.</p>
<h2>Links</h2>
<p>This site does not link to outside websites except where a button is clearly marked as a demo.</p>
<h2>Changes and contact</h2>
<p>We may update these terms and will change the version and date above when we do. Questions: {mail}.</p>"""
    if key == 'cookies':
        return f"""<h1>Cookie Policy</h1>{meta}
<p>This page lists everything this website stores in your browser, and every outside service it contacts. It was checked against the site's actual behavior on {DATE}.</p>
<h2>What is stored</h2>
<div class="table-wrap" tabindex="0" role="region" aria-label="Stored items table"><table>
<thead><tr><th scope="col">Name</th><th scope="col">Type</th><th scope="col">Purpose</th><th scope="col">Category</th><th scope="col">How long</th><th scope="col">Set by</th></tr></thead>
<tbody><tr><td><code>pws-consent</code></td><td>Local storage</td><td>Remembers your cookie choice, the date you made it and the policy version, so the banner does not keep appearing.</td><td>Essential</td><td>Until you clear your browser data, or until this policy's version changes</td><td>This site</td></tr></tbody>
</table></div>
<p>This site sets <b>no cookies</b>. It does not use analytics, advertising, social media or other tracking tools, in any category. Fonts and images are served from this site itself, so no outside font or image services are contacted when you load a page.</p>
<h2>Outside services</h2>
<p>The only outside service is Formspree, which receives a report only when you submit the <a href="report.html">Report a website issue</a> form. Nothing is sent to Formspree when you simply visit a page.</p>
<h2>Changing or withdrawing your choice</h2>
<p>Use the <b>Cookie settings</b> button at the bottom of any page to see or change your choice. If we ever add analytics or marketing tools, they will stay off unless you accept them, and this page will list them first.</p>
<h2>Clearing stored data in your browser</h2>
<ul>
<li><b>Chrome:</b> Settings, Privacy and security, Delete browsing data, then choose Cookies and other site data.</li>
<li><b>Safari (Mac):</b> Settings, Privacy, Manage Website Data, then remove this site.</li>
<li><b>Safari (iPhone):</b> Settings, Apps, Safari, Advanced, Website Data, then remove this site.</li>
<li><b>Firefox:</b> Settings, Privacy &amp; Security, Cookies and Site Data, Manage Data.</li>
<li><b>Edge:</b> Settings, Privacy, search and services, Clear browsing data.</li>
</ul>
<h2>Contact</h2>
<p>{mail}</p>"""
    if key == 'accessibility':
        return f"""<h1>Accessibility statement</h1>{meta}
<p>This website was built with accessibility in mind. Our goal is for everyone, including people who use screen readers, keyboards, magnification or other assistive technology, to be able to use it.</p>
<h2>What we did</h2>
<ul>
<li>We aimed for the Web Content Accessibility Guidelines (WCAG) 2.1, level AA.</li>
<li>{cfg.get('a11y_text','Menus, prices and hours are real text, not pictures or PDFs.')}</li>
<li>{cfg.get('a11y_img','Photos have text descriptions.')} Text has strong color contrast.</li>
<li>Everything works with a keyboard, with a visible focus outline and a "Skip to content" link.</li>
<li>Slideshows can be paused, and motion is reduced if your device asks for it.</li>
<li>The page still works when zoomed to 200%.</li>
<li>Each page was checked with the axe automated accessibility checker and by tabbing through it by hand.</li>
</ul>
<h2>Known limits</h2>
<p>Automated tools find only some problems, so we do not claim the site is fully compliant. If something does not work for you, we want to know.</p>
<h2>Tell us about a problem</h2>
<p>Use the <a href="report.html">Report a website issue</a> form or email {mail}. We will look into it and reply if you leave contact details.</p>"""
    if key == 'report':
        return f"""<h1>Report a website issue</h1>{meta}
<p>Found something broken, hard to read or hard to use? Tell us here. Name and email are optional; add them if you would like a reply.</p>
<form id="report-form" action="{FORMSPREE}" method="POST" novalidate data-email="{EMAIL}">
 <input type="hidden" name="business" value="Sample site: {esc(n)}">
 <input type="hidden" name="_subject" value="Website issue: {esc(n)} (sample)">
 <div class="form-grid">
 <div class="field full"><label for="r-type">What kind of problem?</label>
  <select id="r-type" name="issue_type"><option>Something is broken</option><option>Hard to read or use (accessibility)</option><option>Wrong or outdated information</option><option>Privacy question</option><option>Something else</option></select></div>
 <div class="field full"><label for="r-msg">What happened? <span class="hint">(required)</span></label>
  <textarea id="r-msg" name="message" required aria-required="true" aria-describedby="r-msg-hint"></textarea>
  <span class="hint" id="r-msg-hint">Include the page and what you were trying to do.</span></div>
 <div class="field full"><label for="r-page">Page address (optional)</label><input id="r-page" name="page" type="text" inputmode="url" autocomplete="off"></div>
 <div class="field"><label for="r-name">Your name (optional)</label><input id="r-name" name="name" type="text" autocomplete="name"></div>
 <div class="field"><label for="r-email">Your email (optional, for a reply)</label><input id="r-email" name="email" type="email" autocomplete="email"></div>
 </div>
 <button class="btn" type="submit" style="margin-top:1.1rem">Send report</button>
 <p class="form-status" role="status" aria-live="polite"></p>
</form>
<div id="report-confirm" class="confirm" hidden>
 <h2 tabindex="-1">Thank you, your report was sent.</h2>
 <p>Preferred Web Solutions received it and will look into it. If you left an email address, we will reply there.</p>
 <p><a href="index.html">Back to the home page</a></p>
</div>
<p class="hint" style="margin-top:1.5rem">Reports are delivered by Formspree. See the <a href="privacy.html">Privacy Policy</a>.</p>"""

# ---------------------------------------------------------------- shell
def head_html(cfg, title, desc, fonts_css):
    pre = ''.join(f'<link rel="preload" href="fonts/{f}" as="font" type="font/woff2" crossorigin>' for f in cfg.get('preload', []))
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="robots" content="noindex, nofollow"><title>{esc(title)}</title><meta name="description" content="{esc(desc)}">'
            f'{pre}<link rel="stylesheet" href="style.css"></head>')

def header_html(cfg, cur):
    items = ''.join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == cur else ""}>{esc(l)}</a>' for k, l, h in cfg['nav'])
    cta = cfg['cta']
    if cfg.get('order_dropdown'):
        dd_items = ''.join(f'<li><a href="#" data-demo="{esc(d)}"><b>{esc(t)}</b><span>{esc(s)}</span></a></li>' for t, s, d in cfg['order_dropdown'])
        endcta = (f'<div class="dd"><button type="button" class="btn dd-btn" aria-expanded="false" aria-controls="dd-menu">{esc(cta)}</button>'
                  f'<ul class="dd-menu" id="dd-menu" hidden>{dd_items}</ul></div>')
    else:
        endcta = f'<a class="btn" href="{cfg["cta_href"]}">{esc(cta)}</a>'
    return (f'<header class="site-header"><div class="wrap bar"><a class="logo" href="index.html">{cfg["logo_html"]}</a>'
            f'<nav class="nav" id="site-nav" aria-label="Main">{items}<a class="btn m-cta" href="{cfg["cta_href"]}">{esc(cta)}</a></nav>'
            f'{endcta}'
            f'<button type="button" class="menu-btn" aria-expanded="false" aria-controls="site-nav"><i aria-hidden="true"></i>{esc(cfg.get("menu_label","Menu"))}</button>'
            f'</div></header>')

def footer_html(cfg):
    hours = ''.join(f'<li>{esc(a)}<br>{esc(b)}</li>' for a, b in cfg['hours_short'])
    legal = ''.join(f'<li><a href="{k}.html">{esc(l)}</a></li>' for k, l in LEGAL)
    social = ''.join(f'<li><a href="#" data-demo="{esc(s)} link is a demo on this sample.">{esc(s)} (demo)</a></li>' for s in cfg.get('social', []))
    return (f'<footer class="site-footer"><div class="wrap"><div class="foot-grid">'
            f'<div><div class="foot-name">{esc(cfg["name"])}</div><p>{esc(cfg["tagline"])}</p><a class="btn btn--ghost btn--sm" href="{cfg["cta_href"]}">{esc(cfg["cta"])}</a></div>'
            f'<div><h2>{esc(cfg.get("foot_loc_title","Find us"))}</h2><p>{esc(cfg["addr1"])}<br>{esc(cfg["addr2"])}</p>{cfg.get("foot_loc_extra","")}</div>'
            f'<div><h2>{esc(cfg.get("foot_hours_title","Hours"))}</h2><ul>{hours}</ul></div>'
            f'<div><h2>Contact</h2><ul><li><a href="tel:{cfg["tel"]}">{esc(cfg["phone"])}</a></li>{social}</ul></div></div>'
            f'<div class="foot-legal"><ul>{legal}<li><button type="button" data-cookie-settings>Cookie settings</button></li></ul>'
            f'<p class="credit">{cfg["credit"]}</p></div></div></footer>')

def sample_bar(cfg):
    return (f'<aside aria-label="Sample notice"><div class="sample-bar" role="note"><span><strong class="sb-lead">Sample design by Preferred Web Solutions.</strong> '
            f'<span class="sb-long">{esc(cfg["name"])} is a fictional {cfg.get("fictional_word","restaurant")}, not a real business. {esc(cfg.get("bar_tail","Photos are for demonstration only."))}</span>'
            f'<span class="sb-short">Fictional {cfg.get("fictional_word","restaurant")}, not a real business.</span></span></div></aside>')

def callbar(cfg):
    return (f'<nav class="callbar" aria-label="Quick actions"><a class="btn" href="{cfg["cta_href"]}">{esc(cfg["cta"])}</a>'
            f'<a class="btn btn--call" href="tel:{cfg["tel"]}" aria-label="Call {esc(cfg["phone"])}">Call</a></nav>')

def page_html(cfg, key, title, desc, body, cur=None, bodycls=""):
    return (head_html(cfg, title, desc, '') + f'<body class="{bodycls}">'
            '<a class="skip" href="#main">Skip to content</a>'
            '<p id="demo-live" class="sr-only" role="status" aria-live="polite"></p>'
            + sample_bar(cfg) + header_html(cfg, cur) +
            f'<main id="main">{body}</main>' + footer_html(cfg) + callbar(cfg) +
            '<script src="consent.js"></script><script src="site.js"></script></body></html>')

def legal_page(cfg, key, label):
    body = f'<div class="wrap doc">{legal_body(key, cfg)}</div>'
    h = (head_html(cfg, f'{label} | {cfg["name"]} (sample)', f'{label} for {cfg["name"]}, a fictional {cfg.get("fictional_word","restaurant")} and design sample by Preferred Web Solutions.', '') +
         '<body class="legal"><a class="skip" href="#main">Skip to content</a><p id="demo-live" class="sr-only" role="status" aria-live="polite"></p>' + sample_bar(cfg) +
         f'<header class="simple-head"><div class="wrap bar"><a class="logo" href="index.html">{cfg["logo_html"]}</a><a href="index.html">Back to the home page</a></div></header>'
         f'<main id="main">{body}</main>' + footer_html(cfg) + callbar(cfg) +
         '<script src="consent.js"></script><script src="site.js"></script></body></html>')
    return h

def build(cfg, pages, theme_css, outroot=None):
    """pages: {key:(filename, title, desc, body_html, cur_key, bodycls)}"""
    outroot = outroot or REPO
    d = os.path.join(outroot, cfg['slug']); os.makedirs(d, exist_ok=True)
    cfg['dir'] = cfg.get('dir') or d
    fonts_css = ''.join(
        f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{w};font-display:swap;src:url(fonts/{f}) format('woff2')}}\n"
        for fam, w, f in cfg['fonts'])
    with open(os.path.join(d, 'style.css'), 'w') as fh: fh.write(fonts_css + BASE_CSS + theme_css)
    with open(os.path.join(d, 'site.js'), 'w') as fh: fh.write(SITE_JS)
    with open(os.path.join(d, 'consent.js'), 'w') as fh: fh.write(CONSENT_JS)
    with open(os.path.join(d, 'robots.txt'), 'w') as fh: fh.write('User-agent: *\nDisallow: /\n')
    for k, (fn, title, desc, body, cur, cls) in pages.items():
        with open(os.path.join(d, fn), 'w') as fh: fh.write(page_html(cfg, k, title, desc, body, cur, cls))
    for k, l in LEGAL:
        with open(os.path.join(d, k + '.html'), 'w') as fh: fh.write(legal_page(cfg, k, l))
    return d
