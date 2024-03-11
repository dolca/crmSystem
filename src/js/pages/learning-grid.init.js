/*
Template Name: CRM System - Admin & Dashboard App
Author: adrian_dolca
Website: https://adrian_dolca.com/
Contact: adrian_dolca@gmail.com
File: learning grid Init Js File
*/

// Course Images
var dropzonePreviewNode = document.querySelector("#course-preview-list");
dropzonePreviewNode.id = "";
if (dropzonePreviewNode) {
    var previewTemplate = dropzonePreviewNode.parentNode.innerHTML;
    dropzonePreviewNode.parentNode.removeChild(dropzonePreviewNode);
    var dropzone = new Dropzone(".course-dropzone", {
        url: 'https://httpbin.org/post',
        method: "post",
        previewTemplate: previewTemplate,
        previewsContainer: "#course-preview",
    });
}
