const mobiles = [
    'abc',
    'pqr',
    'lmn',
    'xyz',
    'ghj',
    'mkl',
    'nmb',
    'wrr',
    'tyy'
]

const ol = document.getElementById('mbs') // refer the dom element 

for (let i = 0; i < mobiles.length; i++) {
    const mb = mobiles[i]

    const li = document.createElement('li') // create the dom element also
    li.textContent = mb

    ol.appendChild(li) // adding element into the dom
}

const btDl = document.getElementById('btDl')
btDl.onclick = () => {
    const lastChild = ol.lastChild
    ol.removeChild(lastChild)
}