const app=document.getElementById('app');
const simpleBtn=document.getElementById('simpleBtn');
const deepBtn=document.getElementById('deepBtn');
const drawer=document.getElementById('drawer');
const scrim=document.getElementById('scrim');
const drawerClose=document.getElementById('drawerClose');
const drawerTitle=document.getElementById('drawerTitle');
const drawerBody=document.getElementById('drawerBody');
const drawerQuestion=document.getElementById('drawerQuestion');

const founderContent={
  founder1:{
    title:"Look one layer beyond the model race.",
    body:"If good AI becomes broadly available, the durable value may move into products that understand a specific workflow, own a customer relationship, or make AI trustworthy enough to use every day.",
    question:"What becomes newly possible when intelligence gets cheaper?"
  },
  founder2:{
    title:"The bottleneck becomes the business.",
    body:"Rapid growth creates new constraints. Networking, power, cooling, memory, data movement and reliability can become enormous markets because they sit in the path of demand.",
    question:"What pain is being created by AI's success?"
  }
};

simpleBtn.onclick=()=>{app.classList.remove('deep');simpleBtn.classList.add('active');deepBtn.classList.remove('active')};
deepBtn.onclick=()=>{app.classList.add('deep');deepBtn.classList.add('active');simpleBtn.classList.remove('active')};

document.querySelectorAll('[data-toggle]').forEach(btn=>{
  btn.addEventListener('click',()=>{
    const target=document.getElementById(btn.dataset.toggle);
    target.classList.toggle('show');
  });
});

document.querySelectorAll('[data-drawer]').forEach(btn=>{
  btn.addEventListener('click',()=>{
    const c=founderContent[btn.dataset.drawer];
    drawerTitle.textContent=c.title;
    drawerBody.textContent=c.body;
    drawerQuestion.textContent=c.question;
    drawer.classList.add('open');
    scrim.classList.add('show');
    drawer.setAttribute('aria-hidden','false');
  });
});

function closeDrawer(){
  drawer.classList.remove('open');
  scrim.classList.remove('show');
  drawer.setAttribute('aria-hidden','true');
}
drawerClose.onclick=closeDrawer;
scrim.onclick=closeDrawer;

const signalCopy={
  s1:"Cheaper AI changes the math. Tasks that were too expensive to automate can become viable products.",
  s2:"The important signal is not demos. It is repeat use inside real businesses, where reliability and workflow fit matter more than novelty.",
  s3:"As demand grows, the supporting layer matters more: data centers, power, networking, chips and regulation."
};
document.querySelectorAll('[data-signal]').forEach(btn=>{
  btn.addEventListener('click',()=>{
    document.getElementById('signalDetail').textContent=signalCopy[btn.dataset.signal];
  });
});

document.querySelectorAll('[data-go]').forEach(btn=>{
  btn.addEventListener('click',()=>{
    const id=btn.dataset.go;
    ['today','learn','saved'].forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==id));
    document.querySelectorAll('[data-go]').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    window.scrollTo({top:0,behavior:'smooth'});
  });
});

const observer=new IntersectionObserver(entries=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting) entry.target.classList.add('visible');
  });
},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
