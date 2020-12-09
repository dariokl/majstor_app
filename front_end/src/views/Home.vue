<template>

<div class="p-grid">
	<div class="p-col">1</div>
	<div class="p-col">2</div>
	<div class="p-col">3</div>
</div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

@Options({
  components: {
    HelloWorld
  }
})
export default class Home extends Vue {}
</script>
