/*
Template Name: CRM System - Admin & Dashboard App
Author: Adrian Dolca
Website: https://adrian-dolca.ro
Contact: adrian.dolca@proton.me
File: nestable init js
*/

// Nested sortable demo
var nestedSortables = [].slice.call(document.querySelectorAll('.nested-sortable'));

// Loop through each nested sortable element
if (nestedSortables)
    Array.from(nestedSortables).forEach(function (nestedSort){
        new Sortable(nestedSort, {
            group: 'nested',
            animation: 150,
            fallbackOnBody: true,
            swapThreshold: 0.65
        });
    });

// Nested sortable handle demo
var nestedSortablesHandles = [].slice.call(document.querySelectorAll('.nested-sortable-handle'));
if (nestedSortablesHandles)
    // Loop through each nested sortable element
    Array.from(nestedSortablesHandles).forEach(function (nestedSortHandle){
        new Sortable(nestedSortHandle, {
            handle: '.handle',
            group: 'nested',
            animation: 150,
            fallbackOnBody: true,
            swapThreshold: 0.65
        });
    });
