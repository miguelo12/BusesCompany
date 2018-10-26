<template>
  <div>
    <v-toolbar flat>
      <v-toolbar-title>Pasajeros</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="primary" dark class="mb-2">Nuevo Pasajero</v-btn>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.nombre" :rules="nameRules" label="Nombre" required></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md4>
                    <v-text-field v-model="editedItem.rut" :rules="rutRules" label="Rut" required></v-text-field>
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
      class="elevation-2">
      <v-progress-linear slot="progress" color="blue" indeterminate></v-progress-linear>
      <template slot="items" slot-scope="props">
        <td width="200px" class="text-xs-left">{{ props.item.rut }}</td>
        <td width="200px" class="text-xs-left">{{ props.item.nombre }}</td>
        <td width="100px" class="justify-center layout px-0">
          <v-btn color="teal" @click="editItem(props.item)" flat>
            <v-icon>edit</v-icon>
          </v-btn>
          <v-btn color="teal" @click="deleteItem(props.item)" flat>
            <v-icon>delete</v-icon>
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
    loading: true,
    error: false,
    valid: false,
    dialog: false,
    snackbar: false,
    snackbar_color: '',
    snackbar_timeout: 100,
    snackbar_text: '',
    busesBox: [],
    nameRules: [
      v => !!v || 'Name is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Name must be less than 50 characters',
      v => v.length >= 3 || 'Rut must be more than 3 characters'
    ],
    rutRules: [
      v => !!v || 'Rut is required',
      v => /[0-9.]/.test(v) || 'Solo numeros.',
      v => v.length <= 11 || 'Rut must be less than 11 characters',
      v => v.length >= 10 || 'Rut must be more than 10 characters'
    ],
    headers: [
      {
        align: 'left',
        text: 'rut',
        value: 'rut'
      },
      {
        text: 'nombre',
        value: 'nombre'
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
      nombre: '',
      rut: ''
    },
    defaultItem: {
      codigo: '',
      nombre: '',
      rut: ''
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
      axios.get(url + 'pasajeros/')
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
      this.dialog = true
      // la fecha arreglar
    },
    deleteItem (item) {
      if (confirm('¿Estas seguro que quiere eliminar el trayecto?')) {
        axios.delete(url + 'pasajeros/' + item.id + '/').then(response => {
          this.initialize()
          this.$emit('pasajeroCRUD')
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
          axios.post(url + 'pasajeros/', {
            nombre: this.editedItem.nombre,
            rut: this.editedItem.rut
          }).then(response => {
            this.initialize()
            this.$emit('pasajeroCRUD')
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
            axios.put(url + 'pasajeros/' + this.editedItem.id + '/', {
              nombre: this.editedItem.nombre,
              rut: this.editedItem.rut
            }).then(response => {
              this.initialize()
              this.$emit('pasajeroCRUD')
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
