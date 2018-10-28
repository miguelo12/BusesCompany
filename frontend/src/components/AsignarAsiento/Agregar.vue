<template>
  <v-container fluid>
    <h3 class="display-3">
        Asignar Asiento
    </h3>
    <h4 class="display-1">
      Eligir asiento para el pasajero.
    </h4>
    <v-form ref="form" v-model="valid" lazy-validation>
    <v-container>
      <v-layout row justify-center >
        <v-flex xs12 >
          <v-layout row justify-center >
            <v-flex xs12 md6 >
              <v-img src="@/assets/bus-top-edit.png" height="550px" width="100%" style="padding-top:240px" contain>
                <v-layout justify-center  :key="s" v-for="s in 5">
                  <v-btn @click="provide(asientos[(2*(s-1))])" :disabled="asientos[(2*(s-1))].disabled" v-bind:class="{'teal darken-2 white--text': contains(reserva_seleccionada, asientos[(2*(s-1))]),'teal lighten-4 black--text': !contains(reserva_seleccionada, asientos[(2*(s-1))])}" >{{ asientos[(2*(s-1))].name }}</v-btn>
                  <v-btn @click="provide(asientos[(2*(s-1))+1])" :disabled="asientos[(2*(s-1))+1].disabled"  v-bind:class="{'teal darken-2 white--text': contains(reserva_seleccionada, asientos[(2*(s-1))+1]),'teal lighten-4 black--text': !contains(reserva_seleccionada, asientos[(2*(s-1))+1])}" >{{ asientos[(2*(s-1))+1].name }}</v-btn>
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
  </v-container>
</template>
<script>
import axios from 'axios'
const url = 'http://localhost:8000/api/'

export default {
  data: () => ({
    valid: false,
    asientos: [{name: 1, disabled: false}, {name: 2, disabled: false}, {name: 3, disabled: false}, {name: 4, disabled: false}, {name: 5, disabled: false}, {name: 6, disabled: false}, {name: 7, disabled: false}, {name: 8, disabled: false}, {name: 9, disabled: false}, {name: 10, disabled: false}],
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
    }
  },
  computed: {
    disabledButton: function () {
      Object.keys(this.asientos).forEach(key => {
        this.reserva_guardada.forEach(elemguardado => {
          if (this.asientos[key].name === elemguardado.numeroAsiento) {
            this.$set(this.asientos[key],'disabled', true)
          }
        })
      })
    }
  },
  methods: {
    submit (evt) {
      if (this.$refs.form.validate()) {
        if (this.idBus) {
          if (this.reserva_seleccionada.length > 0) {
            this.reserva_seleccionada.forEach(elementrsvslc => {
              var existreserva = false
              this.reserva.forEach(elementrsv => {
                if (elementrsv.asiento === elementrsvslc.name) {
                  existreserva = true
                }
              })
              if (!existreserva) {
                this.reserva.push({'pasajero_id': this.pasajero_id, 'numeroAsiento': elementrsvslc.name})
              }
            })
            axios.patch(url + 'asientoAsignadoCRUD/' + this.idBus + '/', {
              id: this.idBus,
              asientoAsignado: this.reserva
            }).then(response => {
              this.reserva_guardada.push(this.reserva)
              this.disabledButton
              alert('se guardo con exito')
            }).catch(e => {
              alert(e)
            })
            this.reserva = []
          } else {
            alert('No has seleccionado asiento')
          }
        }
      }
    },
    initialize () {
      if (this.idBus) {
        axios.get(url + 'asientoAsignadoCRUD/' + this.idBus + '/'
        ).then(response => {
          this.reserva_guardada = response.data.asientoAsignado
          this.reserva = []
          this.disabledButton
        }).catch(e => {
          alert(e)
        })
      }
      axios.get(url + 'pasajerosCRUD/')
        .then(response => {
          this.items = response.data
        }).catch(e => {
          this.trayectos = []
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
  mounted () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
