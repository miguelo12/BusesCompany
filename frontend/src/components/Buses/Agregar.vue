<template>
  <v-container fluid>
    <h3 class="display-3">
      Bus
    </h3>
    <h4 class="display-1">
      Datos del bus {{ idBus }}
    </h4>
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
          axios.put(url + 'BusSet/' + this.idBus + '/', {
            matricula: this.matricula,
            choferes: this.chofer
          }).then(response => {
            alert(response.data)
          }).catch(e => {
            alert(e)
          })
        } else {
          axios.post(url + 'BusSet/', {
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
      axios.put(url + 'trayectoSet/' + this.idTrayecto + '/', {
        choferes: idbus
      }).then(response => {
        this.items(response.id)
      }).catch(e => {
        alert(e)
      })
    },
    initialize () {
      axios.get(url + 'choferes/')
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
