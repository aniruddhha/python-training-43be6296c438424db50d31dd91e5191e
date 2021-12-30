import { apiListCrmUsers } from './crm-user-list-rest-api'
import { useEffect, useState } from 'react'
import './users.css'

export function CrmUser() {

    const [users, setUsers] = useState([])

    useEffect(() => { // used for calling rest api at the time of initial render
        apiListCrmUsers().then(json => {
            const urs = json['res']

            setUsers(urs)
        })
    }, [])

    const trUsers = users.map((usr, inx) => {
        return (
            <tr key={inx}>
                <td>{inx + 1}</td>
                <td>{usr['mobile']}</td>
                <td>{usr['role']}</td>
                <td>{usr['doj']}</td>
                <td>{usr['status'] == 1 ? '✅' : '❌'}</td>
                <td>{usr['status'] ? 'deactivate' : 'activate'}</td>
            </tr>
        )
    })

    return (
        <div className='container border border-primary'>
            <div className='row'>
                <div className='column'>
                    <h3 className='text-muted'> Crm Users </h3>
                </div>
            </div>
            <div className='row'>
                <table className="table">
                    <thead>
                        <tr>
                            <th scope="col">#</th>
                            <th scope="col">Mobile</th>
                            <th scope="col">Role</th>
                            <th scope="col">Joining</th>
                            <th scope="col">Status</th>
                            <th scope="col">Operation</th>
                        </tr>
                    </thead>
                    <tbody>
                        {trUsers}
                    </tbody>
                </table>
            </div>
        </div>
    )
}