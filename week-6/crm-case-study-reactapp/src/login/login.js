
import React from 'react';
import bg from '../images/bg-login.jpg'

export function LoginPage() {

    return (
        <div className='container py-3'>
            <header>
                <div className="d-flex flex-column flex-md-row align-items-center pb-3 mb-4 border-bottom">
                    <a href="/" className="d-flex align-items-center text-dark text-decoration-none">
                        <span className="fs-4">CRM Food Vendor</span>
                    </a>

                    <form className="d-inline-flex mt-2 mt-md-0 ms-md-auto">
                        <div className="form-floating">
                            <input type="text" className="form-control" id="floatingInput" placeholder="name@example.com" />
                            <label for="floatingInput">Mobile</label>
                        </div>
                        <div className="form-floating ms-2">
                            <input type="password" className="form-control" id="floatingPassword" placeholder="Password" />
                            <label for="floatingPassword">Password</label>
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