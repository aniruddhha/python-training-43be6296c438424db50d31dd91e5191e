import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

const version = 17.01

const mobiles = ['abc', 'pqr', 'lmn', 'xyz', 'bcc']
const liMobiles = []

for (let i = 0; i < mobiles.length; i++) {
  liMobiles.push(<li> {mobiles[i]} </li>)
}

// react gives you much more elegant way
// i.e. create components

function First() { // it is called as component
  const dt1 = (
    <div className='cnt'>
      <div>
        <h1> This is React App</h1>
      </div>
      <div>
        <p> React Version is {version} </p>
        <p>{10 + 23}</p>
        <p>{new Date().toString()}</p>
      </div>
      <div>
        <ol>
          {liMobiles}
        </ol>
      </div>
    </div>
  )

  return dt1
}

function Second() {
  const dt = <div></div>
}


const root = document.getElementById('root')

// ReactDOM.render(First(), root);
ReactDOM.render(<First />, root)