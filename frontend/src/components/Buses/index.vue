<template>
  <div>
    <v-container fluid grid-list-sm>
      <v-layout row wrap>
        <v-flex d-flex xs12 sm6>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card color="purple" dark>
                <bus v-bind:idTrayecto="idTrayecto" v-bind:idBus="idBus" />
              </v-card>
            </v-flex>
            <v-flex d-flex>
              <v-card color="indigo" dark>
                <pasajero v-on:pasajeroCRUD="initialize" />
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex d-flex xs12 sm6>
          <v-layout row wrap>
            <v-flex d-flex>
              <v-card color="indigo lighten-1" dark tile flat>
                <v-card-text>
                  <h3 class="display-3">
                      Asignar Asiento
                  </h3>
                  <h4 class="display-1">
                    Eligir asiento para el pasajero.
                  </h4>
                  <v-form ref="form" v-model="valid2" lazy-validation>
                  <v-container>
                    <v-layout row justify-center >
                      <v-flex xs12 >
                        <v-layout row justify-center >
                          <v-flex xs12 md6 >
                            <v-img src="@/assets/bus-top-edit.png" height="550px" width="100%" style="padding-top:240px"
                                  contain>
                              <v-layout justify-center  :key="s" v-for="s in 5">
                                <v-btn @click="provide(asientos[(2*(s-1))])" v-bind:class="{'teal darken-2 white--text': contains(reserva, asientos[(2*(s-1))]),'teal lighten-4 black--text': !contains(reserva, asientos[(2*(s-1))])}" >{{ asientos[(2*(s-1))].name }}</v-btn>
                                <v-btn @click="provide(asientos[(2*(s-1))+1])" v-bind:class="{'teal darken-2 white--text': contains(reserva, asientos[(2*(s-1))+1]),'teal lighten-4 black--text': !contains(reserva, asientos[(2*(s-1))+1])}" >{{ asientos[(2*(s-1))+1].name }}</v-btn>
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
                      :item-text="item => item.nombre+' '+item.rut" :item-value="item => item.id"
                      label="Pasajero:"
                      required></v-select>
                    <v-btn :disabled="!valid2" @click="submit" color="info">Submit</v-btn>
                    <v-btn @click="clear" color="error">Reset</v-btn>
                  </v-form>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :multi-line="true"
      :timeout="snackbar_timeout">
      {{ snackbar_text }}
      <v-btn
        dark
        flat
        @click="snackbar = false">
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>
<script>
import axios from 'axios'
import pasajero from '@/components/Pasajeros/index'
import bus from '@/components/Buses/agregar'
const url = 'http://localhost:8000/api/'

export default {
  components: {
    pasajero,
    bus
  },
  data: () => ({
    idTrayecto: 0,
    idBus: 0,
    ActualizoPasajero: false,
    lorem: `Lorem ipsum dolor sit amet, mel at clita quando. Te sit oratio vituperatoribus, nam ad ipsum posidonium mediocritatem, explicari dissentiunt cu mea. Repudiare disputationi vim in, mollis iriure nec cu, alienum argumentum ius ad. Pri eu justo aeque torquatos.`,
    valid2: false,
    asientos: [{name: '1'}, {name: '2'}, {name: '3'}, {name: '4'}, {name: '5'}, {name: '6'}, {name: '7'}, {name: '8'}, {name: '9'}, {name: '10'}],
    reserva: [],
    pasajero_id: null,
    items: [
      'Ejemplo 1',
      'Ejemplo 2',
      'Ejemplo 3',
      'Ejemplo 4'
    ],
    loading: true,
    error: false,
    valid: false,
    dialog: false,
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: '',
    busesBox: [],
    headers: [
      {
        text: 'Codigo',
        align: 'left',
        sortable: false,
        value: 'id'
      },
      {
        text: 'Acciones',
        value: 'name',
        sortable: false
      }
    ],
    trayectos: [],
    editedIndex: -1,
    editedItem: {
      destino: '',
      subida: '',
      buses: null,
      picker_date: null,
      picker_time: null,
      modal1: false,
      modal2: false
    },
    defaultItem: {
      codigo: '',
      origen: '',
      destino: '',
      subida: '',
      buses: null,
      picker_date: null,
      picker_time: null,
      modal1: false,
      modal2: false
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Nuevo Trayecto' : 'Editar Trayecto'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    }
  },
  methods: {
    initialize () {
      // parametro id
      // if (this.$route.params.id !== undefined) {

      // }
      this.loading = true
      this.error = false
      axios.get(url + 'pasajeros/')
        .then(response => {
          this.items = response.data
          this.loading = false
        }).catch(e => {
          this.trayectos = []
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
          this.loading = false
          this.error = true
        })
        // axios.get(url + 'trayectos/')
        // .then(response => {
        //   this.trayectos = response.data
        //   this.loading = false
        // }).catch(e => {
        //   this.trayectos = []
        //   this.snackbar_color = 'error'
        //   this.snackbar_timeout = 4000
        //   this.snackbar_text = 'Error inesperado.'
        //   this.snackbar = true
        //   this.loading = false
        //   this.error = true
        // })
    },
    editItem (item) {
      this.editedIndex = this.trayectos.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
      // la fecha arreglar
    },
    deleteItem (item) {
      if (confirm('¿Estas seguro que quiere eliminar el trayecto?')) {
        axios.delete(url + 'trayectoSet/' + item.id + '/').then(response => {
          this.initialize()
          this.snackbar_color = 'success'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Se ha eliminado con exito.'
          this.snackbar = true
        }).catch(e => {
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
      }
    },
    close () {
      this.dialog = false
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      }, 300)
    },
    save () {
      if (this.$refs.form.validate()) {
        if (this.editedItem.codigo === '') {
          axios.post(url + 'trayectoSet/', {
            origen: this.editedItem.origen,
            destino: this.editedItem.destino,
            horario: this.editedItem.picker_date + ' ' + this.editedItem.picker_time,
            subida: this.editedItem.subida,
            buses: this.editedItem.buses
          }).then(response => {
            this.initialize()
            this.snackbar_color = 'success'
            this.snackbar_timeout = 4000
            this.snackbar_text = 'Se ha guardado con exito.'
            this.snackbar = true
          }).catch(e => {
            this.snackbar_color = 'error'
            this.snackbar_timeout = 4000
            this.snackbar_text = 'Error inesperado.'
            this.snackbar = true
          })
          this.close()
        } else {
          if (confirm('¿Estas seguro que quiere editar el trayecto?')) {
            axios.put(url + 'trayectoSet/' + this.editedItem.id + '/', {
              origen: this.editedItem.origen,
              destino: this.editedItem.destino,
              horario: this.editedItem.picker_date + ' ' + this.editedItem.picker_time,
              subida: this.editedItem.subida,
              buses: this.editedItem.buses
            }).then(response => {
              this.initialize()
              this.snackbar_color = 'success'
              this.snackbar_timeout = 4000
              this.snackbar_text = 'Se ha editado con exito.'
              this.snackbar = true
            }).catch(e => {
              this.snackbar_color = 'error'
              this.snackbar_timeout = 4000
              this.snackbar_text = 'Error inesperado.'
              this.snackbar = true
            })
            this.close()
          }
        }
      }
    },
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
  },
  mounted () {
    this.idTrayecto = this.$route.params.id
    this.idBus = this.$route.params.idBus
    this.initialize()
  }
}
</script>
<style lang="">
</style>
