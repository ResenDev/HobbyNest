document.addEventListener('htmx:afterSwap', (event) => {
    if (event.target.id === 'addContent') {
        const modal = new bootstrap.Modal(document.getElementById('addItem'));
        modal.show();
    }
});
