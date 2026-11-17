(function(){
var T=window.PS_T||{};
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return [].slice.call((r||document).querySelectorAll(s))}
// mobile menu
var b=$('.burger'),n=$('.nav');
if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)})}
// close dropdown when clicking outside
document.addEventListener('click',function(e){$$('.nav details[open]').forEach(function(d){if(!d.contains(e.target))d.removeAttribute('open')})});
function money(v){v=Math.round(v/100)*100;return '€'+v.toString().replace(/\B(?=(\d{3})+(?!\d))/g,T.sep||',')}

/* ---------- padel estimator ---------- */
var est=$('#est');
if(est){
 // public selling prices, EUR excl. VAT, ex-works. Range shown = price to price + 5%
 var P={court:{olimpia:21040,panoramix:23570,brutux:26820},install:2875,cover:{pro:59800,xl:64690},assembly:5750,flap:6900};
 var qty=1,out=$('#qty');
 function val(nm){var i=$('input[name='+nm+']:checked',est);return i?i.value:null}
 function calc(){
  var m=val('model'),c=val('cover'),inst=val('inst')==='yes',fl=$('#flap'),lines=[];
  fl.disabled=(c==='none'); if(c==='none')fl.checked=false;
  var t=P.court[m]*qty; lines.push(qty+' × '+m.charAt(0).toUpperCase()+m.slice(1)+' — '+T.l_court);
  if(inst){t+=P.install*qty;lines.push(T.l_inst)}
  if(c!=='none'){t+=(P.cover[c]+P.assembly)*qty;lines.push(qty+' × '+(c==='pro'?'One-Pro':'One-Pro XL')+' — '+T.l_cover);
   if(fl.checked){t+=P.flap*qty;lines.push(T.l_flap)}}
  $('#price').innerHTML='<span>'+money(t)+'</span> – <span>'+money(t*1.05)+'</span>';
  $('#incl').innerHTML=lines.map(function(l){return '<li>'+l+'</li>'}).join('');
  $('#lead').textContent=c==='none'?T.l_lead:T.l_lead_cover;
  return {m:m,c:c,inst:inst,flap:fl.checked,t:t};
 }
 $('#plus').onclick=function(){if(qty<20){qty++;out.textContent=qty;calc()}};
 $('#minus').onclick=function(){if(qty>1){qty--;out.textContent=qty;calc()}};
 est.addEventListener('change',calc);
 $('#estSend').onclick=function(){var r=calc();
  var body=T.mail_intro+'\n\n'+T.k_model+': '+r.m+'\n'+T.k_courts+': '+qty+'\n'+T.k_cover+': '+r.c+(r.flap?' + flap':'')+'\n'+T.k_inst+': '+(r.inst?'yes':'no')+'\n'+T.k_budget+': '+money(r.t)+' – '+money(r.t*1.05)+'\n\n'+T.k_name+':\n'+T.k_company+':\n'+T.k_site+':\n'+T.k_phone+':\n';
  location.href='mailto:spaces@permanentsummer.co?subject='+encodeURIComponent('Padel — '+qty+' × '+r.m)+'&body='+encodeURIComponent(body)};
 calc();
}

/* ---------- guided contact form ---------- */
var gf=$('#gf');
if(gf){
 var S={step:1,who:'',prods:[],when:'',svc:'',budget:''};
 var steps=$$('.step',gf),li=$$('.steps li'),bar=$('.bar i',gf),next=$('#next'),back=$('#back'),err=$('#err');
 function show(){
  steps.forEach(function(s){s.classList.toggle('on',+s.dataset.step===S.step)});
  li.forEach(function(l,i){l.className=(i+1<S.step?'done':i+1===S.step?'cur':'');l.querySelector('i').textContent=i+1<S.step?'✓':i+1});
  bar.style.width=Math.min(100,S.step*25)+'%';
  back.style.visibility=(S.step>1&&S.step<5)?'visible':'hidden';
  next.style.display=(S.step>1&&S.step<5)?'':'none';
  next.textContent=S.step===4?T.f_send:T.f_next;
  err.textContent='';
  var h=$('.step.on h2',gf); if(h&&S.started){h.setAttribute('tabindex','-1');h.focus()}
 }
 $$('[data-who]',gf).forEach(function(bt){bt.onclick=function(){S.who=bt.dataset.who;$$('[data-who]',gf).forEach(function(x){x.setAttribute('aria-pressed',x===bt)});S.step=2;S.started=1;show()}});
 $$('[data-prod]',gf).forEach(function(bt){bt.onclick=function(){var v=bt.dataset.prod,i=S.prods.indexOf(v);if(i>-1)S.prods.splice(i,1);else S.prods.push(v);bt.setAttribute('aria-pressed',i<0);bt.querySelector('i').textContent=i<0?'✓':''}});
 $$('[data-k]',gf).forEach(function(bt){bt.onclick=function(){var k=bt.dataset.k;S[k]=bt.dataset.v;$$('[data-k='+k+']',gf).forEach(function(x){x.setAttribute('aria-pressed',x===bt)})}});
 back.onclick=function(){S.step--;show()};
 next.onclick=function(){
  if(S.step===2&&!S.prods.length){err.textContent=T.e_prod;return}
  if(S.step===3&&(!S.when||!S.svc)){err.textContent=T.e_proj;return}
  if(S.step===4){
   var f=function(id){return $('#'+id).value.trim()};
   if(!f('f_name')||!/\S+@\S+\.\S+/.test(f('f_email'))){err.textContent=T.e_contact;return}
   var lines=[T.k_who+': '+S.who,T.k_need+': '+S.prods.join(', '),T.k_site+': '+f('f_site'),T.k_when+': '+S.when,T.k_svc+': '+S.svc,T.k_budget+': '+(S.budget||'-'),'',T.k_name+': '+f('f_name'),T.k_company+': '+f('f_company'),'Email: '+f('f_email'),T.k_phone+': '+f('f_phone'),'',f('f_msg')];
   var body=lines.join('\n');
   $('#sum').textContent=[S.who,S.prods.join(', '),S.when,S.svc].join(' · ');
   $('#waLink').href='https://wa.me/351924477353?text='+encodeURIComponent(body);
   location.href='mailto:spaces@permanentsummer.co?subject='+encodeURIComponent('Project request — '+(f('f_company')||f('f_name')))+'&body='+encodeURIComponent(body);
  }
  S.step++;show();
 };
 // preselect product from ?p=
 try{var p=new URLSearchParams(location.search).get('p');if(p){var bt=$('[data-slug="'+p+'"]',gf);if(bt)bt.click()}}catch(e){}
 show();
}
})();
