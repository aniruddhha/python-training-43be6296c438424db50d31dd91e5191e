import './second.css'
import { useState } from 'react' // react hook

// state management 

export default function Second() {

    const arr = useState('hello welcome to react')
    const msg = arr[0]
    const setMsg = arr[1]

    const [msg, setMsg] = useState('hello welcome to react')

    const onBtClk = () => {
        // msg = 'great react'
        setMsg('great react')
        console.log(msg)
    }

    return (
        <div>
            <div>
                <h1>{msg}</h1>
            </div>
            <div>
                <input type='button' value='Okay' onClick={onBtClk} />
            </div>
        </div>
    );
}