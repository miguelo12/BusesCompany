<template>
  <div id="app">
    <v-app>
      <!-- <v-parallax dark height="1300" src="./assets/fondo-patagonia.jpg"> -->
        <NavBar v-if="'show-NavBar'" />
          <v-content>
            <router-view/>
          </v-content>
        <Footer v-if="'show-NavBar'" />
      <!-- </v-parallax> -->
      </v-app>
    </div>
</template>

<script>
import NavBar from '@/components/Layout/navBar'
import Footer from '@/components/Layout/footer'
export default {
  name: 'App',
  'show-NavBar': true,
  components: {
    NavBar,
    Footer
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
  margin-top: 0px;
  padding-bottom: 5px;
}
</style>
