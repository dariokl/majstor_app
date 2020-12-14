<template>
  <i class="pi pi-plus" @click.prevent="openModal()" />
  <div class="modal" :class="{ 'is-active': display }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title"></p>
        <button class="delete" aria-label="close" @click.prevent="closeModal"></button>
      </header>
      <section class="modal-card-body">
        <div class="contaner-box">
          <h4>License & Dostignuća</h4>
          <hr />
        </div>

        <div class="column is-12 ">
          <div class="p-inputgroup">
            <span class="p-inputgroup-addon">
              <i class="pi pi-calendar"></i>
            </span>
            <span class="p-float-label">
              <InputText
                id="historyDate"
                type="text"
                v-model="loadHistory.date"
                v-bind:class="{
                  'p-filled': loadHistory.date,
                }"
              />
              <label for="historyDate">Godina * </label>
            </span>
          </div>
        </div>
        <div class="column is-12 ">
          <div class="p-inputgroup">
            <span class="p-inputgroup-addon">
              <i class="pi pi-align-center"></i>
            </span>
            <span class="p-float-label">
              <Textarea
                id="historyDescription"
                v-model="loadHistory.description"
                v-bind:class="{
                  'p-filled': loadHistory.description,
                }"
              />
              <label for="historyDescription">Opis * </label>
            </span>
          </div>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click.prevent="push(loadHistory)">
          Save changes
        </button>
        <button class="button" @click.prevent="closeModal">Cancel</button>
      </footer>
    </div>
  </div>
</template>
<script lang="ts">
import { ref } from "vue";
export default {
  props: ["history"],
  emits: ["history"],

  setup(props: any, { emit }: any) {
    const display = ref(false);

    const openModal = () => {
      display.value = true;
    };

    const closeModal = () => {
      display.value = false;
    };

    const loadHistory = ref({ date: "", description: "" });

    const push = (payload: any) => {
      emit("history", loadHistory.value);
      loadHistory.value = { date: "", description: "" };
    };

    return {
      openModal,
      closeModal,
      display,
      loadHistory,
      push,
    };
  },
};
</script>
