<template>
  <div class="mt-5 view-p">
    <div class="message" v-if="message">
      <Message> {{ message }}</Message>
    </div>
    <div class="mt-5 container">
      <div class="columns is-multilines no-margin">
        <div class="column is-paddingless">
          <div class="cover-bg">
            <img
              class="cover-image"
              src="https://s27389.pcdn.co/wp-content/uploads/2019/07/digital-transformation-construction-industry-1024x440.jpeg"
              data-demo-src="assets/img/demo/bg/4.jpg"
              alt=""
            />
            <div class="avatar">
              <figure class="image is-128x128">
                <img
                  class="is-rounded"
                  src="https://bulma.io/images/placeholders/128x128.png"
                />
              </figure>
            </div>
            <div class="cover-overlay"></div>
          </div>

          <div class="mt-3 user-men is-hidden-mobile">
            <div class="menu-start">
              <Button
                label="Plain"
                class="p-button p-component p-button-raised p-button-text"
              />
              <Button
                label="Submit"
                class="ml-2 p-button p-component p-button-raised p-button-text"
              />
            </div>
            <div class="menu-end"></div>
          </div>

          <div class="general-tab">
            <div class="subheader-start">
              <span class="">148K</span>
              <span>Followers</span>
            </div>
            <div class="subheader-middle">
              <h2>{{ user.name }} {{ user.last_name }}</h2>
              <strong>
                <span>{{ user.info.title }} </span>
              </strong>
              <br />
              <span class="companyname"> {{ user.company_name }} </span>
              <div class="container-progress">
                <ProgressBar
                  :value="user.profile_completed"
                  style="height: .2em"
                  class="mt-5"
                >
                </ProgressBar>
                <span class="progress-status">
                  Verifikacija profila : {{ user.profile_completed }} %
                </span>
              </div>
            </div>
            <div class="subheader-end is-hidden-mobile"></div>
          </div>
        </div>
      </div>
      <div class="columns has-portrait-padding">
        <div class="mt-1 column is-4">
          <div class="box-heading">
            <h4>Info</h4>
          </div>

          <div class="basic-infos-wrapper">
            <div class="card is-community">
              <h4>Community</h4>
              <div v-if="user.profile_completed == 100" class="flex-block">
                <i class="material-icons">beenhere</i>
                <p><a>Invite your friends</a> to follow this page</p>
              </div>
              <div v-else class="flex-block">
                <i class="pi pi-times"></i>
                <p><a>Invite your friends</a> to follow this page</p>
              </div>
              <div class="flex-block">
                <p>150K people like this page</p>
              </div>
              <div class="flex-block">
                <p>90K people are following this</p>
              </div>
            </div>

            <div class="card is-about">
              <h4>About</h4>
              <div class="flex-block">
                <p><a>Send a Message</a></p>
              </div>
              <div class="flex-block">
                <p><a>Commercial Company</a></p>
              </div>
              <div class="flex-block">
                <p><a>Suggest Changes</a></p>
              </div>
            </div>

            <div class="card is-friendkit">
              <div class="title-wrap">
                <img src="assets/img/logo/friendkit-bold.svg" alt="" />
                <h4>Security</h4>
              </div>
              <p>
                Idem iste, inquam, de voluptate quid sentit? Re mihi non aeque
                satisfacit, et quidem locis pluribus. Consequens enim est et
                post oritur, ut dixi.
              </p>
              <div class="created">
                <span>Page created on May 6th 2019</span>
              </div>
            </div>
          </div>
        </div>

        <div class="column is-8">
          <div class="box-heading">
            <h4>Profil</h4>
            <div class="button-wrap"></div>
          </div>

          <div class="profile-timeline">
            <div class="mt-3 card contain-card">
              <div>
                <div class="card-title">
                  <h4>About</h4>
                  <div class="button-wrapper">
                    <Button icon="pi pi-pencil" @click="openModalEdit"></Button>
                  </div>
                </div>
                <div class="contain-body">
                  <div v-if="user.info.about">
                    <p style="mt-2 white-space: pre-line; text-align: left">
                      {{ user.info.about }}
                    </p>
                  </div>
                  <div v-else>
                    <p style="mt-2 white-space: pre-line; text-align: left">
                      Upisite iformacije o Vama !
                    </p>
                  </div>
                </div>

                <p></p>
              </div>
              <div></div>

              <div class="modal" :class="{ 'is-active': displayEdit }">
                <div class="modal-background"></div>
                <div class="modal-card">
                  <header class="modal-card-head">
                    <p class="modal-card-title">O nama</p>
                    <button class="delete" aria-label="close"></button>
                  </header>
                  <section class="modal-card-body">
                    <p>Upisite sto vise informacija o vama</p>
                    <Textarea
                      v-model="user.info.about"
                      :value="user.info.about"
                      rows="5"
                      cols="50"
                    >
                    </Textarea>
                  </section>
                  <footer class="modal-card-foot">
                    <button
                      class="button is-success"
                      @click="editPayload(user), closeModalEdit()"
                    >
                      Save changes
                    </button>
                    <button class="button" @click="closeModalEdit">
                      Cancel
                    </button>
                  </footer>
                </div>
              </div>
            </div>
            <div class="mt-2 card contain-card top-border">
              <div class="card-title">
                <h4>About {{ user.company }}</h4>
                <div class="button-wrapper">
                  <Button
                    label="Uredi profil"
                    icon="pi pi-external-link"
                    @click="openMaximizable"
                  />
                  <div
                    class="mt-6 modal"
                    v-bind:class="{ 'is-active': display }"
                  >
                    <div class="modal-background"></div>
                    <div class="modal-card">
                      <header class="modal-card-head">
                        <p class="modal-card-title">Uredi profil</p>
                        <button
                          @click="closeMaximizable"
                          class="delete"
                          aria-label="close"
                        ></button>
                      </header>
                      <section class="modal-card-body">
                        <div class="container">
                          <div class="pb-5 columns is-flex is-centered">
                            <figure class="image is-128x128">
                              <img
                                class="is-rounded"
                                src="https://bulma.io/images/placeholders/128x128.png"
                              />
                            </figure>
                          </div>
                          <div class="columns is-multiline">
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-user"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="name"
                                    type="text"
                                    v-model="user.name"
                                    :value="user.name"
                                    :class="{ 'p-filled': user.name }"
                                  />
                                  <label for="name">Ime * </label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-user"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="lastName"
                                    type="text"
                                    v-model="user.last_name"
                                    :value="user.last_name"
                                    v-bind:class="{
                                      'p-filled': user.last_name,
                                    }"
                                  />
                                  <label for="lastName">Prezime * </label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-12">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-info"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="title"
                                    v-model="user.info.title"
                                    :value="user.info.title"
                                    :class="{ 'p-filled': user.info.title }"
                                  />

                                  <label for="title"
                                    >Naslov * (npr. Keramicar/godine
                                    iskustva)</label
                                  >
                                </span>
                              </div>
                            </div>
                            <div class="column is-12">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-globe"></i>
                                </span>
                                <span class="p-float-label">
                                  <Dropdown
                                    id="entity"
                                    v-model="user.info.entity"
                                    :options="entity"
                                    optionLabel="name"
                                    :class="{ 'p-filled': user.entity }"
                                  />

                                  <label for="entity">Entitet</label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-globe"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="city"
                                    v-model="user.city"
                                    :value="user.city"
                                    :class="{ 'p-filled': user.city }"
                                  />
                                  <label for="city">City *</label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-globe"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="address"
                                    v-model="user.address"
                                    :value="user.address"
                                    :class="{ 'p-filled': user.address }"
                                  />
                                  <label for="address">Adresa *</label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-12">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-user"></i>
                                </span>
                                <span class="p-float-label">
                                  <Textarea
                                    id="about"
                                    v-model="user.info.about"
                                    :value="user.info.about"
                                    :class="{ 'p-filled': user.info.about }"
                                  />
                                  <label for="about"
                                    >O nama ( Napisite nesto vise o vasoj
                                    firmi/zanimanju ) *</label
                                  >
                                </span>
                              </div>
                            </div>
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-mobile"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="address"
                                    v-model="user.info.phone"
                                    :value="user.info.phone"
                                    :class="{ 'p-filled': user.info.phone }"
                                  />
                                  <label for="address">Telefon</label>
                                </span>
                              </div>
                            </div>
                            <div class="column is-6">
                              <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                  <i class="pi pi-facebook"></i>
                                </span>
                                <span class="p-float-label">
                                  <InputText
                                    id="address"
                                    v-model="user.info.facebook"
                                    :value="user.info.facebook"
                                    :class="{ 'p-filled': user.info.facebook }"
                                  />
                                  <label for="address">Facebook Link</label>
                                </span>
                              </div>
                            </div>
                          </div>
                        </div>
                      </section>
                      <footer class="modal-card-foot">
                        <button
                          @click="
                            editPayload(user);
                            closeMaximizable();
                          "
                          class="button is-success"
                        >
                          Save changes
                        </button>
                        <button @click="closeMaximizable" class="button">
                          Cancel
                        </button>
                      </footer>
                    </div>
                  </div>
                </div>
              </div>
              <div class="about-body">
                <div class="columns">
                  <div class="column is-5">
                    <div class="about-block">
                      <div class="block-header">
                        <h4>Contact Info</h4>
                      </div>
                      <div class="block-content">
                        <div class="flex-inner">
                          <i class="pi pi-mobile" />

                          <span
                            >Call
                            <a v-if="user.info.phone">{{
                              user.info.phone
                            }}</a></span
                          >
                        </div>
                        <div class="flex-inner">
                          <i class="pi pi-globe" />
                          <span
                            >Grad <a v-if="user.city">{{ user.city }}</a></span
                          >
                        </div>
                        <div class="flex-inner">
                          <i class="pi pi-compass" />

                          <span
                            >Adresa
                            <a v-if="user.address">{{ user.address }}</a></span
                          >
                        </div>
                      </div>
                      <div class="block-header">
                        <h4> Socijalne Mreze </h4>
                      </div>
                      <div class="block-content">
                        <div class="flex-inner">
                          <i class="pi pi-facebook" />

                          <span
                            >Call
                            <a v-if="user.info.facebook">{{
                              user.info.facebook
                            }}</a></span
                          >
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="column is-6">
                    <div class="about-block">
                      <div class="block-header">
                        <h4>History</h4>
                      </div>
                      <div class="block-content">
                        <div class="div has-text-right">
                          <History
                            :history="user.info.history"
                            @history="handleHistory"
                          >
                          </History>
                        </div>
                        <div
                          v-for="(event, index) in user.info.history"
                          :key="event"
                          class="history-block"
                        >
                          <div class="date">{{ event.date }}</div>
                          <div class="timeline">
                            <ul>
                              <li class="">
                                {{ event.description }}

                                <div
                                  class="dropdown is-right"
                                  :id="+index"
                                  :class="{ 'is-active': index === render }"
                                >
                                  <div class="dropdown-trigger">
                                    <i
                                      class="pi pi-trash"
                                      style="margin-left: 6.7rem;"
                                      @click.prevent="historyFetch(index)"
                                    />
                                  </div>
                                  <div
                                    class="dropdown-menu"
                                    :id="'dropdown-menu_' + index"
                                    role="menu"
                                  >
                                    <div class="dropdown-content">
                                      <div class="dropdown-item">
                                        <div class="button-wrappper">
                                          <div class="columns">
                                            <div class="column">
                                              <i
                                                class="pi pi-info"
                                                aria-haspopu="true"
                                                aria-controls="dropdown-menu2"
                                              />
                                              <span>
                                                Potvrdite brisanje unosa !
                                              </span>
                                            </div>
                                          </div>
                                          <Button
                                            icon="pi pi-check"
                                            class="p-button-rounded p-button-text"
                                            @click.prevent="
                                              deleteHistory(index)
                                            "
                                          />
                                          <Button
                                            icon="pi pi-times"
                                            class="p-button-rounded p-button-danger p-button-text"
                                            @click.prevent="closeHistory"
                                          />
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <Portfolio
              :projects="user.projects"
              :check="user.portfolio"
              @handlePortfolio="currentUser"
            ></Portfolio>

            <Skills
              :check="user.info.skills"
              :skillsdata="user.info.skills"
              @skills="handleSkill"
              @deleteskills="handleDeleteSkills"
            />
          </div>
        
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import UserWork from "@/modules/user.ts";
import { User } from "@/modules/user.ts";
import Portfolio from "../components/Portfolio.vue";
import History from "../components/History.vue";
import Skills from "../components/Skills.vue";
import { onMounted, ref, reactive, onUpdated} from "vue";
import axios from "axios";

interface History {
  date: "";
  description: "";
}
export default {
  components: {
    Portfolio,
    History,
    Skills,
  },
   setup() {
    const { currentUser, user, errorMessage} = UserWork();
    const display = ref(false);
    const displayEdit = ref(false);
    const message = ref("");
    const render = ref(null);

    currentUser()

    /** Modal area */

    const openMaximizable = () => {
      display.value = true;
    };
    const closeMaximizable = () => {
      display.value = false;
    };

    const openModalEdit = () => {
      displayEdit.value = true;
    };

    const closeModalEdit = () => {
      displayEdit.value = false;
    };

    /** Core of view used to interact withback end route to provide all editing functions */
    const editPayload = (payload: User) => {
      axios
        .put("http://localhost:8000/users/edit", payload)
        .then((response) => {
          message.value = "Uspjesno ste izmijenili podatke !";
        });
    };

    /** This block is resposible for history events */
    const handleSkill = (payload: any) => {
      const data = [payload];

      if (user.value.info.skills) {
        user.value.info.skills.push(payload);
        editPayload(user.value);
      } else {
        user.value.info.skills = data;
        editPayload(user.value);
      }
    };

    const handleDeleteSkills = (payload: any) => {
      user.value.info.skills.splice(payload, 1);
      editPayload(user.value);
    };

    /** History block used to handle all the stuff happening in child component */
    const handleHistory = (payload: any) => {
      console.log(user.value.info.history);
      const data = [payload];

      if (user.value.info.history) {
        user.value.info.history.push(payload);
        editPayload(user.value);
      } else {
        user.value.info.history = data;
        editPayload(user.value);
      }
    };

    const historyFetch = (payload: number) => {
      render.value = payload;
    };

    const deleteHistory = (payload: number) => {
      user.value.info.history.splice(payload, 1);
      editPayload(user.value);
      render.value = null;
    };

    const closeHistory = () => {
      render.value = null;
    };

    const entity = [
      { name: "Federacija Bosne i Hercegovine" },
      { name: "Republika Srpska" },
      { name: "Brčko Distrikt" },
    ];

    return {
      user,
      errorMessage,
      display,
      displayEdit,
      openModalEdit,
      closeModalEdit,
      openMaximizable,
      closeMaximizable,
      editPayload,
      entity,
      currentUser,
      handleHistory,
      handleSkill,
      handleDeleteSkills,
      historyFetch,
      deleteHistory,
      closeHistory,
      render,
      message,
    };
  },
};
</script>
