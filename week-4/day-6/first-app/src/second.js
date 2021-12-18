import './second.css'

export default function Second() {

    function onClickOkay() {
        console.log(`hello`)
    }

    const onBtClk = () => {
        console.log(`hello seperate arrow`)
    }

    return (
        <div>
            <div className='box'>
            </div>
            <div>
                <input type='button' value='Okay' onClick={onClickOkay} />
                <input type='button' value='Okay' onClick={() => console.log('hello arrow')} />
                <input type='button' value='Okay' onClick={onBtClk} />
            </div>
        </div>
    );
}