<template>
  <div>
    <v-container fluid grid-list-sm>
      <v-layout row wrap>
        <v-flex d-flex xs12>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card>
                <apexcharts width="500" type="bar" :options="options" :series="series"></apexcharts>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex d-flex xs12>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card>
                <apexcharts width="500" type="bar" :options="options" :series="series"></apexcharts>
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
        categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
      }
    },
    series: [{
      name: 'series-1',
      data: [30, 40, 45, 50, 49, 60, 70, 91]
    }],
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: ''
  }),
  methods: {
    initialize () {
      axios.get(url + 'trayectosR/')
        .then(response => {
          console.log(response.data)
        }).catch(e => {
          alert(e)
        })
    }
  },
  created: function () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
