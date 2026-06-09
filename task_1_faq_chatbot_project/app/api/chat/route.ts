
import {NextResponse} from "next/server";
import {getAnswer} from "../../../lib/chatbot";
export async function POST(req:Request){
 const body=await req.json();
 return NextResponse.json({answer:getAnswer(body.question)});
}
