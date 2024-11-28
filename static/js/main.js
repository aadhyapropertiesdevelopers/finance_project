let container = document.getElementById('container');

function toggleToSignIn() {
    container.classList.remove('sign-up', 'forgot-password');
    container.classList.add('sign-in');
}

function toggleToSignUp() {
    container.classList.remove('sign-in', 'forgot-password');
    container.classList.add('sign-up');
}

function toggleToForgotPassword() {
    container.classList.remove('sign-in', 'sign-up');
    container.classList.add('forgot-password');
}
