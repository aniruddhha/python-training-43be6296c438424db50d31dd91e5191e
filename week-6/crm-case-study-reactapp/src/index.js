import React from 'react';
import ReactDOM from 'react-dom';

import { LoginPage } from './login/login';
import { DashboardPage } from './dashboard/dashboard'

import { BrowserRouter, Routes, Route } from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';


const routes = (
  <BrowserRouter>
    <Routes>
      <Route path='/' element={<LoginPage />}></Route>
      <Route path='/dash' element={<DashboardPage />}></Route>
    </Routes>
  </BrowserRouter>
)


ReactDOM.render(
  routes,
  document.getElementById('root')
);

