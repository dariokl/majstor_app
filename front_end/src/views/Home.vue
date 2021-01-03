<template>
  <HelloWorld />
  <About />
</template>
<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import About from "./About.vue";

@Options({
  components: {
    HelloWorld,
    About
  }
})


export default class Home extends Vue {
}
</script>
