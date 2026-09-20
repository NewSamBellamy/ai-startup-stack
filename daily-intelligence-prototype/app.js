const app=document.getElementById('app');
const simpleBtn=document.getElementById('simpleBtn');
const deepBtn=document.getElementById('deepBtn');
simpleBtn.onclick=()=>{app.classList.remove('deep');simpleBtn.classList.add('active');deepBtn.classList.remove('active')};
deepBtn.onclick=()=>{app.classList.add('deep');deepBtn.classList.add('active');simpleBtn.classList.remove('active')};
document.querySelectorAll('.sources-toggle').forEach(btn=>btn.onclick=()=>{const s=btn.nextElementSibling;s.classList.toggle('show');btn.textContent=s.classList.contains('show')?'Hide sources':'Sources'});
document.querySelectorAll('[data-go]').forEach(btn=>btn.onclick=()=>{const id=btn.dataset.go;['today','learn','saved'].forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==id));document.querySelectorAll('[data-go]').forEach(b=>b.classList.remove('active'));btn.classList.add('active');window.scrollTo({top:0,behavior:'smooth'})});
window.addEventListener('scroll',()=>{const h=document.documentElement.scrollHeight-innerHeight;const p=h?Math.min(100,Math.max(20,scrollY/h*100)):20;document.getElementById('progress').style.width=p+'%'});