import React from 'react';
import ReactDOM from 'react-dom';

import { LoginPage } from './login/login';

import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';


const routes = (
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<LoginPage />}></Route>
    </Routes>
  </BrowserRouter>
)


ReactDOM.render(
  routes,
  document.getElementById('root')
);

