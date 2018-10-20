<template>
        <v-container fluid>
            <h2 class="display-4">
                Trayecto
            </h2>
            <h3 class="display-2">
                Lista de todos los trayectos.
            </h3>
            <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
            <v-btn @click="clear" color="error">Reset</v-btn>
        </v-container>
</template>
<script>
import axios from 'axios'

export default {
  data: () => ({
    valid: false,
    picker_date: null,
    picker_time: null,
    modal1: false,
    modal2: false,
    origen: '',
    destino: '',
    subida: '',
    origenRules: [
      v => !!v || 'Matricula is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Matricula must be less than 50 characters',
      v => v.length >= 3 || 'Matricula must be more than 3 characters'
    ],
    destinoRules: [
      v => !!v || 'Matricula is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Matricula must be less than 50 characters',
      v => v.length >= 3 || 'Matricula must be more than 3 characters'
    ],
    subidaRules: [
      v => !!v || 'Subida is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Subida must be less than 50 characters',
      v => v.length >= 3 || 'Subida must be more than 3 characters'
    ],
    buses: null,
    items: [
      'Ejemplo 1',
      'Ejemplo 2',
      'Ejemplo 3',
      'Ejemplo 4'
    ]
  }),
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        axios.post('http://localhost:8000/api/buses/', {
          origen: this.origen,
          destino: this.destino,
          subida: this.subida,
          horario: this.picker_date + ' ' + this.picker_time,
          buses: this.buses
        }).then(response => {
          alert(response.id)
        }).catch(e => {
          alert(e)
        })
      }
    },
    clear () {
      this.$refs.form.reset()
    }
  }
}
</script>
<style lang="">
</style>
