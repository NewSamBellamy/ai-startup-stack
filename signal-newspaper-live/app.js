const depthCopy=document.getElementById('depthCopy');
document.querySelectorAll('[data-depth]').forEach(btn=>btn.addEventListener('click',()=>{
  document.querySelectorAll('[data-depth]').forEach(b=>b.classList.remove('active'));btn.classList.add('active');
  depthCopy.textContent=btn.dataset.depth==='deep'
    ? 'Lower inference costs change the economics of AI products. More workflows can move from demos to production because serving each request becomes cheaper, faster, and easier to justify.'
    : 'It’s becoming significantly cheaper for companies to run powerful AI models. That lowers the barrier to adopt AI across more industries — not just tech.';
}));
const insights=[
 'Lower costs drive adoption, which drives infrastructure investment, which makes AI even cheaper and more capable.',
 'The important shift is repeat use inside real businesses — not another impressive demo.',
 'As demand grows, the supporting layer matters more: chips, networks, power, data centers, and policy.'
];
document.querySelectorAll('[data-signal]').forEach((btn,i)=>btn.addEventListener('click',()=>{
 document.querySelectorAll('[data-signal]').forEach(b=>b.classList.remove('active'));btn.classList.add('active');
 document.getElementById('signalInsight').textContent=insights[i];
}));
const notesBtn=document.getElementById('founderNotes');
notesBtn?.addEventListener('click',()=>{const notes=document.getElementById('marginNotes');notes.classList.toggle('show');notesBtn.textContent=notes.classList.contains('show')?'Hide the margin notes ↑':'Reveal the margin notes ↓'});
const audioBtn=document.getElementById('audioBtn');
audioBtn?.addEventListener('click',()=>{audioBtn.classList.toggle('playing');audioBtn.textContent=audioBtn.classList.contains('playing')?'▮▮ Playing demo…':'▶ Listen to the clip'});