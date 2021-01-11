<template>
<div class="view-p">
<div class="container">


<div v-for='user in users.users' :key='user.id' class="mt-6 colum">
<div class="box">
  <article class="media">
    <div class="media-left">
      <figure class="image is-128x128">
        <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
      </figure>
    </div>
    <div class="column has-text-left" style='display: flex;'>
    <div class="media-content meta-left">
      <div class="content">
        <p style=''>
          <span class='company-name'>{{user.company_name}}</span> 
          <br>
          <span><small>{{user.entity}}</small>, <small>{{user.city}}</small>, <small>{{user.address}}</small></span>
          <br>
          <i class='idot mt-3 pi pi-circle-off' style='fontSize: 0.7rem;' />
          <span class='dot'> 3 </span>
                    <i class='ml-5 idot mt-3 pi pi-circle-off' style='fontSize: 0.7rem;' />
          <span class='dot'> 3 </span>
                    <i class='ml-5 idot mt-3 pi pi-circle-off' style='fontSize: 0.7rem;' />
          <span class='dot'> 3 </span>
            <br>
          <i class='bottom-dot mt-4 pi pi-user' />
            <span class='bottom-dot'> Profile </span>
                      <i class='ml-5 bottom-dot mt-4 pi pi-facebook' />
            <span class='bottom-dot'> Facebook </span>
                                  <i class='ml-5 bottom-dot mt-4 pi pi-inbox' />
            <span class='bottom-dot'> Poruka </span>
          <br>
        </p>
        </div>
    </div>
    <div class="meta-right">
                                                <div class="buttons">
              <Button
                label="Plain"
                class="p-button p-component p-button-raised p-button-text"
              />
            <Button label="Success" class="p-button-raised ml-2 p-button-success" />
                                                </div>
                                            </div>

                                         

    </div>

  </article>
</div>
</div>

</div>
</div>
                                    
 
</template>

<script lang="ts">
import Vue from 'vue';
import {onMounted, ref} from 'vue'
import {useRoute} from 'vue-router';
import axios from 'axios';
import UserWork from '@/modules/user.ts'
export default {
    setup () {
        const a = 10;
        const b = ref('a')
        const route = useRoute()
        const {users} = UserWork()

            onMounted(() => {
      axios.post('http://127.0.0.1:8000/q', {q: route.params.search})
      .then((response) =>
      users.value = response.data)
    })


        return {
            a,
            b,
            users
        }
        
    }

}
</script>

<style scoped>
.view-p {
    height: 100vh;
}

.media-left {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    margin-left: 16px;
}

p {
    font-size: .95rem;
    color: #9fa4c9;
}

.company-name {
    font-size: 1.6rem;
font-family: "Montserrat", sans-serif;
font-weight: bold;
color: #393a4f;
line-height: 1.2;
font-style: inherit;
font-weight: inherit;
}

.idot {
font-size: .9rem;
color: #6895c2;
}

.dot {
font-family: "Montserrat",sans-serif;
font-size: .9rem;
color: #6895c2;
}
.bottom-dot {
font-size: .85rem;
color: #283252;

}
.meta-left {
    display: flex;
    -webkit-box-orient: vertical;
    -webkit-box-direction: normal;
    -ms-flex-direction: column;
    flex-direction: column;
    margin-left: 16px;
}

.meta-right {
    margin-left: auto;
display: -webkit-box;
display: -ms-flexbox;
display: flex;
-webkit-box-align: center;
-ms-flex-align: center;
align-items: center;
-webkit-box-pack: end;
-ms-flex-pack: end;
justify-content: flex-end;
}
</style>