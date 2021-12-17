

const btGt = document.getElementById('btGt')
btGt.onclick = () => {

    // promise design pattern

    // this code is for consuming any rest any
    const resPromise = fetch('http://localhost:5000/bye/456')

    resPromise
        .then(function (res) {
            return res.json() // you are converting res object to json
        })
        .then(json => { // you are getting json data
            console.log(json)
        })
        .catch(ecfhffcgfdgrr => { // here you handle all errors
            console.log(`---- I am Getting Error ----`)
            console.log(ecfhffcgfdgrr)
        })

    console.log(`----hi-----`)
}