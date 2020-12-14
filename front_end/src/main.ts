import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from 'primevue/config';
import router from "./router";

import Message from "primevue/message";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dropdown from "primevue/dropdown";
import Textarea from "primevue/textarea";
import FileUpload from "primevue/fileupload";
import Checkbox from "primevue/checkbox";


import "primevue/resources/themes/nova-vue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";


createApp(App)
  .component("Message", Message)
  .component("Button", Button)
  .component("InputText", InputText)
  .component("Dropdown", Dropdown)
  .component("Textarea", Textarea)
  .component("FileUpload", FileUpload)
  .component("Checkbox", Checkbox)
  .use(router)
  .use(PrimeVue)
  .mount("#app");
