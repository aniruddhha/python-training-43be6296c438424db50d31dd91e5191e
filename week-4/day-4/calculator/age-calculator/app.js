const dob = document.getElementById('dob')
dob.onchange = e => { // arrow - lambda - traditional function

    const selectedDateStr = e.target.value //  string date
    const selectedDate = new Date(selectedDateStr) // convert string to date object

    console.log(selectedDate)
    // console.log(calculateAge(new Date(e.target.value)))

    const msg = document.getElementById('msg')
    msg.textContent = `Age is ${calculateAge(selectedDate)}` // you pass date object
}

function calculateAge(birthday) { // birthday is a date
    const ageDifMs = Date.now() - birthday;
    const ageDate = new Date(ageDifMs); // miliseconds from epoch
    return Math.abs(ageDate.getUTCFullYear() - 1970)
}