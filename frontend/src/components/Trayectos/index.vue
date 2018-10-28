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
                    <v-text-field v-model="editedItem.origen" :rules="origenRules" label="Origen" required></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.destino" :rules="destinoRules" label="Destino" required></v-text-field>
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
                    <v-text-field v-model="editedItem.subida" :rules="subidaRules" label="Subida" required></v-text-field>
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
      :loading="loading"
      class="elevation-1" >
      <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.id }}</td>
        <td class="text-xs-left">{{ props.item.origen }}</td>
        <td class="text-xs-left">{{ props.item.destino }}</td>
        <td class="text-xs-left">{{ props.item.horario }}</td>
        <td class="text-xs-left">{{ props.item.subida }}</td>
        <td class="text-xs-left" v-if="props.item.buses != null">{{ props.item.buses.matricula }}</td>
        <td class="text-xs-left" v-if="props.item.buses == null"></td>
        <td class="justify-center layout px-0">
          <v-btn color="teal" @click="editItem(props.item)" flat>
            <v-icon>edit</v-icon>
          </v-btn>
          <v-btn color="teal" @click="deleteItem(props.item)" flat>
            <v-icon>delete</v-icon>
          </v-btn>
          <v-btn color="teal" v-if="props.item.buses" :to="{name: 'BusesConbus', params:{ id: props.item.id, idbus: props.item.buses.id }}" flat>
            <v-icon>directions_bus</v-icon>
          </v-btn>
          <v-btn color="teal" v-if="!props.item.buses" :to="{name: 'BusesSinbus', params:{ id: props.item.id }}" flat>
            <v-icon>directions_bus</v-icon>
          </v-btn>
        </td>
      </template>
      <template slot="no-data">
        <v-alert :value="error" color="error" icon="warning">
          Disculpa, no hay datos aun.
        </v-alert>
        <v-btn color="primary" @click="initialize">Reiniciar</v-btn>
      </template>
    </v-data-table>
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
  </div>
</template>
<script>
import axios from 'axios'

const url = 'http://localhost:8000/api/'

export default {
  data: () => ({
    loading: true,
    error: false,
    valid: false,
    dialog: false,
    origenRules: [
      v => !!v || 'Origen es requerido',
      v => v.length <= 50 || 'Origen debe ser menor o igual a  50 characters',
      v => v.length >= 3 || 'Origen debe ser mayor o igual a 3 characters'
    ],
    destinoRules: [
      v => !!v || 'Destino es requerido',
      v => v.length <= 50 || 'Destino debe ser menor o igual a  50 characters',
      v => v.length >= 3 || 'Destino debe ser mayor o igual a 3 characters'
    ],
    subidaRules: [
      v => !!v || 'Subida es requerido',
      v => v.length <= 50 || 'Subida debe ser menor o igual a  50 characters',
      v => v.length >= 3 || 'Subida debe ser mayor o igual a 3 characters'
    ],
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: '',
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
      buses: '',
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
      buses: '',
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
      this.loading = true
      this.error = false
      axios.get(url + 'trayectosR/')
        .then(response => {
          this.trayectos = response.data
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
    },
    editItem (item) {
      this.editedIndex = this.trayectos.indexOf(item)
      this.editedItem = Object.assign({}, item)
      var horariostr = item.horario
      var res = horariostr.split('T')
      this.editedItem.picker_date = res[0]
      this.editedItem.picker_time = res[1].slice(0, -1)
      this.dialog = true
    },
    deleteItem (item) {
      if (confirm('¿Estas seguro que quiere eliminar el trayecto?')) {
        axios.delete(url + 'trayectoCUD/' + item.id + '/').then(response => {
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
          axios.post(url + 'trayectoCUD/', {
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
            axios.put(url + 'trayectoCUD/' + this.editedItem.id + '/', {
              origen: this.editedItem.origen,
              destino: this.editedItem.destino,
              horario: this.editedItem.picker_date + ' ' + this.editedItem.picker_time,
              subida: this.editedItem.subida
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
    }
  },
  mounted () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
