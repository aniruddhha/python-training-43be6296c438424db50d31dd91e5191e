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

ol = document.getElementById('mbs')

for (let i = 0; i < mobiles.length; i++) {
    const mb = mobiles[i]

    const li = document.createElement('li')
    li.textContent = mb

    ol.appendChild(li)
}