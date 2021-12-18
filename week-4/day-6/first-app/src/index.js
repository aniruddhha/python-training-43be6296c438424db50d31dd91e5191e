import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'

import First from './first';
import Second from './second';
import Third from './third'


// react gives you much more elegant way
// i.e. create components


// ReactDOM.render(First(), root);
ReactDOM.render(<Third />, document.getElementById('root'))