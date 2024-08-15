<template>
    <div :class='{"tabs__light": mode === "light", "tabs__dark": mode === "dark"}'>
      <ul class='tabs__header'>
        <li v-for='(tab, index) in tabs'
          :key='tab.title'
          @click='selectTab(index)'
          :class='{"tab__selected": (index == selectedIndex)}'>
          {{ tab.props.title }}
        </li>
      </ul>
      <slot></slot>
    </div>
  </template>
  
  <script>
  import { ref, provide, onMounted } from 'vue'
  
  export default {
    
    props: {
      mode: {
        type: String,
        default: 'light'
      }
    },
    setup() {
      const selectedIndex = ref(0)
      const tabs = ref([])
  
      provide('tabs', tabs)
  
      const selectTab = (i) => {
        selectedIndex.value = i
        tabs.value.forEach((tab, index) => {
          tab.isActive = (index === i)
        })
      }
  
      onMounted(() => {
        selectTab(0)
      })
  
      return { selectedIndex, tabs, selectTab }
    }
  }
  </script>
  
  <style lang="css">

  ul.tabs__header {
    display: block;
    list-style: none;
    margin: 0 0 0 20px;
    padding: 0;
  }

  ul.tabs__header > li {
    padding: 15px 30px;
    border-radius: 10px;
    margin: 0;
    display: inline-block;
    margin-right: 5px;
    cursor: pointer;
  }

  ul.tabs__header > li.tab__selected {
    font-weight: bold;
    border-radius: 10px 10px 0 0;
    border-bottom: 8px solid transparent;
  }

  .tab {
    display: inline-block;
    color: black;
    padding: 20px;
    min-width: 800px;
    border-radius: 10px;
    min-height: 400px;
  }

  .tabs__light .tab{
    background-color: #fff;
  }

  .tabs__light li {
    background-color: #ddd;
    color: #aaa;
  }

  .tabs__light li.tab__selected {
    background-color: #fff;
    color: #42d584;
  }

  .tabs__dark .tab{
    background-color: #555;
    color: #eee;
  }

  .tabs__dark li {
    background-color: #ddd;
    color: #bbb9b9;
  }

  .tabs__dark li.tab__selected {
    background-color: #555;
    color: white;

  }

</style>