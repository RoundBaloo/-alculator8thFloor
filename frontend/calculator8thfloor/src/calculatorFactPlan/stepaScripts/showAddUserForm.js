export const showAddUserForm = () => {
    const addUserButton = document.querySelector('.add-user');
    const registerForm = document.querySelector('.register');

    addUserButton.style.display = 'none';
    registerForm.style.display = 'flex';
}