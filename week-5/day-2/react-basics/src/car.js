import React from 'react';

function Car(props) {

    console.log(props)

    return (
        <div>
            {props.children}
            <h1> Car Price is {props.price} </h1>
            <p> Car Color is {props.color}</p>
        </div>
    )
}

export default Car