import './second.css'

export default function Second() {

    let msg = 'hello welcome to react'

    const onBtClk = () => {
        msg = 'great react'
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