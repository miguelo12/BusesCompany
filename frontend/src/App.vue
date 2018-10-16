<template>
  <div id="app">
    <NavBar v-if="show" />
    <div>
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
export default {
  name: 'App',
  'show-NavBar': true,
  components: {
    NavBar
  }
}
</script>

<style lang="">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>
