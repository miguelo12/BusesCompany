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
        :rules="[v => !!v || 'Chofer is required']"
        label="Chofer:"
        :item-text="item => item.nombre+' '+item.rut" :item-value="item => item.id"
        required></v-select>
      <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
      <v-btn @click="clear" color="error">Reset</v-btn>
      <br>
    </v-form>
  </v-container>
</template>
<script>
import axios from 'axios'

const url = 'http://localhost:8000/api/'

export default {
  data: () => ({
    valid: false,
    matricula: '',
    matriculaRules: [
      v => !!v || 'Matricula is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Matricula must be less than 50 characters',
      v => v.length >= 3 || 'Matricula must be more than 3 characters'
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
          }).catch(e => {
            alert(e)
          })
        } else {
          axios.post(url + 'busCUD/', {
            matricula: this.matricula,
            choferes: this.chofer
          }).then(response => {
            this.update(response.data.id)
          }).catch(e => {
            alert(e)
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
        alert(e)
      })
    },
    initialize () {
      if (this.idBus) {
        axios.get(url + 'busesR/' + this.idBus + '/')
          .then(response => {
            this.matricula = response.data.matricula
            this.chofer = response.data.choferes.id
          }).catch(e => {
            alert(e)
          })
      }

      axios.get(url + 'choferesCRUD/')
        .then(response => {
          this.items = response.data
        }).catch(e => {
          alert(e)
        })
    },
    clear () {
      this.$refs.form.reset()
    }
  },
  mounted () {
    this.initialize()
  }
}
</script>
<style lang="">
</style>
