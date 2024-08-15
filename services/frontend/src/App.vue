<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>


<template>
  <v-app>
    <v-main>
        <RouterView />
    </v-main>
  </v-app>
</template>



<style>
v-container {
  background-color: #d4cdcd;
}

#app {

  max-width: 1100px;
  margin: 0 auto;
  color: #c9c4c4;
}
</style>


