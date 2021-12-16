
//ECMAScript
var nm = 'android' // value can be changed
let ver = 12 //  value can be changed but in a scope
const os = 'Froyo' // constant in scope
// os = 'kkk'

console.log('os is ' + nm + ' version is ' + ver)

let cnt = 10
if (true) {
    let cnt = 20
    let abc = 'hi'

    console.log(abc)
}

var dt = 20
if (true) {
    var dt = 20
}
console.log(dt)


console.log(cnt)
console.log(abc)


