<template>
  <div>
    <v-container fluid grid-list-sm>
      <v-layout row wrap>
        <v-flex d-flex xs12 sm6>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card color="purple" dark>
                <bus v-bind:idTrayecto="idTrayecto" v-bind:idBus="idBus" v-on:busCUD="onCrudNuevo" />
              </v-card>
            </v-flex>
            <v-flex d-flex>
              <v-card color="indigo" dark>
                <pasajero v-on:pasajeroCRUD="actualizarPasajero" />
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex d-flex xs12 sm6>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card color="indigo lighten-1" dark tile flat>
                <asignarAsiento v-bind:idTrayecto="idTrayecto" v-bind:idBus="idBus" v-bind:ActualizarPasajero="ActualizarPasajero" v-on:actualizarPasajero="actualizarPasajero" />
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
<script>
import pasajero from '@/components/Pasajeros/index'
import bus from '@/components/Buses/agregar'
import asignarAsiento from '@/components/AsignarAsiento/agregar'

export default {
  components: {
    pasajero,
    bus,
    asignarAsiento
  },
  data: () => ({
    ActualizarPasajero: 0,
    idTrayecto: 0,
    idBus: 0
  }),
  methods: {
    actualizarPasajero () {
      this.ActualizarPasajero === 0 ? this.ActualizarPasajero++ : this.ActualizarPasajero--
    },
    onCrudNuevo: function (item) {
      this.$router.push({name: 'BusesConbus', params: { id: this.idTrayecto, idbus: item }})
      this.idBus = this.$route.params.idbus
    }
  },
  created: function () {
    this.idTrayecto = this.$route.params.id
    this.idBus = this.$route.params.idbus
  }
}
</script>
<style lang="">
</style>
