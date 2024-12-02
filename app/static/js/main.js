let container = document.getElementById('container')

toggle = () => {
	container.classList.toggle('sign-in')
	container.classList.toggle('sign-up')
}

setTimeout(() => {
	container.classList.add('sign-in')
}, 200)
function toggleToSignIn() {
    const container = document.querySelector('.container');
    container.classList.remove('sign-up', 'forgot-password');
    container.classList.add('sign-in');
}

function toggleToSignUp() {
    const container = document.querySelector('.container');
    container.classList.remove('sign-in', 'forgot-password');
    container.classList.add('sign-up');
}

function toggleToForgotPassword() {
    const container = document.querySelector('.container');
    container.classList.remove('sign-in', 'sign-up');
    container.classList.add('forgot-password');
}



