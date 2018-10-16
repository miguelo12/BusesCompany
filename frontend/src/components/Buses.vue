<template>
    <div>
        <b-jumbotron>
            <template slot="header">
                Buses
            </template>
            <template slot="lead">
                Agregar nuevo bus.
            </template>
            <hr class="my-4">
            <div class="container">
                <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <b-form-group id="exampleInputGroup1"
                                    label="Matricula:"
                                    label-for="exampleInput1"
                                    description="Matricula del bus.">
                        <b-form-input id="exampleInput1"
                                    type="text"
                                    v-model="form.matricula"
                                    required
                                    placeholder="Ingresar Matricula">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup2"
                                    label="Chofer:"
                                    label-for="exampleInput2"
                                    description="El chofer quien va a manejar el bus.">
                        <b-form-select id="exampleInput3"
                                    :options="chofer_id"
                                    required
                                    v-model="form.chofer_id">
                        </b-form-select>
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
        chofer_id: null,
        todos: null
      },
      chofer_id: [
        { text: 'Seleccionar chofer', value: null },
        'Carrots', 'Beans', 'Tomatoes', 'Corn'
      ],
      show: true
    }
  },
  methods: {
    onSubmit (evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
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
