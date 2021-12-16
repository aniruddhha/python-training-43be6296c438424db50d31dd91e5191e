
// document is that object browser creates after parsing complete html
// document gives you access to all the elements by means of id
const nm = 'welcome to web development'

const ttl = document.getElementById('ttl')

const btn = document.getElementById('btn')
btn.onclick = function () {
    ttl.textContent = nm
}