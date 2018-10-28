<template>
  <div>
    <v-container fluid grid-list-sm>
      <v-layout row wrap>
        <v-flex d-flex xs12>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card>
                <apexcharts width="600" type="bar" :options="options" :series="series"></apexcharts>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex d-flex xs12>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card>
                <v-list>
                  <v-list-tile
                    v-for="s in 1"
                    :key="s"
                    avatar>
                    <v-list-tile-content>
                      <v-list-tile-title v-text="'Trayecto'"></v-list-tile-title>
                    </v-list-tile-content>
                    <v-list-tile-content>
                      <v-list-tile-title v-text="'Pasajeros%'"></v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile
                    v-for="(item,s) in datosTrayectos"
                    :key="item.origen"
                    avatar>
                    <v-list-tile-content>
                      <v-list-tile-title v-text="'origen: '+item.origen+' destino: '+item.destino"></v-list-tile-title>
                    </v-list-tile-content>
                    <v-list-tile-content>
                      <v-list-tile-title v-text="dataCant[s]+'%'"></v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'
import axios from 'axios'

const url = 'http://localhost:8000/api/'

export default {
  components: {
    apexcharts: VueApexCharts
  },
  data: () => ({
    options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: ['Pasajero promedio']
      }
    },
    series: [{
      name: 'Trayecto',
      data: []
    }],
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: '',
    datosTrayectos: [],
    dataCant: [],
    dataName: []
  }),
  methods: {
    initialize () {    
      axios.get(url + 'trayectosR/')
        .then(response => {
          response.data.forEach(element => {
            if(element.buses){
              this.dataCant.push(element.buses.asientoAsignado.length*10)
              this.datosTrayectos.push(element)
            }
          })
        }).catch(e => {
          alert(e)
        })

      this.series = [{ name: 'Trayecto' , data: this.dataCant }]
    }
  },
  created: function () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
