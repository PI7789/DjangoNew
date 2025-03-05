function update_cost(){

// variable creation

    let VIP = document.getElementById("VIP_Selector").value
    let cost = document.getElementById("cost_output")
    let person = document.getElementById("id_booking_people").value
    let start = document.getElementById("id_booking_startdate").value
    let end = document.getElementById("id_booking_enddate").value
    let button = document.getElementById("booking_button")

// date and price
    
    let sdate = new Date(start)

    let edate = new Date(end)

    let diff = edate - sdate 
    
    let daydiff = diff/1000/60/60/24

    let price = 0

    if (VIP == "option1"){
        price = person * 25000
    }

    else if (VIP == "option2"){
        price = person * 35000
    }

    price = daydiff * price

// validation: 
    

    if (person < 1 ){
        document.getElementById("booking_button").disabled = true;
        cost.innerHTML = "Invalid amount of people."
    }
    else if(daydiff < 1){
        document.getElementById("booking_button").disabled = true;
        cost.innerHTML = "Invalid Date."
    }
    
    
    
    
    else{
        document.getElementById("booking_button").disabled = false;
        cost.innerHTML = "Price = £" + price
    }





    

    
    

}
let start = document.getElementById("id_booking_startdate")
let end = document.getElementById("id_booking_enddate")
let person = document.getElementById("id_booking_people") 
let VIP = document.getElementById("VIP_Selector")


start.addEventListener("change", update_cost)
end.addEventListener("change", update_cost)
person.addEventListener("change", update_cost)
VIP.addEventListener("change", update_cost)
