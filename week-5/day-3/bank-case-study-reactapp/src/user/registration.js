import react from 'react'
import './registration.css'
import { useState, useCallback } from 'react'

import banner from '../images/reg-banner.jpg'

export function UserRegistration() {

    const [formData, setFormData] = useState()
    const [isRegisterSuccess, setRegisterSuccess] = useState(false)

    const onUserNameChanged = ev => setFormData({ ...formData, userName: ev.target.value })
    const onEmailChanged = ev => setFormData({ ...formData, email: ev.target.value })
    const onPasswordChanged = ev => setFormData({ ...formData, password: ev.target.value })
    const onCheckChanged = ev => setFormData({ ...formData, checkout: ev.target.checked })

    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)

        makePostRequest()
    }

    const validateEmail = (email) => {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            )
    };

    const makePostRequest = useCallback(() => {

        const obj = {
            user_id: 134688,
            user_name: '123456789',
            password: '123456789',
            role: 'admin'
        }

        setRegisterSuccess(false)
        fetch('http://localhost:5000/user', obj)
            .then(dt => {
                setRegisterSuccess(true)
                console.log(dt)
            })
            .catch(err => {
                setRegisterSuccess(false)
                console.log(err)
            })
    }, [isRegisterSuccess])

    return (
        <div className="container d-flex flex-row-reverse align-items-center">
            <form onSubmit={onFormSubmit}>
                <div className="mb-3">
                    <h2 className="text-muted"> User Registration </h2>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label" >User Name</label>
                    <input
                        onChange={onUserNameChanged}
                        type="text"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {
                        formData && !formData.userName && <div className="form-text text-danger">Invalid username</div>
                    }
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                    <input
                        onChange={onEmailChanged}
                        type="email"
                        className="form-control"
                        aria-describedby="emailHelp"
                        required
                    />
                    {formData && !formData.email && <div className="form-text text-danger">Email Is Required</div>}
                    {formData && (formData.email && !validateEmail(formData.email)) && <div className="form-text text-danger">Invalid Email</div>}
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                    <input
                        onChange={onPasswordChanged}
                        type="password"
                        className="form-control"
                        required
                    />
                    {formData && !formData.password && <div className="form-text text-danger">Password required</div>}
                </div>
                <div className="mb-3 form-check">
                    <input
                        onChange={onCheckChanged}
                        type="checkbox"
                        className="form-check-input"
                    />
                    <label htmlFor="form-check-label">Check me out</label>
                </div>

                <button type="submit" className="btn btn-primary">Regsiter</button>
            </form>

            <div>
                <img src={banner}></img>
            </div>
        </div>
    )
}