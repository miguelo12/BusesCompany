<template>
  <v-container fluid>
    <h3 class="display-3">
      Bus
    </h3>
    <h4 class="display-1">
      Datos del bus
    </h4>
    <br>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        v-model="matricula"
        :rules="matriculaRules"
        :counter="50"
        label="Matricula:"
        required></v-text-field>
      <v-select
        v-model="chofer"
        :items="items"
        :rules="[v => !!v || 'Chofer es requerido']"
        label="Chofer:"
        :item-text="item => item.nombre+' '+item.rut" :item-value="item => item.id"
        required></v-select>
      <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
      <br>
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
        @click="snackbar = false">
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
    matricula: '',
    matriculaRules: [
      v => !!v || 'Matricula es requerido',
      v => v.length <= 50 || 'Matricula debe ser menor o igual a 50 characters',
      v => v.length >= 3 || 'Matricula debe ser mayor o igual a 3 characters'
    ],
    chofer: null,
    items: []
  }),
  props: ['idTrayecto', 'idBus'],
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        if (this.idBus) {
          axios.patch(url + 'busCUD/' + this.idBus + '/', {
            matricula: this.matricula,
            choferes: this.chofer
          }).then(response => {
            this.initialize()
            this.snackbar_color = 'success'
            this.snackbar_timeout = 3000
            this.snackbar_text = 'Se ha actualizado con exito.'
            this.snackbar = true
          }).catch(e => {
            this.snackbar_color = 'error'
            this.snackbar_timeout = 3000
            this.snackbar_text = 'No has seleccionado asiento.'
            this.snackbar = true
          })
        } else {
          axios.post(url + 'busCUD/', {
            matricula: this.matricula,
            choferes: this.chofer
          }).then(response => {
            this.update(response.data.id)
            this.snackbar_color = 'success'
            this.snackbar_timeout = 3000
            this.snackbar_text = 'Se ha ingresado con exito.'
            this.snackbar = true
          }).catch(e => {
            this.snackbar_color = 'error'
            this.snackbar_timeout = 3000
            this.snackbar_text = 'No has seleccionado asiento.'
            this.snackbar = true
          })
        }
      }
    },
    update (idbus) {
      axios.patch(url + 'trayectoCUD/' + this.idTrayecto + '/', {
        buses: idbus
      }).then(response => {
        this.$emit('busCUD', idbus)
      }).catch(e => {
        this.snackbar_color = 'error'
        this.snackbar_timeout = 3000
        this.snackbar_text = 'Error inesperado.'
        this.snackbar = true
      })
    },
    initialize () {
      if (this.idBus) {
        axios.get(url + 'busesR/' + this.idBus + '/')
          .then(response => {
            this.matricula = response.data.matricula
            this.chofer = response.data.choferes.id
          }).catch(e => {
            this.snackbar_color = 'error'
            this.snackbar_timeout = 3000
            this.snackbar_text = 'Error inesperado.'
            this.snackbar = true
          })
      }
      axios.get(url + 'choferesCRUD/')
        .then(response => {
          this.items = response.data
        }).catch(e => {
          this.snackbar_color = 'error'
          this.snackbar_timeout = 3000
          this.snackbar_text = 'Error inesperado.'
          this.snackbar = true
        })
    }
  },
  mounted () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
