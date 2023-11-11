<script>
import rules from "@/utils/rules"

export default {
  name: 'Index',
  data() {
    return {
      displayAlert: false,
      alertTimeout: 100,
      alertTimeoutIntervId: null,
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
        vias_da_rota: [],
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
      return process.env.NODE_ENV === 'production' ? 'https://match-calc-combustivel.vercel.app': 'http://localhost:8000'
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
    showAlert() {
      this.displayAlert = true
    },
    validarForm: function () {
      return this.dataForm.origemLatitude.status && this.dataForm.origemLongitude.status &&
        this.dataForm.destinoLatitude.status && this.dataForm.destinoLongitude.status &&
        this.dataForm.mediaConsumoVeiculo.status
    },
    validarField: function (newValue, rule, field, fieldSnakeCase) {
      const validationResult = rule(newValue)
      field.status = validationResult.state
      field.mess = validationResult.message
      this.dataFormIsValid = this.validarForm()
      return validationResult
    },
    alertRunTimeout: function (timeOut) {
      const resolution = 30
      const timeToReloadVal = timeOut/resolution
      const percent = 100/resolution
      if (!this.alertTimeoutIntervId) {
        this.alertTimeoutIntervId = setInterval(() => {
          this.alertTimeout = this.alertTimeout - percent
        }, timeToReloadVal);
      }
    },
    alertClose: function () {
      this.displayAlert = false
      clearInterval(this.alertTimeoutIntervId)
      this.alertTimeoutIntervId = null
    }
  },
  watch: {
    displayAlert(new_val) {
      const timeOut = 4000
      if (new_val) {
        this.alertRunTimeout(timeOut)
        setTimeout(() => {
          this.alertClose()
        }, timeOut)
      }
    },
    'dataForm.origemLatitude.value'(newValue) {
      const validationResult = this.validarField(newValue, rules.ruleLatitude, this.dataForm.origemLatitude)
      this.dataFormSnakeCase.origem_latitude = validationResult.valueClear
    },
    'dataForm.origemLongitude.value'(newValue) {
      const validationResult = this.validarField(newValue, rules.ruleLongitude, this.dataForm.origemLongitude)
      this.dataFormSnakeCase.origem_longitude = validationResult.valueClear
    },
    'dataForm.destinoLatitude.value'(newValue) {
      const validationResult = this.validarField(newValue, rules.ruleLatitude, this.dataForm.destinoLatitude)
      this.dataFormSnakeCase.destino_latitude = validationResult.valueClear
    },
    'dataForm.destinoLongitude.value'(newValue) {
      const validationResult = this.validarField(newValue, rules.ruleLongitude, this.dataForm.destinoLongitude)
      this.dataFormSnakeCase.destino_longitude = validationResult.valueClear
    },
    'dataForm.mediaConsumoVeiculo.value'(newValue) {
      const validationResult = this.validarField(newValue, rules.ruleIsNumberPositive, this.dataForm.mediaConsumoVeiculo)
      this.dataFormSnakeCase.media_consumo_veiculo = validationResult.valueClear
    },
    'dataForm.idaEVolta.value'(newValue) {
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
    <v-progress-linear color="grey" :value="alertTimeout" reverse></v-progress-linear>
      </v-alert>
      <v-row class="g-5">
        <v-col sm="12" md="5">
          <v-card>
            <v-card-text v-if="!showRelatorioViagem" class="card-text">
              Calcula a quantidade de combustível necessária para percorrer uma determinada distância
              entre dois pontos, levando em consideração o consumo estimado do veículo.
            </v-card-text>
            <div v-else>
              <v-card-text data-cy="reportCard">
                <h2 v-if="relatorioViagem.ida_e_volta" class="mb-3">Para a viagem de ida e volta temos:</h2>
                <h2 v-else class="mb-3">Para apenas a viagem de ida:</h2>
                <h3 class="mb-1"><b>Combustível necessário:</b> {{ relatorioViagem.consumo_total_de_combustivel }} litros</h3>
                <p><b>Distância:</b> {{ relatorioViagem.distancia_km }} Km</p>
                <p><b>Principais vias da rota:</b></p>

                <v-timeline align-top dense>
                  <v-timeline-item small v-for="(place, index) in relatorioViagem.vias_da_rota" :key="index"
                               :color="place.type === 'origem'? 'pink': ( place.type === 'destino'? 'green': 'blue')" >
                    <v-row class="pt-1"><v-col>{{ place.name }}</v-col></v-row>
                  </v-timeline-item>
                </v-timeline>

              </v-card-text>
            </div>
            <v-img width="470"
                   src="https://img.freepik.com/vetores-premium/ilustracao-do-mapa-da-cidade-para-o-aplicativo-de-navegacao_8276-371.jpg?w=400"></v-img>
          </v-card>
        </v-col>
        <v-col sm="12" md="7">
          <h4 class="mb-3">Informe os dados da viagem</h4>
          <v-form @submit.prevent="submeterFormViagem" @reset="resetarForm" novalidate>
            <v-row dense>
              <v-col class="col-12 col-md-12 col-lg-4">
                <label for="origemLatitude">Coordenadas da origem:</label>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Latitude da Origem" v-model="dataForm.origemLatitude.value" id="origemLatitude"
                              dense
                              :error-messages="dataForm.origemLatitude.mess"
                              :error="dataForm.origemLatitude.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Longitude da Origem" v-model="dataForm.origemLongitude.value" id="origemLongitude"
                              dense
                              :error-messages="dataForm.origemLongitude.mess"
                              :error="dataForm.origemLongitude.state"></v-text-field>
              </v-col>
            </v-row>

            <v-row dense>
              <v-col class="col-12 col-md-12 col-lg-4">
                <label for="destinoLatitude">Coordenadas do destino:</label>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Latitude do Destino" v-model="dataForm.destinoLatitude.value" id="destinoLatitude"
                              dense
                              :error-messages="dataForm.destinoLatitude.mess"
                              :error="dataForm.destinoLatitude.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-md-6 col-lg-4">
                <v-text-field label="Longitude do Destino" v-model="dataForm.destinoLongitude.value"
                              id="destinoLongitude" dense
                              :error-messages="dataForm.destinoLongitude.mess"
                              :error="dataForm.destinoLongitude.state"></v-text-field>
              </v-col>
            </v-row>

            <v-row dense>
              <v-col class="col-12 col-sm-12 col-md-6">
                <label for="mediaConsumoVeiculo">Média de consumo do veículo:</label>
                <v-text-field v-model="dataForm.mediaConsumoVeiculo.value" id="mediaConsumoVeiculo" dense type="number"
                              :error-messages="dataForm.mediaConsumoVeiculo.mess"
                              :error="dataForm.mediaConsumoVeiculo.state"></v-text-field>
              </v-col>
              <v-col class="col-12 col-sm-12 col-md-4">
                <v-checkbox id="idaEVolta" label="Calcular ida e volta" v-model="dataForm.idaEVolta.value"></v-checkbox>
                <input type="hidden" data-cy="idaEVolta" :value="dataForm.idaEVolta.value">
              </v-col>
            </v-row>

            <v-row dense>
              <div class="">
                <v-btn type="button" color="secundary" data-cy="resetForm" @click="resetarForm()">
                  Limpar
                  <v-icon right>mdi-trash-can</v-icon>
                </v-btn>
                <v-btn type="submit" id="btnSubmitForm" data-cy="SubmitForm" color="success"
                       :disabled="!dataFormIsValid">
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

p {
  margin-bottom: 0.2rem;
}
</style>
