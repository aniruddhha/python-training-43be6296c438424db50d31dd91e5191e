import { useState } from 'react'
import './third.css'

function Third() {

    const maxColor = 255
    const [red, setRed] = useState(0)
    const [green, setGreen] = useState(0)
    const [blue, setBlue] = useState(0)

    const onClickRedAdd = () => {
        setRed(red + 2)
    }

    const onClickRedSub = () => {
        setRed(red - 2)
    }

    const onClickGreenAdd = () => {
        setGreen(green + 2)
    }

    const onClickGreenSub = () => {
        setGreen(green - 2)
    }

    const onClickBlueAdd = () => {
        setBlue(blue + 2)
    }

    const onClickBlueSub = () => {
        setBlue(blue - 2)
    }

    const stObj = { backgroundColor: `rgb(${red}, ${green}, ${blue})` }
    return (
        <div className='colCont'>
            <div className='colorPanel' style={stObj}>

            </div>
            <div className='red'>
                <input type='button' value='-' onClick={onClickRedSub} />
                <progress value={red} max={maxColor} ></progress>
                <input type='button' value='+' onClick={onClickRedAdd} />
            </div>
            <div className='green'>
                <input type='button' value='-' onClick={onClickGreenSub} />
                <progress value={green} max={maxColor}></progress>
                <input type='button' value='+' onClick={onClickGreenAdd} />
            </div>
            <div className='blue'>
                <input type='button' value='-' onClick={onClickBlueSub} />
                <progress value={blue} max={maxColor}></progress>
                <input type='button' value='+' onClick={onClickBlueAdd} />
            </div>
        </div>
    )
}

export default Third