'use client';

import { useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';

export default function Page({params}){
    const router=useRouter();
    const slug=params.slug;
    const [note, setNote]=useState('');

    useEffect(()=>{
        async function fetchNote(slug){
            const res=await fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes/${slug}`)
            const json=await res.json();
            setNote(json.text);
            console.log("note: ", note);
        }
        fetchNote(slug);
    }, [])

    return (
        <div className='bg-yellow-100 m-3 p-3 border-yellow-200 border-2 overflow-hidden'>
            {note}            
        </div>
    )
}