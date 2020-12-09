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
      <!-- Content ... -->
    </section>
    <footer class="modal-card-foot">
      <button class="button is-success">Save changes</button>
      <button class="button" @click='closeModal' >Cancel</button>
    </footer>
  </div>
</div>
</div>
</template>
<script lang="ts">
import {ref} from 'vue';
export default {

    setup() {
        const display = ref(false);

        const openModal = () => {
            display.value = true;
        }

        const closeModal = () => {
            display.value = false;
        }

        return {
            openModal,
            closeModal,
            display
        }

    }
}
</script>