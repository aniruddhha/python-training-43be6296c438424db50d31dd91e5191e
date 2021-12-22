import React from 'react';
import ReactDOM from 'react-dom';

import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";


import { UserRegistration } from './user/registration'
import { UserLogin } from './user/login'
import { Dashboard } from './dashboard/dashboard';

import 'bootstrap/dist/css/bootstrap.min.css';

const router = (
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<UserLogin />}></Route>
      <Route path="reg" element={<UserRegistration />}></Route>
      <Route path="dash" element={<Dashboard />}></Route>
    </Routes>
  </BrowserRouter>
)

ReactDOM.render(
  router,
  document.getElementById('root')
);

