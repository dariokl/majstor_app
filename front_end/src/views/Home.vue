<template>
  <LandingPage />
  <About />
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import LandingPage from "@/components/LandingPage.vue"; // @ is an alias to /src
import About from "./About.vue";

@Options({
  components: {
    LandingPage,
    About
  }
})


export default class Home extends Vue {
}
</script>
