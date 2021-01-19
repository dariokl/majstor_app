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
    <div  class="container" style='bottom: 15px;'>
      <div v-if="user.loggedIn === false"  class="column has-text-right">
        <p>{{ errorMessage }}</p>
       
      </div>
      <div v-else class="column has-text-left">
        <div else class="hover-effect3" style="height: 0px">
          <ul>
            <li>
              <a v-if="user.message_counter > 0" href="#." title="Facebook" @click.prevent='inboxq(inboxM), openInbox()'>
                <div class="mt-5 dropdown is-left" :class="{'is-active': inboxM}">

  <div v-if='loading === true' class="dropdown-menu" id="dropdown-menu6" role="menu">
<Skeleton />
<Skeleton />
  </div>
    <div v-else class="dropdown-menu" id="dropdown-menu6" role="menu" style='border-top: 10px solid #f5faff;'>

      
  </div>
</div>

                <i
                  class="pi pi-envelope p-text-secondary"
                  style="font-size: 1.2rem"
                  v-badge.success=""
                ></i
              ></a>
              <a v-else href="#." title="Facebook">
                <i
                  class="pi pi-envelope p-text-secondary"
                  style="font-size: 1.2rem"
                ></i
              ></a>
            </li>

            <li>
              <a href="#." title="Twitter">
                <i
                  class="pi pi-bell p-text-secondary"
                  style="font-size: 1.2rem"
                  v-badge.success=""
                ></i
              ></a>
            </li>
            <li>
              <a href="#." title="Google Plus"
                ><i
                  class="pi pi-comment p-text-secondary"
                  style="font-size: 1.2rem"
                  v-badge.success=""
                ></i
              ></a>
            </li>

            <li></li>
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
            <li class="menu-item" @click.prevent="closeMenu">
              <router-link to="/profile">Profile</router-link>
            </li>
              <li class="menu-item" @click.prevent="closeMenu">
              <router-link to="/inbox">Inbox</router-link>
            </li>
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

<style lang="scss">
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
<script lang="ts">
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import Home from "Home.vue";
import UserWork from "@/modules/user.ts";

export default {
  setup() {
    const checking = ref(false);
    const inboxM= ref(false)

    const { currentUser, errorMessage, user, inboxq, loading} = UserWork();

    onMounted(() => {
       currentUser();
    });

    const openInbox = () => {
      inboxM.value = !inboxM.value
    }


    function closeMenu() {
      checking.value = false;
    }


    return {
      closeMenu,
      checking,
      errorMessage,
      user,
      inboxq,
      inboxM,
      openInbox,
      loading
    };
  },
};
</script>
