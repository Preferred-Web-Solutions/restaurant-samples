/* Consent banner. This site sets no cookies and loads no analytics or marketing scripts.
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
