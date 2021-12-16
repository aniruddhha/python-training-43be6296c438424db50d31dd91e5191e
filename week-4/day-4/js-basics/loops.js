
function whileLoop() {
    let cnt = 1
    while (cnt < 10) {
        console.log(cnt)
        cnt++
    }
}

function forLoop() {
    const ageCnt = 10
    for (let i = 0; i < ageCnt; i++) {
        console.log(` Your Age is ${i} `) // es6
        console.log('Your Age is ' + i) // older way
    }
}

function doWhile() {
    let cnt = 0
    do {
        console.log(`Counter is ${cnt}`)
        cnt++
    } while (cnt < 10)
}

whileLoop()
forLoop()
doWhile()
