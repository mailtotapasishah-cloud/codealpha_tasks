
"use client";
import {useState} from "react";
export default function Home(){
 const [q,setQ]=useState("");
 const [msgs,setMsgs]=useState<any[]>([]);
 async function ask(){
  const r=await fetch("/api/chat",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({question:q})});
  const d=await r.json();
  setMsgs([...msgs,{u:q,b:d.answer}]);
  setQ("");
 }
 return <main style={{maxWidth:900,margin:"40px auto"}}>
 <h1>AI Powered FAQ Chatbot</h1>
 {msgs.map((m,i)=><div key={i}><p><b>You:</b> {m.u}</p><p><b>Bot:</b> {m.b}</p></div>)}
 <input value={q} onChange={e=>setQ(e.target.value)} />
 <button onClick={ask}>Send</button>
 </main>
}
