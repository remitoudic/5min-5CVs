<!-- components/Navbar.vue -->
<template>
  <nav>
    <span class="nav-item">CV buidler</span>
    <span class="nav-item">Docs</span>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.navbar {
  background-color: #333;
  padding: 10px 20px;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-item {
  margin: 0 10px;
  cursor: pointer;
}

.nav-item:hover {
  text-decoration: underline;
}
</style>
