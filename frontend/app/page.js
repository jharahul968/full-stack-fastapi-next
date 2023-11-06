import Image from 'next/image';
import Router, { useRouter } from 'next/navigation';


export default function Home() {

  const router=useRouter();

  return (
    <main>
      <button className='border p-5 m-5 cursor-pointer hover:border-pink-500 hover:bg-slate-300' onClick={()=>router.push('/notes')}>
        Notes App
      </button>
    </main>
  )
}
