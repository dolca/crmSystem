/*
Template Name: CRM System - Admin & Dashboard App
Author: Adrian Dolca
Version: 1.1.0
Website: https://adrian_dolca.com/
Contact: adrian.dolca@gmail.com
File: Common Plugins Js File
*/

//Common plugins
if (document.querySelectorAll("[toast-list]"))
  document.writeln("<script src='/static/libs/toastify-js/src/toastify.js'></script>");

if (document.querySelectorAll("[data-provider]"))
  document.writeln("<script src='/static/libs/flatpickr/dist/flatpickr.min.js'></script>");

if (document.querySelectorAll('[data-choices]'))
  document.writeln("<script src='/static/libs/choices.js/public/assets/scripts/choices.min.js'></script>");
