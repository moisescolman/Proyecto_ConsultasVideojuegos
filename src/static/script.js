// script.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-juego');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const titulo = document.getElementById('titulo').value;
        const genero = document.getElementById('genero').value;
        const consola = document.getElementById('consola').value;
        const desarrollador = document.getElementById('desarrollador').value;

        const data = {
            titulo: titulo,
            genero: genero,
            consola_id: consola,
            desarrollador_id: desarrollador
        };

        const res = await fetch('/add_videojuego', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();
        alert(result.mensaje || 'Videojuego añadido');
    });
});
