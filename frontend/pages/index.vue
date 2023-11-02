<script>

export default {
  name: 'Index',
  data () {
    return {
      displayAlert: false,
      alertColor: 'success',
      messageAlert: 'Aguardando menssagem...',
      dados_viajem: {
        distancia: 'dist',
        vias_da_rota: 'vias_da_rota',
        consumo_total_de_combustivel: 'consumo_total_de_combustivel'
      },
      dataFormIsValid: false,
      dataForm: {
        origemLatitude: {value: '', mess: '', status: null},
        origemLongitude: {value: '', mess: '', status: null},
        destinoLatitude: {value: '', mess: '', status: null},
        destinoLongitude: {value: '', mess: '', status: null},
        mediaConsumoVeiculo: {value: '', mess: '', status: null},
        idaEVolta: {value: false, mess: '', status: null}
      },
      dataFormDefault: {
        origemLatitude: {value: '', mess: '', status: null},
        origemLongitude: {value: '', mess: '', status: null},
        destinoLatitude: {value: '', mess: '', status: null},
        destinoLongitude: {value: '', mess: '', status: null},
        mediaConsumoVeiculo: {value: '', mess: '', status: null},
        idaEVolta: {value: false, mess: '', status: null}
      },
      showRelatorioViagem: false,
      relatorioViagem: {
        consumo_total_de_combustivel: '',
        distancia_km: '',
        vias_da_rota: '',
        ida_e_volta: null
      },
      dataFormSnakeCase: {
        origem_latitude: null,
        origem_longitude: null,
        destino_latitude: null,
        destino_longitude: null,
        media_consumo_veiculo: null,
        ida_e_volta: false
      }
    }
  },
  methods: {
    getUrlBackend: function () {
      return process.env.NODE_ENV === 'production' ? 'https://match-calc-combustivel.vercel.app' : 'http://localhost:8000'
    },
    submeterFormViagem: async function () {
      const endpoint = '/viagem'
      const baseUrlBackend = this.getUrlBackend()
      await this.$axios.post(baseUrlBackend + endpoint, this.dataFormSnakeCase).then((response) => {
        if (response.status === 200) {
          console.log(response)
          this.relatorioViagem = response.data
          this.showRelatorioViagem = true
          this.messageAlert = 'Relatório de Viagem recebido com sucesso.'
          this.alertColor = 'success'
          this.showAlert()
        }
      }).catch((error) => {
        console.log(error)
        if (error.response.data.detail) {
          this.messageAlert = error.response.data.detail
        } else {
          if (error.response) {
            this.messageAlert = `Erro ${error.response.status}`
          } else {
            this.messageAlert = error
          }
        }
        this.alertColor = 'error'
        this.showAlert()
      })
    },
    resetarForm: function () {
      this.dataForm = Object.assign({}, this.dataFormDefault)
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert () {
      this.displayAlert = true
    },
    ruleLatitude: function (value) {
      let state = true
      let message = ""
      const latitudeFloat = parseFloat(value)
      if ( isNaN(latitudeFloat) ) {
        state = false
        message = 'Insira uma coordenada numérica.'
      }
      if ( latitudeFloat < -90 ) {
        state = false
        message = 'A latitude não pode ser menor do que -90'
      }
      if ( latitudeFloat > 90 ) {
        state = false
        message = 'A latitude não pode ser maior do que 90'
      }
      return {state, message}
    },
    ruleLongitude: function (value) {
      let state = true
      let message = ""
      const longitudeFloat = parseFloat(value)
      if ( isNaN(longitudeFloat) ) {
        state = false
        message = 'Insira uma coordenada numérica.'
      }
      if ( longitudeFloat < -180 ) {
        state = false
        message = 'A longitude não pode ser menor do que -180'
      }
      if ( longitudeFloat > 180 ) {
        state = false
        message = 'A longitude não pode ser maior do que 180'
      }
      return {state, message}
    },
    ruleIsNumberPositive: function (value) {
      let state = true
      let message = ""
      const numFloat = parseFloat(value)
      if ( isNaN(numFloat) ) {
        state = false
        message = 'Insira um valor numérico.'
      }
      if ( numFloat <= 0 ) {
        state = false
        message = 'Insira um valor maior que zero.'
      }
      return {state, message}
    },
    validarForm: function () {
      return this.dataForm.origemLatitude.status && this.dataForm.origemLongitude.status &&
          this.dataForm.destinoLatitude.status && this.dataForm.destinoLongitude.status &&
          this.dataForm.mediaConsumoVeiculo.status
    }
  },
  watch: {
    'dataForm.origemLatitude.value' (newValue) {
      if ( this.ruleLatitude(newValue).state ) {
        this.dataForm.origemLatitude.status = this.ruleLatitude(newValue).state
        this.dataForm.origemLatitude.mess = this.ruleLatitude(newValue).message
        this.dataFormSnakeCase.origem_latitude = parseFloat(newValue)
      } else {
        this.dataForm.origemLatitude.status = this.ruleLatitude(newValue).state
        this.dataForm.origemLatitude.mess = this.ruleLatitude(newValue).message
        this.dataFormSnakeCase.origem_latitude = null
      }
      this.dataFormIsValid = this.validarForm()
    },
    'dataForm.origemLongitude.value' (newValue) {
      if ( this.ruleLongitude(newValue).state ) {
        this.dataForm.origemLongitude.status = this.ruleLongitude(newValue).state
        this.dataForm.origemLongitude.mess = this.ruleLongitude(newValue).message
        this.dataFormSnakeCase.origem_longitude = parseFloat(newValue)
      } else {
        this.dataForm.origemLongitude.status = this.ruleLongitude(newValue).state
        this.dataForm.origemLongitude.mess = this.ruleLongitude(newValue).message
        this.dataFormSnakeCase.origem_longitude = null
      }
      this.dataFormIsValid = this.validarForm()
    },
    'dataForm.destinoLatitude.value' (newValue) {
      if ( this.ruleLatitude(newValue).state ) {
        this.dataForm.destinoLatitude.status = this.ruleLatitude(newValue).state
        this.dataForm.destinoLatitude.mess = this.ruleLatitude(newValue).message
        this.dataFormSnakeCase.destino_latitude = parseFloat(newValue)
      } else {
        this.dataForm.destinoLatitude.status = this.ruleLatitude(newValue).state
        this.dataForm.destinoLatitude.mess = this.ruleLatitude(newValue).message
        this.dataFormSnakeCase.destino_latitude = null
      }
      this.dataFormIsValid = this.validarForm()
    },
    'dataForm.destinoLongitude.value' (newValue) {
      if ( this.ruleLongitude(newValue).state ) {
        this.dataForm.destinoLongitude.status = this.ruleLongitude(newValue).state
        this.dataForm.destinoLongitude.mess = this.ruleLongitude(newValue).message
        this.dataFormSnakeCase.destino_longitude = parseFloat(newValue)
      } else {
        this.dataForm.destinoLongitude.status = this.ruleLongitude(newValue).state
        this.dataForm.destinoLongitude.mess = this.ruleLongitude(newValue).message
        this.dataFormSnakeCase.destino_longitude = null
      }
      this.dataFormIsValid = this.validarForm()
    },
    'dataForm.mediaConsumoVeiculo.value' (newValue) {
      if ( this.ruleIsNumberPositive(newValue).state ) {
        this.dataForm.mediaConsumoVeiculo.status = this.ruleIsNumberPositive(newValue).state
        this.dataForm.mediaConsumoVeiculo.mess = this.ruleIsNumberPositive(newValue).message
        this.dataFormSnakeCase.media_consumo_veiculo = parseFloat(newValue)
      } else {
        this.dataForm.mediaConsumoVeiculo.status = this.ruleIsNumberPositive(newValue).state
        this.dataForm.mediaConsumoVeiculo.mess = this.ruleIsNumberPositive(newValue).message
        this.dataFormSnakeCase.media_consumo_veiculo = null
      }
      this.dataFormIsValid = this.validarForm()
    },
    'dataForm.idaEVolta.value' (newValue) {
      this.dataFormSnakeCase.ida_e_volta = newValue
    },
  }
}
</script>

<template>
  <div class="cor-tertiary w-100">
    <v-container style="max-width: 1185px;">
      <v-alert :value="displayAlert" dismissible :color="alertColor" text outlined dense>
        {{ messageAlert }}
      </v-alert>
      <v-row class="g-5">
        <v-col sm="12" md="4">
          <v-card>
              <v-img width="400" src="https://img.freepik.com/vetores-premium/ilustracao-do-mapa-da-cidade-para-o-aplicativo-de-navegacao_8276-371.jpg?w=400"></v-img>
              <v-card-text v-if="!showRelatorioViagem" class="card-text">
                Calcula a quantidade de combustível necessária para percorrer uma determinada distância
                entre dois pontos, levando em consideração o consumo estimado do veículo.
              </v-card-text>
              <div v-else>
                <v-card-text>
                  <p v-if="relatorioViagem.ida_e_volta" class="text-h6">Para a viagem de ida e volta temos:</p>
                  <p v-else class="text-h6">Para apenas a viagem de ida:</p>
                  <p><b>Distância:</b> {{ relatorioViagem.distancia_km }} Km</p>
                  <p><b>Principais vias da rota:</b> {{ relatorioViagem.vias_da_rota }}</p>
                  <p><b>Litros necessários:</b>
                    {{ relatorioViagem.consumo_total_de_combustivel }}
                    litros
                  </p>
                </v-card-text>
              </div>

          </v-card>
        </v-col>
        <v-col sm="12" md="8">
          <h4 class="mb-3">Informe os dados da viagem</h4>
          <v-form @submit.prevent="submeterFormViagem" @reset="resetarForm" novalidate>
            <v-row dense>
              <v-col class="col-12 col-md-12 col-lg-4">
                <label for="origemLatitude">Coordenadas da origem:</label>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Latitude da Origem" v-model="dataForm.origemLatitude.value" id="origemLatitude" dense
                :error-messages="dataForm.origemLatitude.mess" :error="dataForm.origemLatitude.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Longitude da Origem" v-model="dataForm.origemLongitude.value" id="origemLongitude" dense
                :error-messages="dataForm.origemLongitude.mess" :error="dataForm.origemLongitude.state"></v-text-field>
              </v-col>
            </v-row>

            <v-row dense>
              <v-col class="col-12 col-md-12 col-lg-4">
                <label for="destinoLatitude">Coordenadas do destino:</label>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Latitude do Destino" v-model="dataForm.destinoLatitude.value" id="destinoLatitude" dense
                :error-messages="dataForm.destinoLatitude.mess" :error="dataForm.destinoLatitude.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Longitude do Destino" v-model="dataForm.destinoLongitude.value" id="destinoLongitude" dense
                :error-messages="dataForm.destinoLongitude.mess" :error="dataForm.destinoLongitude.state"></v-text-field>
              </v-col>
            </v-row>

            <v-row dense>
              <v-col class="col-12 col-sm-12 col-md-6">
                <label for="mediaConsumoVeiculo">Média de consumo do veículo:</label>
                <v-text-field v-model="dataForm.mediaConsumoVeiculo.value" id="mediaConsumoVeiculo" dense type="number"
                :error-messages="dataForm.mediaConsumoVeiculo.mess" :error="dataForm.mediaConsumoVeiculo.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-sm-12 col-md-4">
                <v-checkbox id="idaEVolta" label="Calcular ida e volta" v-model="dataForm.idaEVolta.value"></v-checkbox>
              </v-col>
            </v-row>

            <v-row dense>
              <div class="">
                <v-btn type="button" color="secundary" @click="resetarForm()">
                  Limpar
                  <v-icon right>mdi-trash-can</v-icon>
                </v-btn>
                <v-btn type="submit" id="btnSubmetForm" color="success" :disabled="!dataFormIsValid">
                  Enviar
                  <v-icon right>mdi-send</v-icon>
                </v-btn>
              </div>

            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped>
.cor-tertiary {
  background-color: rgba(248, 249, 250)
}
p{
  margin-bottom: 0.2rem;
}
</style>
