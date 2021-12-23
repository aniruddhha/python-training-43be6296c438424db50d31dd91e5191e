import react from 'react'
import './registration.css'
import { useState } from 'react'
import { useNavigate } from 'react-router'

import banner from '../images/reg-banner.jpg'

export function UserLogin() {

    const [formData, setFormData] = useState()

    const navigate = useNavigate()

    const onUserNameChanged = ev => setFormData({ ...formData, userName: ev.target.value })
    const onPasswordChanged = ev => setFormData({ ...formData, password: ev.target.value })

    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(formData)

        // - here you need to make post call
        // - response should return user object with role, userId and other required data
        // - you need to store user object in local storage (you need to make little research)
        //   so that, you can retrieve user object from local storage as required through out the app
        // - on the success of fetch call, you need to navigate dashboard

        navigate('/dash')
    }

    return (
        <div className="container d-flex flex-row-reverse align-items-center">
            <form onSubmit={onFormSubmit}>
                <div className="mb-3">
                    <h2 className="text-muted"> User Login </h2>
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
                    <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                    <input
                        onChange={onPasswordChanged}
                        type="password"
                        className="form-control"
                        required
                    />
                    {formData && !formData.password && <div className="form-text text-danger">Password required</div>}
                </div>

                <button type="submit" className="btn btn-primary">Login</button>
            </form>
            <div>
                <img src={banner}></img>
            </div>
        </div>
    )
}