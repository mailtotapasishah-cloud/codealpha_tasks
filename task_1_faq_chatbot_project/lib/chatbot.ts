
import natural from "natural";
import faqs from "../data/faqs.json";
export function getAnswer(q:string){
 const tfidf=new natural.TfIdf();
 faqs.forEach((f:any)=>tfidf.addDocument(f.question.toLowerCase()));
 let best=0,score=0;
 tfidf.tfidfs(q.toLowerCase(),(i:number,m:number)=>{if(m>score){score=m;best=i;}});
 return score<0.1?"No matching FAQ found.":(faqs as any)[best].answer;
}
