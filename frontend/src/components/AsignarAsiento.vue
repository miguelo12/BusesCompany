<template>
    <div>
        <b-jumbotron>
            <template slot="header">
                Asignar Asiento.
            </template>
            <template slot="lead">
                Eligir asiento para el pasajero.
            </template>
            <hr class="my-4" my-variant="primary">
            <div class="container">
                <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                    <div class="mx-auto" style="width: 250px;">
                        <b-card overlay
                                bg-variant="transparent"
                                border-variant="info"
                                style="max-width: 20rem;"
                                img-src="../assets/bus-top-edit.png"
                                img-alt="Card Image" class="mb-2">
                            <div class="card-text">
                              <b-container>
                                <b-col style="padding-top:145px; margin-left:19px; width:140px;">
                                  <b-button style="margin:3px; width: 48px;" :key="s" v-for="(item,s) in asientos" @click="provide(item)" v-bind:class="{'btn-info': contains(reserva, item),'btn-light': !contains(reserva, item)}" >{{ item.name }}</b-button>
                                </b-col>
                              </b-container>
                            </div>
                        </b-card>
                    </div>
                    <b-form-group id="exampleInputGroup3"
                                    label="Pasajero:"
                                    label-for="exampleInput3">
                        <b-form-select id="exampleInput3"
                                    :options="pasajero_id"
                                    required
                                    v-model="form.pasajero_id">
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
        pasajero_id: null,
        asientos: null,
        reserva: null
      },
      reserva: [],
      asientos: [{name: '1'}, {name: '2'}, {name: '3'}, {name: '4'}, {name: '5'}, {name: '6'}, {name: '7'}, {name: '8'}, {name: '9'}, {name: '10'}],
      pasajero_id: [
        { text: 'Seleccionar Pasajero', value: null },
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
      this.reserva = []
      this.show = false
      this.form.pasajero_id = null
      this.$nextTick(() => { this.show = true })
    },
    changeAsignar (s, evt) {
      if (this.asientos[s]) {
        this.asientos[s] = false
      } else {
        this.asientos[s] = true
      }
    },
    provide (item) {
      if (this.reserva.indexOf(item) === -1) {
        this.reserva.push(item)
      } else {
        this.reserva.splice(this.reserva.indexOf(item), 1)
      }
    },
    contains (arr, item) {
      return arr.indexOf(item) !== -1
    }
  }
}
</script>
<style lang="">
</style>
