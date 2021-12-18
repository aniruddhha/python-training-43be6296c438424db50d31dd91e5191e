import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

import First from './first';
import Second from './second';


// react gives you much more elegant way
// i.e. create components


// ReactDOM.render(First(), root);
ReactDOM.render(<Second />, document.getElementById('root'))