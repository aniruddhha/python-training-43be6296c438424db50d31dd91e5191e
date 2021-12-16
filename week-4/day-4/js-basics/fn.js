function calculate(num1, num2) {
    return num1 + num2
}

let res = calculate(50, 78)
console.log(res)

// if else ladder
if (res > 50) console.log('its good')
else if (res > 60 && res < 70) console.log('its better')
else console.log('its best')

// switch case statement
switch (res) {
    case 100: {
        console.log('its good')
        break
    }
    case 128: {
        console.log('its better')
        break
    }
    default: {
        console.log('its best')
    }
}