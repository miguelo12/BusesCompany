<template>
  <div>
  <v-navigation-drawer class="teal teal darken-4" dark fixed clipped v-model="drawer" app>
    <v-list dense>
      <v-subheader class="mt-3 gray--text">Menu</v-subheader>
      <div v-for="item in items" :key="item.text">
       <div v-if="item.icon !== 'home'">
        <v-list-tile slot="activator" active-class="teal accent-4" avatar :to="{name: item.text}">
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ item.text }}
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </div>
      <div v-else>
      <v-list-group no-action >
        <v-list-tile slot="activator">
          <v-list-tile-action>
            <v-icon>
              home
            </v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>App</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
          <v-list-tile v-for="item1 in dashboard" active-class="teal accent-4" :key="item1.text" avatar :to="{name: item1.text}">
            <v-list-tile-action active-class="teal accent-2">
              <v-icon>{{item1.icon}}</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>{{item1.text}}</v-list-tile-title>
          </v-list-tile>
        </v-list-group>
      </div>
    </div>
    </v-list>
  </v-navigation-drawer>
  <v-toolbar color="teal" app fixed clipped-left dark>
    <v-toolbar-side-icon  @click.stop="drawer = !drawer"><v-icon>view_headline</v-icon></v-toolbar-side-icon>
    <v-toolbar-title>BusesCompany</v-toolbar-title>
  </v-toolbar>
  </div>
</template>
<script>
export default {
  data: () => ({
    drawer: true,
    items: [
      { icon: 'insert_chart', text: 'Dashboard' },
      { icon: 'home', text: 'App' },
      { icon: 'info', text: 'About' }
    ],
    dashboard: [
      { icon: 'terrain', text: 'Trayectos' },
      { icon: 'airline_seat_recline_normal', text: 'Choferes' },
      { icon: 'people', text: 'Pasajeros' }
    ]
  }),
  props: {
    source: String
  }
}
</script>
<style lang="">
</style>
