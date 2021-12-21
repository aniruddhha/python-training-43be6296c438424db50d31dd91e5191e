import Dropdown from 'react-bootstrap/Dropdown';
import { useState } from 'react';



function DropDownDemo({ bxCl }) {
    const [bk, setBk] = useState(bxCl)

    const box = {
        backgroundColor: bk,
        width: '300px',
        height: '300px'
    }

    return (
        <div>
            <div >
                <Dropdown>
                    <Dropdown.Toggle variant="success" id="dropdown-basic">
                        Dropdown Button
                    </Dropdown.Toggle>

                    <Dropdown.Menu>
                        <Dropdown.Item onClick={() => setBk('red')}>Red</Dropdown.Item>
                        <Dropdown.Item onClick={() => setBk('green')}>Green</Dropdown.Item>
                        <Dropdown.Item onClick={() => setBk('blue')}>Blue</Dropdown.Item>
                    </Dropdown.Menu>
                </Dropdown>
            </div>
            <div style={box}>

            </div>
        </div>

    )
}

export default DropDownDemo