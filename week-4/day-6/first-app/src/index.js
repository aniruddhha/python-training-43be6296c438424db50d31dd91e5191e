import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

const version = 17.01


const mobiles = ['abc', 'pqr', 'lmn', 'xyz', 'bcc']
const liMobiles = []

for (let i = 0; i < mobiles.length; i++) {
  liMobiles.push(<li> {mobiles[i]} </li>)
}

const dt = (
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

const root = document.getElementById('root')

ReactDOM.render(dt, root);