<template>
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
          <div v-if='errorMessage' class="column has-text-right">
            <p> {{errorMessage}}</p>

          </div>
          <div v-else class="column has-text-left">
     
<div class="hover-effect3" style='height: 0px'>
	<ul>
    
		<li ><a v-if='user.message_counter > 0' href="#." title="Facebook">  <i class="pi pi-envelope p-text-secondary" style="font-size: 1.2rem" v-badge.success=""></i></a>
    <a v-else href="#." title="Facebook">  <i class="pi pi-envelope p-text-secondary" style="font-size: 1.2rem" ></i></a></li>
    		
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

.do-it {
  background: red;
}
</style>
<script lang='ts'>
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import Home from 'Home.vue';
import UserWork from '@/modules/user.ts'

export default {
  setup() {
    const checking = ref(false);

    const {currentUser, errorMessage, user} = UserWork()

    onMounted(() => {
      currentUser();
    });

    const simple = ref(false)

    function messageCounter() {
      if (user.value.messageCounter > 0)
      return true
      else {
        return false
      }
    }

    function closeMenu() {
      checking.value = false;
    }

    return {
      closeMenu,
      checking,
      errorMessage,
      messageCounter,
      user,
      simple
    };
  }
};
</script>