<template>
<div class="">
    <i class='pi pi-plus' @click='openModal()' />
    <div class="modal" :class="{'is-active': display}">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Modal title</p>
      <button class="delete" aria-label="close"></button>
    </header>
    <section class="modal-card-body">
                                  <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-user"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="lastName"
                                    type="text"
                                    v-model="loadHistory.date"
                                    
                                    v-bind:class="{
                                      'p-filled': loadHistory.date,
                                    }"
                                  />
                                  <label for="lastName">Prezime * </label>
                                </span>
                              </div>
                            </div>
                            
      <InputText v-model='loadHistory.date'/>
      <InputText v-model='loadHistory.description'/>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-success" @click='push(loadHistory)'>Save changes</button>
      <button class="button" @click='closeModal' >Cancel</button>
    </footer>
  </div>
</div>
</div>
</template>
<script lang="ts">
import {ref} from 'vue';
export default {
  props: ['history'],

    setup(props: any , {emit} : any) {
        const display = ref(false);

        const openModal = () => {
            display.value = true;
        }

        const closeModal = () => {
            display.value = false;
        }

        const loadHistory = ref({date : '', description: ''})

        const push = (payload: any) => {
          console.log(loadHistory.value)
          emit('user-history', loadHistory.value)
          loadHistory.value = {date: '', description: ''}
        }

        return {
            openModal,
            closeModal,
            display,
            loadHistory,
            push
        }

    }
}
</script>