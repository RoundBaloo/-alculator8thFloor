export const switchButtons = () => {
    const table = document.querySelector('.users');

    table.querySelectorAll('.info-row').forEach(row => {
        row.addEventListener('mouseenter', () => {

            const deleteButton = row.querySelector('.delete-button');
            const changeButton = row.querySelector('.change-button');

            deleteButton.style.visibility = 'visible';
            changeButton.style.visibility = 'visible';

            deleteButton.style.pointerEvents = 'auto';
            changeButton.style.pointerEvents = 'auto';
        });

        row.addEventListener('mouseleave', () => {

            const deleteButton = row.querySelector('.delete-button');
            const changeButton = row.querySelector('.change-button');

            deleteButton.style.visibility = 'hidden';
            changeButton.style.visibility = 'hidden';

            deleteButton.style.pointerEvents = 'none';
            changeButton.style.pointerEvents = 'none';
        })
    })
}