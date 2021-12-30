
import React from 'react';
import bg from '../images/bg-login.jpg'

import { useState, useCallback } from 'react';
import { apiCrmLogin } from './login-rest-api';
import { useNavigate } from 'react-router';

export function LoginPage() {

    const navigate = useNavigate()
    const [formData, setFormData] = useState({ user_name: '', password: '' })

    const onChangeMobile = (e) => setFormData({ ...formData, user_name: e.target.value })
    const onChangePassword = (e) => setFormData({ ...formData, password: e.target.value })

    const makeLoginRequest = useCallback(() => {
        apiCrmLogin(formData).then(resJson => {
            console.log(resJson)
            if (resJson['sts'] == 'success') {
                // localStorage is html5 feature
                const result = resJson['res']
                localStorage.setItem('status', result['status'])
                localStorage.setItem('mobile', result['mobile'])
                localStorage.setItem('doj', result['doj'])
                localStorage.setItem('role', result['role'])

                navigate('/dash')
            }
        }).catch(err => console.log(err))
    }, [formData])

    const onLoginSubmit = (e) => {
        e.preventDefault() // stop refreshing bevaiour
        console.log(formData)

        makeLoginRequest()
    }

    return (
        <div className='container py-3'>
            <header>
                <div className="d-flex flex-column flex-md-row align-items-center pb-3 mb-4 border-bottom">
                    <a href="/" className="d-flex align-items-center text-dark text-decoration-none">
                        <span className="fs-4">CRM Food Vendor</span>
                    </a>

                    <form onSubmit={onLoginSubmit} className="d-inline-flex mt-2 mt-md-0 ms-md-auto">
                        <div className="form-floating">
                            <input onChange={onChangeMobile} type="text" className="form-control" id="floatingInput" placeholder="8888888888" />
                            <label htmlFor="floatingInput">Mobile</label>
                        </div>
                        <div className="form-floating ms-2">
                            <input onChange={onChangePassword} type="password" className="form-control" id="floatingPassword" placeholder="Password" />
                            <label htmlFor="floatingPassword">Password</label>
                        </div>
                        <div className="d-flex align-items-center ms-2">
                            <input type="submit" value="Login" className="btn btn-primary" />
                        </div>
                    </form>
                </div>
            </header>
            <main>
                <div className="row">
                    <div className="col d-flex justify-content-center">
                        <img src={bg} />
                    </div>
                </div>
            </main>
        </div>
    )
}