<template>
    <div class='tab' v-show='isActive'>
      <slot></slot>
    </div>
  </template>
  
  <script>
  import { ref, inject, onMounted } from 'vue'
  
  export default {
    props: {
      title: {
        type: String,
        default: 'Tab'
      }
    },
    setup(props) {
      const isActive = ref(true)
      const tabs = inject('tabs')
  
      onMounted(() => {
        tabs.value.push({ props, isActive })
      })
  
      return { isActive }
    }
  }
  </script>
  
  <style>
  </style>