<template>
    <div>
        <b-jumbotron>
            <template slot="header">
                Trayecto
            </template>
            <template slot="lead">
                Agregar nuevo trayecto.
            </template>
            <hr class="my-4">
            <div class="container">
                <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <b-form-group id="exampleInputGroup1"
                                    label="Origen:"
                                    label-for="exampleInput1"
                                    description="Debe ser donde comienza el viaje.">
                        <b-form-input id="exampleInput1"
                                    type="text"
                                    v-model="form.origen"
                                    required
                                    placeholder="Ingresar Origen">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup2"
                                    label="Destino:"
                                    label-for="exampleInput2"
                                    description="Debe ser donde termina el viaje.">
                        <b-form-input id="exampleInput2"
                                    type="text"
                                    v-model="form.destino"
                                    required
                                    placeholder="Ingresar Destino">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup3"
                                    label="Horario:"
                                    label-for="exampleInput3"
                                    description="El horario que tomara el bus.">
                                    <date-picker id="exampleInput3" v-model="form.horario" lang="es" type="datetime" :time-picker-options="timePickerOptions"  format="YYYY-MM-DD hh:mm:ss" confirm required></date-picker>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup4"
                                    label="Subida:"
                                    label-for="exampleInput4"
                                    description="En que terminal subira el pasajero.">
                        <b-form-input id="exampleInput4"
                                    type="text"
                                    v-model="form.pasajero"
                                    required
                                    placeholder="Ingresar Subida">
                        </b-form-input>
                    </b-form-group>
                    <b-form-group id="exampleInputGroup3"
                                    label="Buses:"
                                    label-for="exampleInput3">
                        <b-form-select id="exampleInput3"
                                    :options="buses_id"
                                    required
                                    v-model="form.buses_id">
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
        origen: '',
        destino: '',
        buses_id: null,
        horario: ''
      },
      buses_id: [
        { text: 'Seleccionar bus', value: null },
        'Carrots', 'Beans', 'Tomatoes', 'Corn'
      ],
      timePickerOptions: {
        start: '00:00',
        step: '00:15',
        end: '24:00'
      },
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
      this.form.origen = ''
      this.form.destino = ''
      this.form.horario = null
      this.form.subida = ''
      this.form.buses_id = null
      /* Trick to reset/clear native browser form validation state */
      this.show = false
      this.$nextTick(() => { this.show = true })
    }
  }
}
</script>
<style lang="">
</style>
