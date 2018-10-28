<template>
  <v-container fluid>
    <h3 class="display-3">
        Asignar Asiento
    </h3>
    <h4 class="display-1">
      Eligir asiento para el pasajero.
    </h4>
    <v-form ref="form" v-model="valid">
    <v-container>
      <v-layout row justify-center >
        <v-flex xs12 >
          <v-layout column justify-center >
            <v-flex xs12 md6 >
              <v-img src="@/assets/bus-top-edit.png" height="550px" width="100%" style="padding-top:240px" contain>
                <v-layout justify-center  :key="s" v-for="s in 5">
                  <v-btn @click="provide(asientos[(2*(s-1))])" :disabled="asiento_disable[(2*(s-1))]" v-bind:class="{'teal darken-2 white--text': contains(reserva_seleccionada, asientos[(2*(s-1))]),'teal lighten-4 black--text': !contains(reserva_seleccionada, asientos[(2*(s-1))])}" >{{ asientos[(2*(s-1))] }}</v-btn>
                  <v-btn @click="provide(asientos[(2*(s-1))+1])" :disabled="asiento_disable[(2*(s-1))+1]" v-bind:class="{'teal darken-2 white--text': contains(reserva_seleccionada, asientos[(2*(s-1))+1]),'teal lighten-4 black--text': !contains(reserva_seleccionada, asientos[(2*(s-1))+1])}" >{{ asientos[(2*(s-1))+1] }}</v-btn>
                </v-layout>
              </v-img>
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
        :item-text="item => item.nombre+' '+item.rut" :item-value="item => item.id"
        required></v-select>
      <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
      <v-btn @click="clear" color="error">Reset</v-btn>
    </v-form>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :multi-line="true"
      :timeout="snackbar_timeout">
      {{ snackbar_text }}
      <v-btn
        dark
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </v-container>
</template>
<script>
import axios from 'axios'
const url = 'http://localhost:8000/api/'

export default {
  data: () => ({
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: '',
    valid: false,
    asiento_disable: [false, false, false, false, false, false, false, false, false, false],
    asientos: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    reserva_seleccionada: [],
    reserva: [],
    reserva_guardada: [],
    pasajero_id: null,
    items: []
  }),
  props: ['ActualizarPasajero', 'idBus'],
  watch: {
    ActualizarPasajero: function () {
      if (this.ActualizarPasajero === 1) {
        this.initialize()
        this.$emit('actualizarPasajero')
      }
    },
    reserva_guardada: function () {
      this.disabledButton()
    }
  },
  methods: {
    disabledButton () {
      Object.keys(this.asientos).forEach(key => {
        this.reserva_guardada.forEach(elemguardado => {
          if (this.asientos[key] === elemguardado.numeroAsiento) {
            this.$set(this.asiento_disable, key, true)
          }
        })
      })
    },
    submit (evt) {
      if (this.$refs.form.validate()) {
        if (this.idBus) {
          if (this.reserva_seleccionada.length > 0) {
            this.reserva_seleccionada.forEach(elementrsvslc => {
              var existreserva = false
              this.reserva.forEach(elementrsv => {
                if (elementrsv.asiento === elementrsvslc) {
                  existreserva = true
                }
              })
              if (!existreserva) {
                this.reserva.push({ 'pasajero_id': this.pasajero_id, 'numeroAsiento': elementrsvslc })
              }
            })
            axios.patch(url + 'asientoAsignadoCRUD/' + this.idBus + '/', {
              id: this.idBus,
              asientoAsignado: this.reserva
            }).then(response => {
              this.reserva_guardada.push(this.reserva)
              alert('Se ha guardado con exito.')
              this.$router.go() // parche horrible
            }).catch(e => {
              this.snackbar_color = 'error'
              this.snackbar_timeout = 4000
              this.snackbar_text = 'Error inesperado.'
              this.snackbar = true
            })
            this.reserva = []
          } else {
            this.snackbar_color = 'error'
            this.snackbar_timeout = 4000
            this.snackbar_text = 'No has seleccionado asiento.'
            this.snackbar = true
          }
        } else {
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Aun no ingresas un bus.'
          this.snackbar = true
        }
      }
    },
    initialize () {
      if (this.idBus) {
        axios.get(url + 'asientoAsignadoCRUD/' + this.idBus + '/'
        ).then(response => {
          this.reserva_guardada = response.data.asientoAsignado
          this.reserva = []
        }).catch(e => {
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
      }
      axios.get(url + 'pasajerosCRUD/')
        .then(response => {
          this.items = response.data
        }).catch(e => {
          this.snackbar_color = 'error'
          this.snackbar_timeout = 3000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
    },
    clear (evt) {
      this.reserva_seleccionada = []
      this.$refs.form.reset()
    },
    provide (item) {
      if (this.reserva_seleccionada.indexOf(item) === -1) {
        this.reserva_seleccionada.push(item)
      } else {
        this.reserva_seleccionada.splice(this.reserva_seleccionada.indexOf(item), 1)
      }
    },
    contains (arr, item) {
      return arr.indexOf(item) !== -1
    }
  },
  created () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
