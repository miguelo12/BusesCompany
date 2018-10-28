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
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import VueApexCharts from 'vue-apexcharts'

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
    ActualizarPasajero: 0,
    idTrayecto: 0,
    idBus: 0,
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: ''
  }),
  methods: {
    GenerateDayWiseTimeSeries (baseval, count, yrange) {
      var i = 0
      var series = []
      while (i < count) {
        var x = baseval
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min

        series.push([x, y])
        baseval += 86400000
        i++
      }
      return series
    }
  },
  created: function () {
  }
}
</script>
<style lang="">
</style>
