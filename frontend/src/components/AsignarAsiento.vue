<template>
    <div>
        <b-jumbotron>
            <template slot="header">
                Asignar Asiento.
            </template>
            <template slot="lead">
                Eligir asiento para el pasajero.
            </template>
            <hr class="my-4">
            <div class="container">
                <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <ol>
                        <li :key="s" v-for="(n,s) in numbers">
                            <b-button v-bind:class="{ 'success': n }" @click="changeAsignar(s)">{{ s+1 }}</b-button>
                        </li>
                    </ol>
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
        todos: null,
        numbers: null
      },
      numbers: [ false, false, false, false, false, false, false, false, false, false],
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
      this.form.nombre = ''
      this.form.rut = ''
      this.show = false
      this.$nextTick(() => { this.show = true })
    },
    changeAsignar (s, evt) {
      if(this.numbers[s]){
          this.numbers[s] = false;
      }else{
          this.numbers[s] = true;
      }

      
    }
  }
}
</script>
<style lang="">
</style>
