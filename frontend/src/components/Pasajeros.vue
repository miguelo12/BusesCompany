<template>
    <div>
        <b-jumbotron>
            <template slot="header">
                Pasajero
            </template>
            <template slot="lead">
                Agregar nuevo Pasajero.
            </template>
            <hr class="my-4">
            <div class="container">
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
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
                </b-form>
            </div>
        </b-jumbotron>
    </div>
</template>
<script>
import DatePicker from 'vue2-datepicker'

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
      axios.post('http://localhost:8000/api/pasajeros/', {
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
