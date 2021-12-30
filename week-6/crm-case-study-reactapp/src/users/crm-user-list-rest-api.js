export function apiListCrmUsers() {
    const call = fetch('http://localhost:5000/admin/users')
    return call.then(res => res.json())
}

export function apiActivateDeactivateUser(admin_id, user_id, sts) {
    const reqConfig = {
        method: 'PUT',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // body: { admin_id: admin_id, user_id: user_id, sts: sts }
        body: JSON.stringify({ admin_id, user_id, sts })
    }

    const call = fetch('http://localhost:5000/admin/activation', reqConfig)
    return call.then(res => res.json())
}