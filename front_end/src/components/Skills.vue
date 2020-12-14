<template>
  <div class="container">
    <div class="box contain-card">
      <div class="card-title ">
        <h4>Usluge/Zanimanja & Potvrde</h4>
        <div class="button-wrapper">
          <Button icon="pi pi-plus" @click.prevent="openModal"></Button>
        </div>
      </div>
      <div class="about-body mt-1">
         
      </div>
    </div>
    <div class="modal" :class="{'is-active' : display}">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Modal title</p>
      <button class="delete" aria-label="close"></button>
    </header>
    <section class="modal-card-body">
        <div class="container">
                <div class="column is-12 ">
          <div class="p-inputgroup">
            <span class="p-inputgroup-addon">
              <i class="pi pi-briefcase"></i>
            </span>
            <span class="p-float-label">
              <InputText
                id="skillName"
                type="text"
              />
              <label for="skillName">Vrsta usluge * (npr. Projektiranje stabmenih objekata  ) </label>
            </span>
          </div>
        </div>
                <div class="column is-12">
                      <div class="p-inputgroup">
            <span class="p-inputgroup-addon">
              <i class="pi pi-check"></i>
            </span>
            <span class="p-float-label">
              <InputText
                id="skillDiploma"
                type="text"
              />
              <label for="skillDiploma">Diploma ili sertifikat vezan za zanimanje (npr. ISO Sertifikat...) </label>
            </span>
          </div>

   
</div>
                          <div class="columns is-multiline">
                            <div class="column is-6">
           
                              <div class="p-field-checkbox">
    <Checkbox id="city1" name="city" value="Chicago" v-model="checked" />
    <label for="city1">Sertifikat</label>
</div>

                                  
                                
                              </div>
                                                          <div class="column is-6">
           
               <div class="p-field-checkbox">
    <Checkbox id="city2" name="city" value="Los Angeles" v-model="checked" />
    <label for="city2">Diploma</label>
</div>
                                  
                                
                              </div>
                            </div>



</div>
    </section>
    <footer class="modal-card-foot">
      <button class="button is-success">Save changes</button>
      <button class="button" @click.prevent='closeModal'>Cancel</button>
    </footer>
  </div>
</div>
  </div>
</template>
<script lang="ts">
import Vue from "vue";
import {ref} from 'vue';
export default {
  setup(props: any, { emit }: any) {
    const display = ref(false);
    const checked = ref(false)
    const value = ref(null)
    const cities = ref([])

    const openModal = () => {
      display.value = true;
    };

    const closeModal = () => {
      display.value = false;
    };

    const checkCert = () => {
        checked.value = true;
    }


    return {
      openModal,
      closeModal,
      display,
      checked,
      checkCert,
      value,
      cities
    };
  },
};
</script>
