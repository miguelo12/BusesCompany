<template>
  <div>
  <v-navigation-drawer class="teal teal darken-4" dark fixed clipped v-model="drawer" app>
    <v-list dense>
       <v-subheader class="mt-3 gray--text">Menu</v-subheader>
       <v-list-tile active-class="default-class teal accent-4" v-for="item in items" :key="item.text" avatar :to="{ name: item.text}">
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>
            {{ item.text }}
          </v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar color="teal" app fixed clipped-left dark>
    <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    <v-toolbar-title>BusesCompany</v-toolbar-title>
  </v-toolbar>
  </div>
</template>
<script>
export default {
  data: () => ({
    drawer: true,
    items: [
      { icon: 'mdi-home', text: 'Home' },
      { icon: 'mdi-chart-line', text: 'Dashboard' },
      { icon: 'mdi-information', text: 'About' }
    ]
  }),
  props: {
    source: String
  }
}
</script>
<style lang="">
</style>
