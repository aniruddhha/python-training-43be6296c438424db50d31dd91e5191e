import { apiListCrmUsers } from './crm-user-list-rest-api'
import { useEffect, useState } from 'react'

export function CrmUser() {

    const [users, setUsers] = useState([])

    useEffect(() => { // used for calling rest api at the time of initial render
        apiListCrmUsers().then(json => {
            const urs = json['res']

            setUsers(urs)
        })
    }, [])

    const liUsers = users.map((usr, inx) => {
        return <li key={inx}>{usr['mobile']}</li>
    })

    return (
        <div>
            <h1> Crm User </h1>
            <ol>
                {liUsers}
            </ol>
        </div>
    )
}