/*
Template Name: CRM System - Admin & Dashboard App
Author: Adrian Dolca
Website: https://adrian-dolca.ro
Contact: adrian.dolca@proton.me
File: ecommerce-checkout.init.js
*/

// card js plugin
var card = new Card({
    form: document.querySelector('#card-form-elem'),
    container: '.card-wrapper',
    formSelectors: {
        numberInput: 'input#card-number-input',
        expiryInput: 'input#card-expiry-input',
        cvcInput: 'input#card-cvc-input',
        nameInput: 'input#card-name-input'
    },
    placeholders: {
        number: '•••• •••• •••• ••••',
        name: 'Full Name',
        expiry: '••/••',
        cvc: '•••'
    },
    masks: {
        cardNumber: '•' // optional - mask card number
    },
});
