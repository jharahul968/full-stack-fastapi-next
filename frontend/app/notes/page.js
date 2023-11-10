'use client'

import Head from 'next/head';
import { useState, useEffect } from 'react';

export default function Notes() {
    const [note, setNote] = useState('');
    const [notes, setNotes] = useState([]);
    const [clickedUpdate, setClickedUpdate]=useState(false);
    const [updatedNote, setUpdatedNote]=useState('');

    useEffect(()=>{
        async function fetchNotes(){
            const res=await
            fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes/`);
            const json=await res.json();
            setNotes(json);
        }
        fetchNotes();
    }, [])

    function handleChange(e){
        setNote(e.target.value);
    }

    function handleUpdateChange(e){
        setUpdatedNote(e.target.value);
    }

    const toggleUpdate=()=>{
        setClickedUpdate(!clickedUpdate);
    }

    async function handleSubmit(){

        if (note.trim() === '') {
            window.alert('Cannot submit empty note.')
            return;
        }

        const res=await
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes/`, {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                text: note,
                completed: false
            })
        })
        const json=await res.json();
        setNotes([...notes, json]);
        setNote('');
    }

    async function handleDelete(id){
        const res=await
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes/${id}`,{
            method: 'DELETE'
        })
        setNotes(notes.filter((note)=>note.id!==id));
    }

    async function handleUpdate(id){
        if (updatedNote.trim() === '') {
            window.alert('Cannot submit empty note.')
            return;
        }

        const res=await
        fetch(`${process.env.NEXT_PUBLIC_API_URL}/notes/${id}`,{
            method: 'PUT',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                text: updatedNote,
                completed: false
            })
        })
        const json=await res.json();
        const updatedNotes=notes.map(note=>{
            if (note.id===id){
                return {...note, text: json.text};
            }
            return note;
        });
        setNotes(updatedNotes);
        setUpdatedNote('');
        toggleUpdate();
    }




    return (
        <div>
            <Head>
                <title>Notes</title>
            </Head>
            <div className="container mx-auto p-10 m-10">
                <div className='flex flex-col'>
                <h1 className='font-bold mb-3'>
                    Notes
                    </h1>
                    <textarea value={note} onChange={handleChange} className='mx-auto p-3 m-5 border border-black-500'>
                    </textarea>
                    <div className='mx-auto p-3 m-5'>
                        <button onClick={handleSubmit} className='bg-green-500 p-3 text-white'>
                            Submit
                        </button>
                    </div>
                <div>
                <ul>
                    {notes && notes.map((note)=>
                    <li key={note.id} className='bg-yellow-100 m-3 p-3 border-yellow-200 border-2 overflow-hidden'>
                        {note.id}. {note.text}
                        <div className='button_class'>
                            <div>
                            <button className="buttons" onClick={()=>handleDelete(note.id)}>
                                Delete
                            </button> 
                            </div>
                            <div>
                            <button className="buttons" onClick={()=>toggleUpdate()}>
                                Update
                            </button> 
                            </div>
                        </div>
                        {clickedUpdate && (
                            <div>
                                <textarea value={updatedNote} onChange={handleUpdateChange} className='mx-auto p-3 m-5 border border-black-500'>
                                </textarea>
                                <button onClick={()=>handleUpdate(note.id)}>
                                    Update
                                </button>
                            </div>
                        )}
                    </li>
                    )}
                </ul>
            </div>
        </div>
        </div>
        </div>
    )
}

