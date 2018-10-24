<template>
  <div>
    <v-toolbar flat color="white">
      <v-toolbar-title>Trayectos</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="primary" dark class="mb-2">Nuevo Trayecto</v-btn>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.origen" :rules="[v => !!v || 'Origen is required']" label="Origen" required></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.destino" :rules="[v => !!v || 'Destino is required']" label="Destino" required></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-dialog
                      ref="dialog1"
                      v-model="editedItem.modal1"
                      :return-value.sync="editedItem.picker_date"
                      persistent
                      lazy
                      full-width
                      width="290px"
                    >
                      <v-text-field
                        slot="activator"
                        v-model="editedItem.picker_date"
                        label="Fecha:"
                        :rules="[v => !!v || 'Fecha is required']"
                        required
                        readonly
                      ></v-text-field>
                      <v-date-picker v-model="editedItem.picker_date" scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="editedItem.modal1 = false">Cancelar</v-btn>
                        <v-btn flat color="primary" @click="$refs.dialog1.save(editedItem.picker_date)">OK</v-btn>
                      </v-date-picker>
                    </v-dialog>
                  </v-flex>

                  <v-flex xs12 sm6 md4>
                    <v-dialog
                      ref="dialog2"
                      v-model="editedItem.modal2"
                      :return-value.sync="editedItem.picker_time"
                      persistent
                      lazy
                      full-width
                      width="290px">
                      <v-text-field
                        slot="activator"
                        v-model="editedItem.picker_time"
                        label="Hora:"
                        :rules="[v => !!v || 'Hora is required']"
                        required
                        readonly></v-text-field>
                      <v-time-picker v-model="editedItem.picker_time" scrollable>
                        <v-spacer></v-spacer>
                        <v-btn flat color="primary" @click="editedItem.modal2 = false">Cancelar</v-btn>
                        <v-btn flat color="primary" @click="$refs.dialog2.save(editedItem.picker_time)">OK</v-btn>
                      </v-time-picker>
                    </v-dialog>
                  </v-flex>

                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.subida" :rules="[v => !!v || 'Subida is required']" label="Subida" required></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-select v-model="editedItem.buses" :items="busesBox" :item-text="item => item.matricula" :item-value="item => item.id" :rules="[v => !!v || 'Buses is required']" label="Buses" required></v-select>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" flat @click.native="close">Cancelar</v-btn>
              <v-btn :disabled="!valid" color="blue darken-1" flat @click.native="save">Guardar</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="trayectos"
      hide-actions
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.origen }}</td>
        <td class="text-xs-left">{{ props.item.destino }}</td>
        <td class="text-xs-left">{{ props.item.horario }}</td>
        <td class="text-xs-left">{{ props.item.subida }}</td>
        <td class="text-xs-left">{{ props.item.buses.matricula }}</td>
        <td class="justify-center layout px-0">
          <v-icon small class="mr-3" @click="editItem(props.item)">edit</v-icon>
          <v-icon small class="mr-3" @click="deleteItem(props.item)">delete</v-icon>
          <v-icon small class="mr-3" @click="deleteItem(props.item)">directions_bus</v-icon>
        </td>
      </template>
      <template slot="no-data">
        <v-alert :value="true" color="error" icon="warning">
          Disculpa, no hay datos aun.
        </v-alert>
        <v-btn color="primary" @click="initialize">Reiniciar</v-btn>
      </template>
    </v-data-table>
    <v-snackbar
      v-model="snackbar"
      :color="snackbar_color"
      :multi-line="true"
      :timeout="snackbar_timeout"
    >
      {{ snackbar_text }}
      <v-btn
        dark
        flat
        @click="snackbar = false"
      >
        Close
      </v-btn>
    </v-snackbar>
  </div>
</template>
<script>
import axios from 'axios'

const url = 'http://localhost:8000/api/'

export default {
  data: () => ({
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
        text: 'Origen',
        value: 'origen'
      },
      {
        text: 'Destino',
        value: 'destino'
      },
      {
        text: 'Horario',
        value: 'horario'
      },
      {
        text: 'Subida',
        value: 'subida'
      },
      {
        text: 'Buses',
        value: 'buses_id'
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
      codigo: '',
      origen: '',
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
      axios.get(url + 'trayectos/')
        .then(response => {
          this.trayectos = response.data
        }).catch(e => {
          this.trayectos = []
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
      axios.get(url + 'buses/')
        .then(response => {
          this.busesBox = response.data
        }).catch(e => {
          this.trayectos = []
          this.snackbar_color = 'error'
          this.snackbar_timeout = 4000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
    },
    editItem (item) {
      this.editedIndex = this.trayectos.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
      //la fecha arreglar
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
            axios.put(url + 'trayectoSet/' + item.id + '/',{
              origen: this.editedItem.origen,
              destino: this.editedItem.destino,
              horario: this.editedItem.picker_date + ' ' + this.editedItem.picker_time,
              subida: this.editedItem.subida,
              buses: this.editedItem.buses
            }).then(response => {
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
            this.close()
          }
        }
      }
    }
  },
  mounted () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
