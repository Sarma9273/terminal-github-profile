const output=document.getElementById("output");
const input=document.getElementById("command");
const history=[];let historyIndex=0;

const data={
about:[
"heading|CHARAN MAVUDURU",
"text|AI & Cybersecurity practitioner focused on SOC engineering, security automation, applied AI and research.",
"text|I build practical systems that connect detection, investigation, retrieval and response.",
"",
"heading|CURRENT FOCUS",
"text|SOC • SIEM • Incident Response • AI Security • RAG • Security Education"
],
skills:[
"heading|TECHNICAL STACK",
"text|Languages     Python • JavaScript • TypeScript • HTML • CSS",
"text|Security      SOC • SIEM • MITRE ATT&CK • Wireshark • Burp Suite",
"text|AI / Data     RAG • FAISS • SentenceTransformers • NLP",
"text|Infra         Docker • Linux • Git • GitHub",
"text|Research      Detection Engineering • Incident Response • AI Security"
],
projects:[
"heading|FEATURED PROJECTS",
"text|[01] RA-XSOC Security Copilot",
"text|    RAG-based security investigation and incident-response assistant.",
"text|[02] SentinelOps-AI",
"text|    AI-assisted security operations command center.",
"text|[03] SynthoQuest",
"text|    Cybersecurity education, labs and institutional technology.",
"text|[04] GURUVERSE",
"text|    Personal developer and portfolio platform.",
"",
"text|Use 'github' for repository links."
],
experience:[
"heading|EXPERIENCE",
"text|Computer Teacher — Swaminarayan Gurukul International School",
"text|Python • HTML • CSS • cybersecurity education",
"",
"text|Junior Design Engineer — Cadsys"
],
education:[
"heading|EDUCATION",
"text|IIT Patna",
"text|Executive M.Tech — AI & Data Science",
"",
"text|Aditya Institute of Technology and Management",
"text|B.Tech — Electrical & Electronics Engineering"
],
contact:[
"heading|CONTACT / PUBLIC LINKS",
"text|GitHub    https://github.com/Sarma9273",
"text|Portfolio  https://github.com/Sarma9273/portfolio",
"text|Terminal   https://sarma9273.github.io/terminal-github-profile/"
],
github:[
"heading|GITHUB",
"text|Profile:   https://github.com/Sarma9273",
"text|RA-XSOC:   https://github.com/Sarma9273/ra-xsoc-security-copilot",
"text|Sentinel:  https://github.com/Sarma9273/sentinelops-ai-command-center",
"text|Portfolio: https://github.com/Sarma9273/portfolio"
],
help:[
"heading|AVAILABLE COMMANDS",
"text|about       profile and focus",
"text|skills      technical stack",
"text|projects    featured projects",
"text|experience  professional experience",
"text|education   academic background",
"text|github      repository links",
"text|contact     public links",
"text|clear       clear terminal",
"text|help        show this menu"
]};

function add(text="",cls="line"){
 const el=document.createElement("div");el.className=cls;
 if(text.startsWith("heading|")){el.className="line heading";el.textContent=text.slice(8)}
 else if(text.startsWith("text|")){el.className="line";el.textContent=text.slice(5)}
 else {el.textContent=text}
 output.appendChild(el);window.scrollTo(0,document.body.scrollHeight);
}
function run(raw){
 const cmd=raw.trim().toLowerCase();
 if(!cmd)return;
 add("sarma@github:~$ "+raw,"line command");
 history.push(raw);historyIndex=history.length;
 if(cmd==="clear"){output.innerHTML="";return}
 if(cmd==="sudo"){add("Nice try. This profile does not need root.");return}
 if(cmd==="whoami"){show("about");return}
 if(data[cmd]){show(cmd);return}
 add("command not found: "+cmd);
 add("Type 'help' to see available commands.","line muted");
}
function show(key){data[key].forEach(x=>add(x))}
input.addEventListener("keydown",e=>{
 if(e.key==="Enter"){run(input.value);input.value=""}
 if(e.key==="ArrowUp"){e.preventDefault();historyIndex=Math.max(0,historyIndex-1);input.value=history[historyIndex]||""}
 if(e.key==="ArrowDown"){e.preventDefault();historyIndex=Math.min(history.length,historyIndex+1);input.value=history[historyIndex]||""}
});
document.querySelectorAll("button").forEach(b=>b.onclick=()=>{input.focus();run(b.dataset.command)});
show("about");add("");add("Type 'help' to explore the profile.","line muted");input.focus();
