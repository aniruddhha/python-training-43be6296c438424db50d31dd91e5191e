import './second.css'
import { useState } from 'react' // react hook

// state management 

export default function Second() {

    const [msg, setMsg] = useState('hello welcome to react')

    const onBtClk = () => {
        // msg = 'great react'
        console.log(msg)
        setMsg('great react')
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