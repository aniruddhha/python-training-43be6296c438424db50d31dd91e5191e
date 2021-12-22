import React from 'react';
import { useState, useEffect } from 'react';


export function Accounts() {

    const data = [
        { sr: 1, acNm: 'abc', acNum: '12348789660', bal: 5000, sts: true },
        { sr: 2, acNm: 'pqr', acNum: '87358362349', bal: 15000, sts: false },
        { sr: 3, acNm: 'lmn', acNum: '65789334546', bal: 95000, sts: true },
        { sr: 4, acNm: 'xyz', acNum: '95948654857', bal: 15000, sts: true },
        { sr: 5, acNm: 'bhy', acNum: '16549865465', bal: 7000, sts: false },
    ]

    const [accounts, setAccounts] = useState(data)

    useEffect(() => { }, [])

    const rows = accounts.map(ac => {
        return (
            <tr>
                <td >{ac.sr}</td>
                <td>{ac.acNm}</td>
                <td>{ac.acNum}</td>
                <td>{ac.bal}</td>
                <td>{ac.sts ? 'active' : 'inactive'}</td>
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
                                <th scope="col">Name</th>
                                <th scope="col">Account #</th>
                                <th scope="col">Balance</th>
                                <th scope="col">Status</th>
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