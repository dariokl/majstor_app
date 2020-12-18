<template>
  <div class="container">
    <div class="box contain-card">
      <div class="card-title">
        <h4>Usluge/Zanimanja & Potvrde</h4>
        <div class="button-wrapper">
          <Button icon="pi pi-plus" @click.prevent="openModal"></Button>
        </div>
      </div>
      <div class="about-body mt-1"></div>
      <div v-for="(skill, index) in skillsdata" :key="index">
        <div class="mt-2 columns is-multiline is-mobile">
          <div class="column is-one-quarter">
            <div v-if="skill.type.name == 'Diploma'">
              <i class="mt-5 pi pi-file-o usluge" style="fontSize: 2rem" />
            </div>
            <div v-else>
              <i class="mt-5 pi pi-bars usluge" style="fontSize: 2rem" />
            </div>
          </div>
          <div class="column is-auto has-text-left">
            <h1>
              <strong>{{ skill.name }}</strong>
            </h1>
            <span> {{ skill.type.name }} </span><br />
            <span>Godina: {{ skill.date.date }}</span>
            <p>{{ skill.description }}</p>
          </div>
          <div class="column is-one-quarter">
            <div class="dropdown is-right" :id="+index" :class="{'is-active': index === render}">
  <div class="dropdown-trigger">
      <Button icon="pi pi-trash" class="p-button-rounded p-button-text" aria-haspopu="true" :aria-controls=" 'dropdown-menu_'+ index " @click='editModal(index)' 
      style='color: #4a4a4a;' />
  </div>
  <div class="dropdown-menu" :id=" 'dropdown-menu_'+ index " role="menu">
    <div class="dropdown-content">
      <div class="dropdown-item">
        <div class="button-wrappper">
          <div class="columns">
            <div class="column">
              <i class="pi pi-info" aria-haspopu="true" aria-controls='dropdown-menu2'/>
              <span> Potvrdite brisanje unosa ! </span>
            </div>
          </div>
          <Button icon="pi pi-check" class="p-button-rounded p-button-text" @click.prevent='deleteSkillEmitter'/>
          <Button icon="pi pi-times" class="p-button-rounded p-button-danger p-button-text" @click.prevent='closeP1Modal' />
          
        </div>
      </div>

    </div>
  </div>
</div>
            
          </div>
        </div>
        <hr type="solid" />
      </div>
    </div>
    <div class="mt-5 modal" :class="{ 'is-active': display }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Usluge/Zanimanja & Potvrde</p>
          <button class="delete" aria-label="close"></button>
        </header>
        <section class="modal-card-body">
          <div class="column">
            <p style="text-align: center">
              Istaknite neke vaznije dokumente vezane za vasu firmu/obrt ili pak
              Vasu licnu diplomu, uvjerenje u strucnoj spremi i duroge slicne
              dokumente a u cilju da posjetitelje vaseg profila uvjerite u
              strucnost i provjernost Vasih usluga i znanja.
            </p>
            <hr type="solid" />
          </div>
          <div class="container">
            <div class="column is-12">
              <div class="p-inputgroup">
                <span class="p-inputgroup-addon">
                  <i class="pi pi-briefcase"></i>
                </span>
                <span class="p-float-label">
                  <InputText
                    id="skillName"
                    type="text"
                    v-model="loadSkill.name"
                  />
                  <label for="skillName"
                    >Vrsta usluge * (npr. Projektiranje stabmenih objekata )
                  </label>
                </span>
              </div>
            </div>
            <div class="column is-12">
              <div class="p-inputgroup">
                <span class="p-inputgroup-addon">
                  <i class="pi pi-file-o"></i>
                </span>
                <span class="p-float-label">
                  <Dropdown
                    :options="skillType"
                    optionLabel="name"
                    id="skillType"
                    v-model="loadSkill.type"
                  />
                  <label for="skillType">Vrsta Potvrde* </label>
                </span>
              </div>
            </div>
            <div class="column is-12">
              <div class="p-inputgroup">
                <span class="p-inputgroup-addon">
                  <i class="pi pi-calendar"></i>
                </span>
                <span class="p-float-label">
                  <Dropdown
                    id="skillDate"
                    :options="getYear()"
                    optionLabel="date"
                    v-model="loadSkill.date"
                  />
                  <label for="skillDate"
                    >Godina sticanja diplome/sertifikata *
                  </label>
                </span>
              </div>
            </div>
            <div class="column is-12">
              <div class="p-inputgroup">
                <span class="p-inputgroup-addon">
                  <i class="pi pi-align-center"></i>
                </span>
                <span class="p-float-label">
                  <Textarea
                    id="skillDescription"
                    v-model="loadSkill.description"
                  />
                  <label for="skillDescription"
                    >Recite nam nesto vise o vasem diplomi/certifikatu*
                  </label>
                </span>
              </div>
            </div>
          </div>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-success" @click="push(loadSkill)">
            Save changes
          </button>
          <button class="button" @click.prevent="closeModal">Cancel</button>
        </footer>
      </div>
    </div>

    
  </div>
</template>
<script lang="ts">
import Vue from "vue";
import { ref } from "vue";
export default {
  props: ["skillsdata"],
  emits: ["skills", 'check', 'deleteskills'],
  setup(props: any, { emit }: any) {
    const display = ref(false);
    const checked = ref(false);
    const modalP1 = ref(false)
    const render = ref(null)
    const drop = ref(null)

  


    const openModal = () => {
      display.value = true;
    };

    const closeModal = () => {
      display.value = false;
    };

    const checkCert = () => {
      checked.value = true;
    };

    const skillType = [{ name: "Diploma" }, { name: "Sertifikat" }];

    const getYear = () => {
      const currentYear = new Date().getFullYear();
      const years: {}[] = [];
      let startYear = 1970;
      for (let i = startYear; i <= currentYear; i++) {
        years.push({ date: startYear++ });
      }
      return years;
    };

    const loadSkill = ref({ name: "", type: "", date: "", description: "" });

    const push = (payload: any) => {
      emit("skills", loadSkill.value);
      loadSkill.value = { name: "", type: "", date: "", description: "" };
    };

    const editModal = (payload: number) => {
      render.value = payload
    }

    const deleteSkillEmitter = () => {
      emit('deleteskills', render)
      render.value = null
    }

    const closeP1Modal = () => {
      render.value = null
    }


    return {
      openModal,
      closeModal,
      display,
      checked,
      checkCert,
      skillType,
      getYear,
      loadSkill,
      push,
      editModal,
      modalP1,
      render,
      deleteSkillEmitter,
      closeP1Modal,
      drop
    };
  },
};
</script>
