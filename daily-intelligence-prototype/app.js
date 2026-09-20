const app=document.getElementById('app'),simpleBtn=document.getElementById('simpleBtn'),deepBtn=document.getElementById('deepBtn');
simpleBtn.onclick=()=>{app.classList.remove('deep');simpleBtn.classList.add('active');deepBtn.classList.remove('active')};
deepBtn.onclick=()=>{app.classList.add('deep');deepBtn.classList.add('active');simpleBtn.classList.remove('active')};
document.getElementById('heroContinue').onclick=()=>document.getElementById('explain').scrollIntoView({behavior:'smooth'});
document.getElementById('depthToggle').onclick=()=>{const x=document.getElementById('depthCopy');x.classList.toggle('show');document.getElementById('depthToggle').textContent=x.classList.contains('show')?'Got it ✓':'Take me deeper →'};
document.querySelector('[data-term]').onclick=()=>document.getElementById('termPop').classList.toggle('show');

const drawer=document.getElementById('drawer'),scrim=document.getElementById('scrim');
function closeDrawer(){drawer.classList.remove('open');scrim.classList.remove('show')}
document.getElementById('founderOpen').onclick=()=>{drawer.classList.add('open');scrim.classList.add('show')};document.getElementById('drawerClose').onclick=closeDrawer;scrim.onclick=closeDrawer;

const insights=[
"Cheaper AI changes the math: tasks that were too expensive to automate can become viable products.",
"Repeat use matters more than demos. Reliability and workflow fit become the real competitive test.",
"More adoption creates demand for chips, networking, power and data centers — making AI a broader economic story."
];
let highest=-1;
document.querySelectorAll('[data-signal]').forEach(btn=>btn.onclick=()=>{
 const n=Number(btn.dataset.signal); if(n>highest+1)return; highest=Math.max(highest,n);
 document.querySelectorAll('[data-signal]').forEach((b,i)=>{b.classList.toggle('done',i<=highest);b.classList.toggle('active',i===n)});
 document.getElementById('signalInsight').textContent=insights[n];
 const track=document.getElementById('signalTrack');track.className='signal-track '+(highest>=2?'step3':highest>=1?'step2':'step1');
 if(highest===2)document.getElementById('dotsConclusion').classList.add('show');
});
document.querySelector('[data-signal="0"]').click();

const trust={
fact:"Confirmed fact means we found the claim in multiple reliable sources or a primary source.",
expert:"Expert interpretation is a named person or publication explaining what the facts may mean.",
signal:"Signal synthesis is our own connection across sources. It is clearly separated from reported fact."
};
document.querySelectorAll('[data-trust]').forEach(b=>b.onclick=()=>document.getElementById('trustNote').textContent=trust[b.dataset.trust]);

const wave=document.getElementById('waveBtn');wave.onclick=()=>{wave.classList.toggle('playing');document.getElementById('waveLabel').textContent=wave.classList.contains('playing')?'Playing demo…':'Play insight'};

document.getElementById('sourceNote').onclick=()=>document.getElementById('sourcePanel').classList.toggle('show');
document.querySelectorAll('[data-source]').forEach(b=>b.onclick=()=>{const p=document.getElementById('sourcePanel');p.textContent=b.textContent+' — '+b.dataset.source+'. In production this opens the exact cited item.';p.classList.add('show')});

document.querySelectorAll('[data-go]').forEach(btn=>btn.onclick=()=>{const id=btn.dataset.go;['today','learn','saved'].forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==id));document.querySelectorAll('[data-go]').forEach(b=>b.classList.remove('active'));btn.classList.add('active');scrollTo({top:0,behavior:'smooth'})});

addEventListener('scroll',()=>{const hero=document.getElementById('hero');if(scrollY<650)hero.style.setProperty('--parallax',Math.min(12,scrollY*.035)+'px')},{passive:true});
