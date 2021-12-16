
const btAd = document.getElementById('btAd')
btAd.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) + parseFloat(num2.value)
}

const btSub = document.getElementById('btSb')
btSub.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) - parseFloat(num2.value)
}

const btMul = document.getElementById('btMl')
btMul.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) * parseFloat(num2.value)
}

const btDv = document.getElementById('btDv')
btDv.onclick = function () {
    const res = document.getElementById('res')
    const num1 = document.getElementById('num1')
    const num2 = document.getElementById('num2')

    res.textContent = parseFloat(num1.value) / parseFloat(num2.value)
}