const app=document.getElementById('app');
const simpleBtn=document.getElementById('simpleBtn');
const deepBtn=document.getElementById('deepBtn');
simpleBtn.onclick=()=>{app.classList.remove('deep');simpleBtn.classList.add('active');deepBtn.classList.remove('active')};
deepBtn.onclick=()=>{app.classList.add('deep');deepBtn.classList.add('active');simpleBtn.classList.remove('active')};

const insights=[
  "Lower costs expand what can be built — and move opportunity away from model access alone.",
  "The shift that matters is from demos to repeat use inside real businesses, where reliability beats novelty.",
  "As access broadens, advantage moves toward distribution, workflow fit, trusted data and infrastructure."
];
document.querySelectorAll('[data-signal]').forEach(btn=>btn.onclick=()=>{
  document.querySelectorAll('[data-signal]').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('signalInsight').textContent=insights[Number(btn.dataset.signal)];
});

const drawer=document.getElementById('drawer'),scrim=document.getElementById('scrim');
function openDrawer(){drawer.classList.add('open');scrim.classList.add('show')}
function closeDrawer(){drawer.classList.remove('open');scrim.classList.remove('show')}
document.getElementById('founderOpen').onclick=openDrawer;
document.getElementById('drawerClose').onclick=closeDrawer;
scrim.onclick=closeDrawer;

document.getElementById('sourceNote').onclick=()=>document.getElementById('sourcePanel').classList.toggle('show');
document.querySelectorAll('.source-row button').forEach(btn=>btn.onclick=()=>document.getElementById('sourcePanel').classList.add('show'));

document.querySelectorAll('[data-go]').forEach(btn=>btn.onclick=()=>{
  const id=btn.dataset.go;
  ['today','learn','saved'].forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==id));
  document.querySelectorAll('[data-go]').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  window.scrollTo({top:0,behavior:'smooth'});
});
