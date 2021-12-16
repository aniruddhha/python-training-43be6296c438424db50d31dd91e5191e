
// document is that object browser creates after parsing complete html
// document gives you access to all the elements by means of id
const nm = 'welcome to web development'
const isTtlVisible = false
const ttl = document.getElementById('ttl')


const btn = document.getElementById('btn')
btn.onclick = function () {
    ttl.textContent = nm
}

const red = document.getElementById('redBtn')
red.onclick = function () {
    ttl.style.color = 'red'
}
const green = document.getElementById('greenBtn')
green.onclick = function () {
    ttl.style.color = 'green'
}

const blue = document.getElementById('blueBtn')
blue.onclick = function () {
    ttl.style.color = 'blue'
}

const show = document.getElementById('showBtn')
show.onclick = function () {
    ttl.style.display = 'block'
}
const hide = document.getElementById('hideBtn')
hide.onclick = function () {
    ttl.style.display = 'none'
}

