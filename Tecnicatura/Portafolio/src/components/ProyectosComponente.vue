<script setup>
// Este componente muestra una galería de proyectos con información sobre cada proyecto
import { ref } from 'vue';
//.ref es una función que se utiliza para crear una referencia reactiva en Vue 3
var misProyectos = ref([]);
//.value es una propiedad que se utiliza para acceder al valor de una referencia reactiva en Vue 3
misProyectos.value = ([
    //esto es un array de objetos que contiene información sobre los proyectos
    {
        id: 1,
        src: "./src/assets/restaurant.png",
        titulo: "Aplicación de Reservas para Restaurantes (2023)",
        descripcion: "Creamos una aplicación móvil con Flutter que permite a los usuarios reservar mesas en restaurantes locales",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 2,
        src: "./src/assets/e-learning.png",
        titulo: "Plataforma de E-learning (2022)",
        descripcion: "Diseñamos y desarrollamos una plataforma de educación en línea utilizando Django y React. Con diferentes funcionalidades",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 3,
        src: "./src/assets/blog.png",
        titulo: "Blog Personal con CMS (2022)",
        descripcion: "Construímos un blog personal con un sistema de gestión de contenidos (CMS) personalizado en WordPress.",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
    {
        id: 4,
        src: "./src/assets/restaurant.png",
        titulo: "Aplicación de Reservas para Restaurantes (2023)",
        descripcion: "Creamos una aplicación móvil con Flutter que permite a los usuarios reservar mesas en restaurantes locales",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://github.com/usuario/proyecto"
    },
])

</script>

<template>
    <!-- Aquí va el código HTML de la galería de proyectos -->
    <div class="galeria">
        <!-- Itera sobre cada proyecto en la lista de misProyectos -->
        <!--key es una propiedad especial que se utiliza para identificar de forma única cada elemento en una lista de Vue.js-->
        <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
            <!-- Muestra la imagen del proyecto utilizando : que es una directiva de enlace de atributo en Vue.js -->
            <img :src="proyecto.src" :alt="proyecto.titlulo">
            <div class="proyecto-info">
                <!-- Muestra el título y la descripción del proyecto utilizando la interpolación de Vue.js -->
                <h3>{{ proyecto.titulo }}</h3>
                <p>{{ proyecto.descripcion }}</p>
                <div class="proyecto-links">
                    <a :href="proyecto.projectoLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver
                        Proyecto</a>
                    <a :href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer">Ver
                        Código en GitHub</a>
                </div>
            </div>
        </li>
    </div>
</template>

<style scoped>
/*Estilo de fondo de la galeria con un fondo estatico */
/* .galeria {
    width: 100%;
    height: 100vh;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    background-image: url('/src/assets/fondo-proyectos.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
} */

/* Estilos Fondo Animado de Css de la galería */
/* La clase 'galeria' es el contenedor principal de la galería de proyectos */
.galeria {
    /* Establece el ancho de la galería al 100% del contenedor padre */
    width: 100%;
    /* Establece la altura de la galería al 100% del contenedor padre */
    height: 100%;
    /* Utiliza flexbox para organizar los elementos hijos en la galería */
    display: flex;
    /* Permite que los elementos se ajusten y pasen a la siguiente línea si no caben en una sola fila */
    flex-wrap: wrap;
    /* Establece un espacio de 20px entre los elementos de la galería */
    gap: 20px;
    /* Agrega un padding de 20px alrededor de la galería */
    padding: 20px;
    /* Centra los elementos hijos horizontalmente */
    justify-content: center;
    /* Aplica un fondo con un degradado de colores */
    background: linear-gradient(-45deg, #021526, #03346E, #6EACDA, #E2E2B6);
    /* Ajusta el tamaño del fondo para que cubra el área completa */
    background-size: 400% 400%;
    /* Aplica una animación al fondo que dura 15 segundos, tiene una transición suave y se repite infinitamente */
    animation: gradient 15s ease infinite;
}

/* Define una animación llamada 'gradient' para cambiar la posición del fondo */
@keyframes gradient {

/* Al inicio, el fondo está posicionado en el 0% horizontal y 50% vertical */
0% {
    background-position: 0% 50%;
}

/* A la mitad de la animación, el fondo se desplaza al 100% horizontal y 50% vertical */
50% {
    background-position: 100% 50%;
}

/* Al final, el fondo vuelve a la posición inicial */
100% {
    background-position: 0% 50%;
}
}