<template>
  <div class="box contain-card">
    <div class="card-title ">
      <h4>Halo</h4>
      <div class="button-wrapper">
        <Button icon="pi pi-plus" @click.prevent="openModal"></Button>
      </div>
    </div>
    <div class="about-body mt-1">
      <div v-if="check">
        <div class="columns is-gapless">
          <div v-for="(project, index) in projects" :key="project.name">
            <div
              class="mx-1 column has-overlay"
              :id="index"
              @click="checkModal(index)"
            >
              <img
                src="https://tedswoodworkingreview2018.com/wp-content/uploads/2017/10/Wood-Wednesday.jpg"
              />
              <div class="portfolio-overlay">
                <div class="portfolio-icon">
                  <i
                    class="pi pi-external-link buzz-out-on-hover"
                    style="fontSize: 1rem"
                  />
                  <br />
                  <span>click za informacije</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-else>
        <h4>Podjelite vase radove sa nama !</h4>
        <div class="column upload">
          <i @click.prevent="openModal" class="pi pi-image" style="fontSize: 5rem"></i>
        </div>
      </div>
    </div>
    <div class="modal" v-bind:class="{ 'is-active': display }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title">Modal title </p>
          <button
            class="delete"
            aria-label="close"
            @click.prevent="closeModal"
          ></button>
        </header>
        <section class="modal-card-body">
          <FileUpload name="demo[]" v-on:change="fileHandle()" ref="file">
            <template #empty>
              <p>Drag and drop files to here to upload.</p>
            </template> </FileUpload
          >
          <div v-if='message'>
        <Message>{{message}}</Message>
          </div>
          
        </section>
        <footer class="modal-card-foot">
  
          <button class="button is-success">Save changes</button>
          <button class="button">Cancel</button>
        </footer>
      </div>
    </div>

    <div v-if='check' class="modal p1" v-bind:class="{ 'is-active': modalP1 }">
      <div class="modal-background"></div>
      <div class="modal-card">
        <header class="modal-card-head">
              <p class="modal-card-title">{{projects[render].name}}</p>
          <button
            class="delete"
            aria-label="close"
            @click.prevent="closeModal1"
          ></button>
        </header>


        <section class="modal-card-body">
                  <div class="columns">
                    <div class="column is-8 border-it">
            <img src='https://tedswoodworkingreview2018.com/wp-content/uploads/2017/10/Wood-Wednesday.jpg'>
          </div>
          <div class="column card-contain">
            <p style='text-align: left;'>{{projects[render].description}}</p>
            <span style='text-align: left'> Cijena: {{projects[render].price}}</span>
          </div>
        </div>
        </section>
        <footer class="modal-card-foot">
          {{projects[render].id}}
          <button class="button is-danger" @click.prevent='deletePost(projects[render].id)'>Obrisi Objavu</button>
          <button class="button" @click.prevent="closeModal1">Nazad</button>
        </footer>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import axios from "axios";
import Vue from "vue";
import { onMounted, ref } from "vue";

interface DeletePortfolio {
  id: number
}
export default {
  name: "Protfolio",
  props: ["projects", "images", 'check'],
  emtis: ['handlePortfolio'],
  setup(props: any, {emit}: any) {
    /** Used in process of saving first images to the user profile display reffers to the modal that is used for inital image uploading  */
    const display = ref(false);
    const file = ref(null);
    const message = ref('')

    /** modalP1 is used to render the projects that user decided to upload , render is simply returning value to the list of projects
     * so the application gets the right index number to index to project inside the list of projects.
     */
    const modalP1 = ref(false);
    const render = ref(0);

    /** Simple modal function to cancel and open */
    const openModal = () => {
      display.value = true;
    };

    const closeModal = () => {
      display.value = false;
    };

    /** Used for saftey after openning the rendering modal , probabblity uncessary on the long run */
    const closeModal1 = () => {
      modalP1.value = false;
    };

    /** Simply changing the render const so we can render the right project to user  */
    const checkModal = (index: any) => {
      console.log(index);
      modalP1.value = true;
      render.value = index;
      return index;
    };

    /**
     * FileHandle is core of this view , it allows users to add new project picture , and new project data.
     */

    const fileHandle = () => {
      const formData = new FormData();
      formData.append("file", file.value.files[0]);
      axios
        .post("http://127.0.0.1:8000/users/uploadfile/", formData)
        .then((response) => {
          emit('handle-portfolio')
          message.value = ''

        })
        .catch((error: any) => {
          message.value = error.response.data.detail

        });
    };

    const deletePost = (payload: any) => {

      axios.delete("http://127.0.0.1:8000/users/delete-post/",{data : {id: payload}})
      .then((response) => {
        emit('handle-portfolio')
      })
    }



    return {
      openModal,
      closeModal,
      display,
      file,
      fileHandle,
      modalP1,
      closeModal1,
      checkModal,
      render,
      message,
      deletePost
    };
  },
};
</script>
