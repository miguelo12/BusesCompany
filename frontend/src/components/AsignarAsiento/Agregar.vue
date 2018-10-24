<template>
  <v-container fluid>
    <h2 class="display-4">
        Asignar Asiento
    </h2>
    <h3 class="display-2">
      Eligir asiento para el pasajero.
    </h3>
    <v-form ref="form" v-model="valid" lazy-validation>
    <v-container>
      <v-layout row justify-center >
        <v-flex xs12 >
          <v-layout row justify-center >
            <v-flex xs12 md6 >
              <v-card-media src="@/assets/bus-top-edit.png" height="550px" width="100%" style="padding-top:240px"
                    contain>
                <v-layout justify-center  :key="s" v-for="s in 5">
                  <v-btn @click="provide(asientos[(2*(s-1))])" v-bind:class="{'teal darken-2 white--text': contains(reserva, asientos[(2*(s-1))]),'teal lighten-4': !contains(reserva, asientos[(2*(s-1))])}" >{{ asientos[(2*(s-1))].name }}</v-btn>
                  <v-btn @click="provide(asientos[(2*(s-1))+1])" v-bind:class="{'teal darken-2 white--text': contains(reserva, asientos[(2*(s-1))+1]),'teal lighten-4': !contains(reserva, asientos[(2*(s-1))+1])}" >{{ asientos[(2*(s-1))+1].name }}</v-btn>
                </v-layout>
              </v-card-media>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
      <v-select
        v-model="pasajero_id"
        :items="items"
        :rules="[v => !!v || 'Pasajero is required']"
        :messages="['Messages']"
        prepend-icon="home"
        label="Pasajero:"
        required></v-select>
      <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
      <v-btn @click="clear" color="error">Reset</v-btn>
    </v-form>
  </v-container>
</template>
<script>
import axios from 'axios'

export default {
  data: () => ({
    valid: false,
    asientos: [{name: '1'}, {name: '2'}, {name: '3'}, {name: '4'}, {name: '5'}, {name: '6'}, {name: '7'}, {name: '8'}, {name: '9'}, {name: '10'}],
    reserva: [],
    pasajero_id: null,
    items: [
      'Ejemplo 1',
      'Ejemplo 2',
      'Ejemplo 3',
      'Ejemplo 4'
    ]
  }),
  methods: {
    submit (evt) {
      if (this.$refs.form.validate()) {
        if (this.reserva.length > 0) {
          axios.post('http://localhost:8000/api/buses/', {
            reserva: this.reserva,
            pasajero_id: this.pasajero_id
          }).then(response => {
            alert(response.id)
          }).catch(e => {
            alert(e)
          })
        } else {
          alert('error')
        }
      }
    },
    clear (evt) {
      this.reserva = []
      this.$refs.form.reset()
    },
    changeAsignar (s, evt) {
      if (this.asientos[s]) {
        this.asientos[s] = false
      } else {
        this.asientos[s] = true
      }
    },
    provide (item) {
      if (this.reserva.indexOf(item) === -1) {
        this.reserva.push(item)
      } else {
        this.reserva.splice(this.reserva.indexOf(item), 1)
      }
    },
    contains (arr, item) {
      return arr.indexOf(item) !== -1
    }
  }
}
</script>
<style lang="">
</style>
