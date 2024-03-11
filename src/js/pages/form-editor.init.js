/*
Template Name: CRM System - Admin & Dashboard App
Author: adrian_dolca
Website: https://adrian_dolca.com/
Contact: adrian_dolca@gmail.com
File: Form editor Js File
*/

// ckeditor
var ckClassicEditor = document.querySelectorAll(".ckeditor-classic")
if (ckClassicEditor) {
    Array.from(ckClassicEditor).forEach(function () {
        ClassicEditor
            .create(document.querySelector('.ckeditor-classic'))
            .then(function (editor) {
                editor.ui.view.editable.element.style.height = '200px';
            })
            .catch(function (error) {
                console.error(error);
            });
    });
}
