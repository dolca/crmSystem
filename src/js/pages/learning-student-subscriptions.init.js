/*
Template Name: CRM System - Admin & Dashboard App
Author: Adrian Dolca
Website: https://adrian-dolca.ro
Contact: adrian.dolca@proton.me
File: learning student subscriptions Init Js File
*/

//subscriptionList Table
var options = {
    valueNames: [
        "plan",
        "price",
        "duration",
        "status",
        "payment_due"
    ],
};

// Init list
var subscriptionList = new List("subscriptionList", options).on("updated", function (list) {
    list.matchingItems.length == 0 ?
        (document.getElementsByClassName("noresult")[0].style.display = "block") :
        (document.getElementsByClassName("noresult")[0].style.display = "none");

    if (list.matchingItems.length > 0) {
        document.getElementsByClassName("noresult")[0].style.display = "none";
    } else {
        document.getElementsByClassName("noresult")[0].style.display = "block";
    }
});
