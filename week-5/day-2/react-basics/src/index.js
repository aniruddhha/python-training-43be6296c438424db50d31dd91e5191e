import React from 'react';
import ReactDOM from 'react-dom';

import Car from './car'


ReactDOM.render(
  <Car color='I am a main prop' price='100'>
    <h1> I am a child prop </h1>
  </Car>,
  document.getElementById('root')
);


