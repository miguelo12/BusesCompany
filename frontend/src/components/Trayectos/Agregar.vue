<template>
        <v-container fluid>
            <h2 class="display-4">
                Trayecto
            </h2>
            <h3 class="display-2">
                Agregar nuevo trayecto.
            </h3>
            <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  v-model="origen"
                  :rules="origenRules"
                  :counter="50"
                  :messages="['Messages']"
                  prepend-icon="mdi-home"
                  label="Origen:"
                  required></v-text-field>

                <v-text-field
                  v-model="destino"
                  :rules="destinoRules"
                  :counter="50"
                  :messages="['Messages']"
                  prepend-icon="mdi-home"
                  label="Destino:"
                  required></v-text-field>

                <v-text-field
                  v-model="subida"
                  :rules="subidaRules"
                  :counter="50"
                  :messages="['Messages']"
                  prepend-icon="mdi-home"
                  label="subida:"
                  required></v-text-field>

                <v-flex xs12>
                  <v-dialog
                    ref="dialog1"
                    v-model="modal1"
                    :return-value.sync="picker_date"
                    persistent
                    lazy
                    full-width
                    width="290px"
                  >
                    <v-text-field
                      slot="activator"
                      v-model="picker_date"
                      label="Fecha:"
                      :rules="[v => !!v || 'Buses is required']"
                      prepend-icon="mdi-home"
                      :messages="['Messages']"
                      required
                      readonly
                    ></v-text-field>
                    <v-date-picker v-model="picker_date" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal1 = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog1.save(picker_date)">OK</v-btn>
                    </v-date-picker>
                  </v-dialog>
                </v-flex>

                <v-flex xs12>
                  <v-dialog
                    ref="dialog2"
                    v-model="modal2"
                    :return-value.sync="picker_time"
                    persistent
                    lazy
                    full-width
                    width="290px">
                    <v-text-field
                      slot="activator"
                      v-model="picker_time"
                      label="Hora:"
                      :rules="[v => !!v || 'Buses is required']"
                      prepend-icon="mdi-home"
                      :messages="['Messages']"
                      required
                      readonly></v-text-field>
                    <v-time-picker v-model="picker_time" scrollable>
                      <v-spacer></v-spacer>
                      <v-btn flat color="primary" @click="modal2 = false">Cancel</v-btn>
                      <v-btn flat color="primary" @click="$refs.dialog2.save(picker_time)">OK</v-btn>
                    </v-time-picker>
                  </v-dialog>
                </v-flex>

                <v-select
                  v-model="buses"
                  :items="items"
                  :rules="[v => !!v || 'Buses is required']"
                  :messages="['Messages']"
                  prepend-icon="mdi-home"
                  label="Buses:"
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
          horario: this.picker_date + ' ' + this.picker_time,
          subida: this.subida,
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
