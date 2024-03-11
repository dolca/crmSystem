/*
Template Name: CRM System - Admin & Dashboard App
Author: Adrian Dolca
Website: https://adrian_dolca.com/
Contact: adrian.dolca@gmail.com
File: Ecommerce Order Overview init js
*/

var map = L.map('map');

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

L.Routing.control({
    waypoints: [
        L.latLng(57.74, 11.94),
        L.latLng(57.6792, 11.949)
    ],
    show: false,
    routeWhileDragging: true
}).addTo(map);
