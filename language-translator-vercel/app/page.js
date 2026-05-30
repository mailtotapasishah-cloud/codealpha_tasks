
'use client';
import { useState } from 'react';

export default function Home() {
  const [text, setText] = useState('');
  const [translated, setTranslated] = useState('');

  const translateText = async () => {
    setTranslated('Translation Demo: ' + text);
  };

  return (
    <main className="container">
      <div className="bg"></div>

      <div className="card">
        <h1>🌍 AI Language Translator</h1>

        <textarea
          placeholder="Enter text..."
          value={text}
          onChange={(e)=>setText(e.target.value)}
        />

        <button onClick={translateText}>Translate</button>

        <div className="output">
          {translated}
        </div>
      </div>

      <style jsx>{`
        .container{
          height:100vh;
          display:flex;
          justify-content:center;
          align-items:center;
          overflow:hidden;
          font-family:Arial;
        }

        .bg{
          position:fixed;
          inset:0;
          background:linear-gradient(-45deg,#0f172a,#1e3a8a,#7c3aed,#06b6d4);
          background-size:400% 400%;
          animation:move 10s ease infinite;
        }

        @keyframes move{
          0%{background-position:0% 50%}
          50%{background-position:100% 50%}
          100%{background-position:0% 50%}
        }

        .card{
          z-index:2;
          width:700px;
          padding:30px;
          border-radius:20px;
          background:rgba(255,255,255,0.12);
          backdrop-filter:blur(15px);
          color:white;
        }

        textarea{
          width:100%;
          height:150px;
          margin-top:20px;
          border:none;
          border-radius:10px;
          padding:15px;
        }

        button{
          margin-top:15px;
          width:100%;
          padding:12px;
          border:none;
          border-radius:10px;
          cursor:pointer;
        }

        .output{
          margin-top:20px;
          background:white;
          color:black;
          padding:15px;
          border-radius:10px;
        }
      `}</style>
    </main>
  );
}
