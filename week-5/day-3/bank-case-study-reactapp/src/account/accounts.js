import React from 'react';
import { useState, useEffect, useCallback } from 'react';

export function Accounts() {

    const [accounts, setAccounts] = useState([])

    useEffect(() => {
        fetch('http://localhost:5000/user')
            .then(res => res.json())
            .then(data => {
                setAccounts(data.res)
            })
            .catch(err => console.log(err))
    }, []) // it will call at the time of loading component only 

    const rows = accounts.map((ac, index) => {
        return (
            <tr key={index}>
                <td >{index + 1}</td>
                <td>{ac.user_id}</td>
                <td>{ac.user_name}</td>
                <td>{ac.password}</td>
                <td>{ac.role}</td>
            </tr>
        )
    })

    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <h3> Existing Account List </h3>
                </div>
            </div>

            <div className="row">
                <div className="col">
                    <table className="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Id</th>
                                <th scope="col">Name</th>
                                <th scope="col">Password</th>
                                <th scope="col">Role</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}