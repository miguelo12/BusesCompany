<template>
        <v-container fluid>
            <h2 class="display-4">
                Chofer
            </h2>
            <h3 class="display-2">
                Agregar nuevo Chofer.
            </h3>
            <hr class="my-4">
            <div class="container">

            <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  v-model="nombre"
                  :rules="nameRules"
                  :counter="50"
                  label="Nombre:"
                  required></v-text-field>
                <v-text-field
                  v-model="rut"
                  :rules="rutRules"
                  :counter="11"
                  label="Rut:"
                  required></v-text-field>
              <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
              <v-btn @click="clear" color="error">Reset</v-btn>
            </v-form>
            </div>
        </v-container>
</template>
<script>
import axios from 'axios'

export default {
  data: () => ({
    valid: false,
    nombre: '',
    rut: '',
    nameRules: [
      v => !!v || 'Name is required',
      v => /^[A-Za-z]+$/.test(v) || 'Solo Palabras.',
      v => v.length <= 50 || 'Name must be less than 50 characters',
      v => v.length >= 3 || 'Name must be more than 3 characters'
    ],
    rutRules: [
      v => !!v || 'Rut is required',
      v => /[0-9.]/.test(v) || 'Solo numeros.',
      v => v.length <= 11 || 'Rut must be less than 11 characters',
      v => v.length >= 10 || 'Rut must be more than 10 characters'
    ]
  }),
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        axios.post('http://localhost:8000/api/choferes/', {
          nombre: this.nombre,
          rut: this.rut
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
