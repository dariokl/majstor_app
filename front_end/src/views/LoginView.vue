<template>
<div class="mt-6 container">
<form class='' method='POST' @submit.prevent='login(loginDetail)'>
  <input type='text' v-model='loginDetail.email'>
  <input type='password' v-model='loginDetail.password'>
<button type='submit'>Click</button>
<p>{{errorMessage}}</p>

<button @click.prevent='logout()'/>


</form>
</div>
</template>
<style scoped>
form {
  padding-top: 5rem;
}
</style>
<script lang="ts">
import UserWork from '@/modules/user.ts'
import {ref} from 'vue';
export default{
  setup() {
    const loginDetail = ref({email: '', password: ''})

    const {login, errorMessage, logout} = UserWork()

 

    return { loginDetail, login, errorMessage, logout}
  }
}
</script>