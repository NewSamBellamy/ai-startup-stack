const menu=document.getElementById('editionMenu'),scrim=document.getElementById('menuScrim');
function openMenu(){menu.classList.add('open');scrim.classList.add('show')}
function closeMenu(){menu.classList.remove('open');scrim.classList.remove('show')}
document.getElementById('menuBtn').onclick=openMenu;
document.getElementById('closeMenu').onclick=closeMenu;
scrim.onclick=closeMenu;
document.querySelectorAll('.edition-menu a').forEach(a=>a.onclick=closeMenu);

const save=document.getElementById('saveBtn');
save.onclick=()=>{save.textContent=save.textContent==='★'?'☆':'★'};

const term=document.querySelector('[data-term]');
term.onclick=()=>document.getElementById('termDefinition').classList.toggle('show');

const panelCopy=[
  'Lower costs expand the number of products that can exist.',
  'Repeat use inside real businesses matters more than another impressive demo.',
  'Demand for AI creates second-order markets around chips, networking, power, and data centers.'
];
document.querySelectorAll('.cartoon-panel').forEach((panel,i)=>panel.onclick=()=>{
  document.querySelectorAll('.cartoon-panel').forEach(p=>p.classList.remove('active'));
  panel.classList.add('active');
  document.getElementById('panelReveal').textContent=panelCopy[i];
});

const founderButton=document.getElementById('founderReveal');
founderButton.onclick=()=>{
  const notes=document.getElementById('marginNotes');
  notes.classList.toggle('show');
  founderButton.textContent=notes.classList.contains('show')?'HIDE THE MARGIN NOTES ↑':'REVEAL THE MARGIN NOTES ↓';
};

const audio=document.getElementById('audioButton');
audio.onclick=()=>{audio.classList.toggle('playing');audio.textContent=audio.classList.contains('playing')?'▮▮ PLAYING THE CLIP…':'▶ PLAY THE CLIP'};

const io=new IntersectionObserver(entries=>entries.forEach(e=>{
  if(e.isIntersecting)e.target.classList.add('entered');
}),{threshold:.15});
document.querySelectorAll('section').forEach(s=>io.observe(s));