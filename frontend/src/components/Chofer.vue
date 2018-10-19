<template>
    <div>
        <v-container fluid>
            <h1 class="display-4">
                Chofer
            </h1>
            <h2 class="display-3">
                Agregar nuevo Chofer.
            </h2>
            <!-- <hr class="my-4"> -->
            <div class="container">

            <v-form @submit="onSubmit" @reset="onReset" v-if="show" v-model="valid">
                <v-text-field
                  v-model="form.nombre"
                  :rules="nameRules"
                  :counter="10"
                  label="Nombre:"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>
              </v-form>

                <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <b-form-group id="exampleInputGroup1"
                                    label="Nombre:"
                                    label-for="exampleInput1"
                                    description="Nombre del pasajero.">
                        <b-form-input id="exampleInput1"
                                    type="text"
                                    v-model="form.nombre"
                                    required
                                    placeholder="Ingresar Nombre">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup2"
                                    label="Rut:"
                                    label-for="exampleInput2"
                                    description="Rut del pasajero.">
                        <b-form-input id="exampleInput2"
                                    type="text"
                                    v-model="form.rut"
                                    required
                                    placeholder="Ingresar Rut">
                        </b-form-input>
                    </b-form-group>
                    <br>
                <v-btn type="submit" color="info">Submit</v-btn>
                <v-btn type="reset" color="error">Reset</v-btn>
                </b-form>

            </div>
        </v-container>
    </div>
</template>
<script>
import DatePicker from 'vue2-datepicker'
import axios from 'axios'

export default {
  components: { DatePicker },
  data () {
    return {
      form: {
        nombre: '',
        rut: ''
      },
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      var nombre = this.form.nombre
      var rut = this.form.rut
      // Fetches posts when the component is created.
      axios.post('http://localhost:8000/api/choferes/', {
        nombre: nombre,
        rut: rut
      }).then(response => {
        alert(response.id)
      }).catch(e => {
        this.errors.push(e)
      })
    },
    onReset (evt) {
      evt.preventDefault()
      /* Reset our form values */
      this.form.nombre = ''
      this.form.rut = ''
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    }
  }
}
</script>
<style lang="">
</style>
