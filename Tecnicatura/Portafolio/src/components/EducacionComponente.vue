<script setup>
import { ref } from 'vue';
const fechaColor = ref([]);
/*Esta es otra forma de utilizar el arreglo, con el metodo value*/
fechaColor.value = [
  {color: '#41516c'},
  {color: '#FBCA3E'},
  {color: '#E24A68'},
  {color: '#1B5F8C'},
  {color: '#4CADAD'}
];
/*Esta es la forma de utilizar el arreglo, sin el metodo value*/
const educacion = ref([
  {fecha: '2024', title: 'Técnicatura Universitaria en Programacion UTN San Rafael', descripcion: 'Trabajamos con metodologias scrum, aprendimos Python, Java, Javascript, MYSQL entre otros lenguajes.', enlace:'https://www.youtube.com/'},
  {fecha: '2023', title: 'Desarrollador Full Stack', descripcion: 'Trabajé en RollingCode, donde diseñé y desarrollé aplicaciones web completas utilizando tecnologías como Node.js, React y MongoDB.', enlace:'http:www.direccion.com'},
  {fecha: '2022', title: 'Internship en Desarrollo Web', descripcion: 'Realicé una pasantía en ABC Solutions, contribuyendo en la creación de interfaces de usuario y optimización de sitios web.', enlace:'http:www.direccion.com'},
  {fecha: '2021', title: 'Proyecto Personal - Aplicación de Gestión de Tareas', descripcion: 'Desarrollamos una aplicación para la gestión de tareas diarias usando HTML, CSS y JavaScript, implementando funcionalidades como listas de tareas y recordatorios.', enlace:'http:www.direccion.com'},
  {fecha: '2020', title: 'Curso de Introducción a la Programación', descripcion: 'Completé un curso en línea sobre fundamentos de programación, donde aprendí lenguajes como Python y Java.', enlace:'http:www.direccion.com'}
]);
</script>

<template>
    <ul>
        <li v-for="(item, index) in educacion" :key="index" :style="{ '--fecha-color': fechaColor[index].color}">
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.title }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
        <!--Aqui vemos con el uso de b-vind (:) que bindeamos el atributo href de html con el item.enlace-->
        <a class="enlace" :href="item.enlace" target="_blank">Saber más</a>
    </li>
    </ul>
</template>

<style scoped>
/* Estilos generales */
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap");
/* Reseteo de estilos básicos para todos los elementos y pseudo-elementos */
*,
*::before,
*::after {
  margin: 0; /* Elimina el margen predeterminado */
  padding: 0; /* Elimina el padding predeterminado */
  box-sizing: border-box; /* Incluye el padding y el borde en el tamaño total del elemento */
}

/* Estilo para el cuerpo de la página */
body {
  --color: rgba(30, 30, 30); /* Variable para el color de texto */
  --bgColor: rgba(245, 245, 245); /* Variable para el color de fondo */
  min-height: 100vh; /* Asegura que el cuerpo ocupe al menos el 100% de la altura de la ventana */
  display: grid; /* Utiliza el modelo de caja de cuadrícula */
  align-content: center; /* Centra verticalmente el contenido dentro de la cuadrícula */
  gap: 2rem; /* Espaciado entre los elementos de la cuadrícula */
  padding: 2rem; /* Espaciado interno alrededor del cuerpo */
  font-family: "Poppins", sans-serif; /* Fuente para todo el texto en la página */
  color: var(--color); /* Aplica el color de texto definido en la variable */
  background: var(--bgColor); /* Aplica el color de fondo definido en la variable */
}

/* Estilos para la lista */
ul {
    margin-top: 2rem;
  --col-gap: 2rem; /* Espacio entre las columnas de la cuadrícula */
  --row-gap: 2rem; /* Espacio entre las filas de la cuadrícula */
  --line-w: 0.25rem; /* Ancho de la línea que conecta los elementos de la lista */
  display: grid; /* Usa un layout de cuadrícula */
  grid-template-columns: var(--line-w) 1fr; /* Define las columnas de la cuadrícula: la primera es la línea y la segunda es el contenido */
  grid-auto-columns: max-content; /* Las columnas se ajustan automáticamente al contenido */
  column-gap: var(--col-gap); /* Espacio entre las columnas */
  list-style: none; /* Elimina las viñetas predeterminadas de la lista */
  width: min(60rem, 90%); /* Limita el ancho de la lista al mínimo entre 60rem y el 90% del ancho de la ventana */
  margin-inline: auto; /* Centra la lista horizontalmente */
}

/* Estilo para la línea vertical que conecta los elementos de la lista */
ul::before {
  content: ""; /* Elemento vacío para crear la línea */
  grid-column: 1; /* Coloca la línea en la primera columna de la cuadrícula */
  grid-row: 1 / span 20; /* La línea se extiende sobre varias filas */
  background: rgb(225, 225, 225); /* Color de la línea */
  border-radius: calc(var(--line-w) / 2); /* Bordes redondeados para la línea */
}

/* Estilo para los elementos de la lista que no son el último */
ul li:not(:last-child) {
  margin-bottom: var(--row-gap); /* Espacio entre los elementos de la lista */
}

/* Estilo para cada ítem de la lista */
ul li {
  grid-column: 2; /* Coloca el contenido en la segunda columna de la cuadrícula */
  --inlineP: 1.5rem; /* Espacio interno horizontal dentro de cada ítem */
  margin-inline: var(--inlineP); /* Margen horizontal para los ítems */
  grid-row: span 2; /* Cada ítem ocupa dos filas en la cuadrícula */
  display: grid; /* Usa un layout de cuadrícula dentro de cada ítem */
  grid-template-rows: min-content min-content min-content; /* Define tres filas de altura mínima */
}