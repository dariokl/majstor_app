<template>
<head>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
</head>
<div class="page-header">

  <input id="menu-toggle-input" type="checkbox" v-model="checking" />
  <label class="menu-toggle" for="menu-toggle-input">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </label>
        <div class="container">
          <div class="colum has-text-left">
     
<div class="hover-effect3">
	<ul>
		<li><a href="#." title="Facebook">  <i class="pi pi-envelope p-text-secondary" style="font-size: 1.2rem" v-badge.success=""></i></a></li>
		<li><a href="#." title="Twitter">  <i class="pi pi-bell p-text-secondary" style="font-size: 1.2rem" v-badge.success=""></i></a></li>
		<li><a href="#." title="Google Plus"><i class="pi pi-comment p-text-secondary" style="font-size: 1.2rem" v-badge.success=""></i></a></li>
    <li>
    </li>
	</ul>
</div>
          </div>
         
          
        </div>
  <nav class="menu">
    <ol>
      <li class="menu-item" @click.prevent="closeMenu">
        <router-link to="/">Home</router-link>
      </li>
      <li class="menu-item" @click.prevent="closeMenu">
        <router-link to="/about">About</router-link>
      </li>
      <li class="menu-item">
        <a href="#0">Widgets</a>
        <ol class="sub-menu">
          <li class="menu-item" @click.prevent='closeMenu'><router-link to='/profile'>Profile</router-link></li>
          <li class="menu-item"><a href="#0">Bigger Widgets</a></li>
          <li class="menu-item"><a href="#0">Huge Widgets</a></li>
        </ol>
      </li>
      <li class="menu-item">
        <a href="#0">Kabobs</a>
        <ol class="sub-menu">
          <li class="menu-item"><a href="#0">Shishkabobs</a></li>
          <li class="menu-item"><a href="#0">BBQ kabobs</a></li>
          <li class="menu-item"><a href="#0">Summer kabobs</a></li>
        </ol>
      </li>
      <li class="menu-item"><a href="#0">Contact</a></li>
    </ol>
  </nav>
  </div>
  <router-view />
</template>

<style lang='scss'>
@import "./assets/css/nav.css";
@import "./assets/css/main.css";
@import "~bulma/bulma";



#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: blue;
}

$primaryColor: red;
</style>

<script lang='ts'>
import { useRoute } from "vue-router";
import { ref } from "vue";

export default {
  setup() {
    const checking = ref(false);

    function closeMenu() {
      checking.value = false;
    }

    return {
      closeMenu,
      checking
    };
  }
};
</script>