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

</template>