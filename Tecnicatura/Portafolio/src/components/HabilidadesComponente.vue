<script setup>
//Se importa ref de vue para poder usarlo
import { ref } from 'vue';
//Se crea un array de objetos con las habilidades
//Este es un array de objetos con habilidades que se pueden modificar o agregar
const habilidades = ref([
    {// Se crea un objeto con id, nombre y habilidades
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            //Se crea un objeto con id, nombre, nivel e icono
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: '/src/components/icons/js.svg' },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: '/src/components/icons/python.svg' },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: '/src/components/icons/html-css.svg' },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: '/src/components/icons/java.svg' },
            { id: 5, nombre: 'SQL', nivel: 'Avanzado', icono: '/src/components/icons/sql.svg' }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: '/src/components/icons/react.svg' },
            { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: '/src/components/icons/vue.svg' },
            { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: '/src/components/icons/node.svg' },
            { id: 4, nombre: 'Django', nivel: 'Intermedio', icono: '/src/components/icons/django.svg' },
            { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: '/src/components/icons/bootstrap.svg' }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: '/src/components/icons/git.svg' },
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: '/src/components/icons/docker.svg' },
            { id: 3, nombre: 'Cypress', nivel: 'Intermedio', icono: '/src/components/icons/cypress.svg' },
            { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: '/src/components/icons/figma.svg' },
            { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: '/src/components/icons/visual.svg' }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: '/src/components/icons/mongo.svg' },
            { id: 2, nombre: 'MySQL', nivel: 'Avanzado', icono: '/src/components/icons/mysql.svg' },
            { id: 3, nombre: 'PostgreSQL', nivel: 'Avanzado', icono: '/src/components/icons/postgres.svg' }
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: '/src/components/icons/arg.svg' },
            { id: 2, nombre: 'Inglés', nivel: 'Avanzado (C1)', icono: '/src/components/icons/eeuu.svg' }
        ]
    }
]);
</script>

<template>
    <!--Este componente vue funciona de esta forma:-->
    <div class="skills-contenedor">
        <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <!--Se muestra el nombre de la habilidad-->
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <!--Se recorre el array habilidades con v-for y se asigna la key habilidad.id-->
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <!--Se muestra el icono de la habilidad y el nombre de la habilidad con su nivel-->
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>

    
</template>