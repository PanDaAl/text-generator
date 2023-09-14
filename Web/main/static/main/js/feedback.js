const showFormBtn = document.getElementById("feedback_button");
const overlay = document.getElementById('overlay');
const sendFormBtn = document.getElementById('feedback_button_in_form');
const name = document.getElementById('text_name');
const email = document.getElementById('text_email');
const main_text = document.getElementById('text_main');
const name_error = document.getElementById('text_error_name');
const email_error = document.getElementById('text_error_email');
const main_error = document.getElementById('text_error_main');
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const successSendWindow = document.getElementById('success_send_window');

showFormBtn.addEventListener("click", () => {
    feedback_form.style.opacity = 1;
    feedback_form.style.zIndex = 9999;
    feedback_form.style.transition = "opacity 0.5s ease-in-out";
    overlay.style.opacity = 1;
    overlay.style.zIndex = 9998;
    overlay.style.transition = "opacity 0.5s ease-in-out";
    sendFormBtn.style.pointerEvents = 'auto';
});

overlay.addEventListener("click", () => {
    feedback_form.style.opacity = 0;
    feedback_form.style.zIndex = -9998;
    feedback_form.style.transition = "opacity 0.5s ease-in-out, z-index 1s ease-in-out";
    overlay.style.opacity = 0;
    overlay.style.zIndex = -9999;
    overlay.style.transition = "opacity 0.5s ease-in-out, z-index 1s ease-in-out";
    successSendWindow.style.opacity = 0;
    successSendWindow.style.zIndex = -9999;
    successSendWindow.style.transition = "opacity 0.5s ease-in-out, z-index 1s ease-in-out";
    sendFormBtn.style.pointerEvents = 'none';
    name.value = "";
    email.value = "";
    main_text.value = "";
    main_error.style.opacity = 0;
    main_text.style.border = "1px solid #ccc";
    email_error.style.opacity = 0;
    email.style.border = "1px solid #ccc";
    name_error.style.opacity = 0;
    name.style.border = "1px solid #ccc";
});

sendFormBtn.addEventListener('click', () => {
    let emailValue = email.value.trim();
    let name_check = false;
    let email_check = false;
    let main_text_check = false;
    if (name.value !== "") {
        name_error.style.opacity = 0;
        name.style.border = "1px solid green";
        name_check = true;
    } else {
        name_error.style.opacity = 1;
        name.style.border = "1px solid red";
        name_check = false;
    }
    if (emailValue !== "" && emailRegex.test(emailValue)) {
        email_error.style.opacity = 0;
        email.style.border = "1px solid green";
        email_check = true;
    } else {
        email_error.style.opacity = 1;
        email.style.border = "1px solid red";
        email_check = false;
    }
    if (main_text.value !== "") {
        main_error.style.opacity = 0;
        main_text.style.border = "1px solid green";
        main_text_check = true;
    } else {
        main_error.style.opacity = 1;
        main_text.style.border = "1px solid red";
        main_text_check = false;
    }
    if (name_check && email_check && main_text_check) {
        successSendWindow.style.opacity = 1;
        successSendWindow.style.zIndex = 9999;
        successSendWindow.style.transition = "opacity 0.5s ease-in-out";
        main_error.style.opacity = 0;
        main_text.style.border = "1px solid #ccc";
        email_error.style.opacity = 0;
        email.style.border = "1px solid #ccc";
        name_error.style.opacity = 0;
        name.style.border = "1px solid #ccc";
    }
});

name.addEventListener("input", function() {
    if (name.value !== "") {
        name_error.style.opacity = 0;
        name.style.border = "1px solid green";
    } else {
        name_error.style.opacity = 1;
        name.style.border = "1px solid red";
    }
});

email.addEventListener("input", function() {
    let emailValue = email.value.trim();
    if (emailValue !== "" && emailRegex.test(emailValue)) {
        email_error.style.opacity = 0;
        email.style.border = "1px solid green";
    } else {
        email_error.style.opacity = 1;
        email.style.border = "1px solid red";
    }
});

main_text.addEventListener("input", function() {
    if (main_text.value !== "") {
        main_error.style.opacity = 0;
        main_text.style.border = "1px solid green";
    } else {
        main_error.style.opacity = 1;
        main_text.style.border = "1px solid red";
    }
});