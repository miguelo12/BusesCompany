<template>
        <v-container fluid>
            <h2 class="display-4">
                Buses
            </h2>
            <h3 class="display-2">
                Agregar nuevo bus.
            </h3>
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
                  required></v-select>
              <v-btn :disabled="!valid" @click="submit" color="info">Submit</v-btn>
              <v-btn @click="clear" color="error">Reset</v-btn>
            </v-form>
        </v-container>
</template>
<script>
import axios from 'axios'

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
          matricula: this.matricula,
          chofer: this.chofer
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
