export function apiListCrmUsers() {

    const call = fetch('http://localhost:5000/admin/users')
    return call.then(res => res.json())
}