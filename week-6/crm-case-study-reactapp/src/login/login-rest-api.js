
export function apiCrmLogin(reqBody) {

    const reqObj = {
        method: 'POST',
        headers: {
            'Accept': 'application/json', // I am going to accept json
            'Content-Type': 'application/json' // I am going to send json
        },
        body: JSON.stringify(reqBody)
    }
    const call = fetch('http://localhost:5000/user/login', reqObj)
    return call.then(res => res.json())
}