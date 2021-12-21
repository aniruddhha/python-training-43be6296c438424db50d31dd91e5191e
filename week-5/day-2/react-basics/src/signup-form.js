import react from 'react'
import './signup-form.css'
import { useState } from 'react'

function SignupPage() {

    const [userName, setUserName] = useState()
    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const [checkOut, setCheckOut] = useState()

    const onEmailChanged = ev => setEmail(ev.target.value)
    const onPasswordChanged = ev => setPassword(ev.target.value)
    const onCheckChanged = ev => setCheckOut(ev.target.value)

    const onFormSubmit = e => {
        e.preventDefault()
        console.log('form submitted')
        console.log(` Username ${userName}, Email ${email}, Password ${password}, Check ${checkOut}`)
    }

    return (
        <div className="container d-flex flex-row-reverse">
            <form onSubmit={onFormSubmit}>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label">User Name</label>
                    <input onChange={ev => setUserName(ev.target.value)} type="text" className="form-control" aria-describedby="emailHelp" />
                    <div className="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                    <input onChange={onEmailChanged} type="email" className="form-control" aria-describedby="emailHelp" />
                    <div className="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div className="mb-3">
                    <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                    <input onChange={onPasswordChanged} type="password" className="form-control" />
                </div>
                <div className="mb-3 form-check">
                    <input onChange={onCheckChanged} type="checkbox" className="form-check-input" />
                    <label htmlFor="form-check-label">Check me out</label>
                </div>
                <button type="submit" className="btn btn-primary">Submit</button>
            </form>
        </div>
    )
}

export default SignupPage