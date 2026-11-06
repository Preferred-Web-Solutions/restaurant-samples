/* Shared sample-site script. No cookies, no storage except the consent choice, no third-party requests. */
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
