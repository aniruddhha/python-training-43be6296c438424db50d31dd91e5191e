import React from 'react';
import ReactDOM from 'react-dom';

import 'bootstrap/dist/css/bootstrap.min.css';

import Car from './car'
import DropDownDemo from './dropdowndemo';
import SignupPage from './signup-form';

const car = <Car color='I am a main prop' price='100'>
  <h1> I am a child prop </h1>
</Car>

const dropdown = <DropDownDemo bxCl="black"></ DropDownDemo>

ReactDOM.render(
  <SignupPage />,
  document.getElementById('root')
);

