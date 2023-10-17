<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Main",
  data() {
    return {
      dismissSecs: 10,
      dismissCountDown: 0,
      showDismissibleAlert: false,
      alertVariant: "danger",
      messageAlert: "Aguardando menssagem...",
      dados_viajem: {
        distancia: "dist",
        vias_da_rota: "vias_da_rota",
        consumo_total_de_combustivel: "consumo_total_de_combustivel",
      },
      dataForm: {
        origemLatitude: "",
        origemLongitude: "",
        destinoLatitude: "",
        destinoLongitude: "",
        mediaConsumoVeiculo: "",
        idaEVolta: false,
      },
      dataFormDefault: {
        origemLatitude: "",
        origemLongitude: "",
        destinoLatitude: "",
        destinoLongitude: "",
        mediaConsumoVeiculo: "",
        idaEVolta: false,
      },
      showRelatorioViagem: false,
      relatorioViagem: {
        consumo_total_de_combustivel: "",
        distancia_km: "",
        vias_da_rota: ""
      }
    }
  },
  methods: {
    dataFormSnakeCase: function () {
      return {
        origem_latitude: this.dataForm.origemLatitude,
        origem_longitude: this.dataForm.origemLongitude,
        destino_latitude: this.dataForm.destinoLatitude,
        destino_longitude: this.dataForm.destinoLongitude,
        media_consumo_veiculo: this.dataForm.mediaConsumoVeiculo,
        ida_e_volta: this.dataForm.idaEVolta
      }
    },
    submeterForm: async function () {
      const baseUrlBackend = process.env.NODE_ENV === 'production' ? "https://match-calc-combustivel.vercel.app" : "http://localhost:8000"
      const endpoint = "/viagem"
      await this.$axios.post(baseUrlBackend + endpoint, this.dataFormSnakeCase()).then((response) => {
        if (response.status === 200) {
          this.relatorioViagem = response.data
          this.showRelatorioViagem = true
          this.messageAlert = "Relatório de Viagem recebido com sucesso."
          this.alertVariant = "success"
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
        this.alertVariant = "danger"
        this.showAlert()
      })
    },
    resetarForm: function () {
      this.dataForm = Object.assign({}, this.dataFormDefault)
    },
    countDownChanged(dismissCountDown: number) {
      this.dismissCountDown = dismissCountDown
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs
    }
  }
})
</script>

<template>
  <div class="py-3 pt-lg-3 cor-tertiary w-100">
    <b-container>
      <b-alert :show="dismissCountDown" dismissible :variant="alertVariant" @dismissed="dismissCountDown=0"
               @dismiss-count-down="countDownChanged">
        <p>{{ messageAlert }}</p>
        <b-progress variant="warning" :max="dismissSecs" :value="dismissCountDown" height="4px"></b-progress>
      </b-alert>
      <b-row class="g-5">
        <b-col sm="12" md="4">
          <b-card class="shadow-sm mb-4" img-alt="Mapa" img-top no-body
                  img-src="https://img.freepik.com/vetores-premium/ilustracao-do-mapa-da-cidade-para-o-aplicativo-de-navegacao_8276-371.jpg?w=400">
            <b-card-body>
              <b-card-text v-if="!showRelatorioViagem" class="card-text">
                Calcula a quantidade de combustível necessária para percorrer uma determinada distância
                entre dois pontos, levando em consideração o consumo estimado do veículo.
              </b-card-text>
              <div v-else>
                <b-card-text class="card-text">Distância: {{ relatorioViagem.distancia_km }} Km</b-card-text>
                <b-card-text class="card-text">Principais vias da rota: {{ relatorioViagem.vias_da_rota }}</b-card-text>
                <b-card-text class="card-text">Litros necessários: {{ relatorioViagem.consumo_total_de_combustivel }}
                  litros
                </b-card-text>
              </div>
            </b-card-body>
          </b-card>
        </b-col>
        <b-col sm="12" md="8">
          <h4 class="mb-3">Informe os dados da viagem</h4>
          <b-form @submit.prevent="submeterForm" @reset="resetarForm" novalidate>
            <b-row>
              <b-col md="12" lg="4">
                <label for="origemLatitude">Coordenadas da origem:</label>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Latitude da Origem" type="text" id="origemLatitude"
                                v-model="dataForm.origemLatitude" required></b-form-input>
                  <b-form-invalid-feedback id="origemLatitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Longitude da Origem" type="text" id="origemLongitude"
                                v-model="dataForm.origemLongitude" required></b-form-input>
                  <b-form-invalid-feedback id="origemLongitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
            </b-row>

            <b-row class="pt-3">
              <b-col md="12" lg="4">
                <label for="destinoLatitude">Coordenadas do destino:</label>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Latitude do destino" type="text" id="destinoLatitude"
                                v-model="dataForm.destinoLatitude" required></b-form-input>
                  <b-form-invalid-feedback id="destinoLatitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Longitude do Destino" type="text" id="destinoLongitude"
                                v-model="dataForm.destinoLongitude" required></b-form-input>
                  <b-form-invalid-feedback id="destinoLongitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
            </b-row>

            <b-row class="pt-3">
              <b-col sm="12" md="6">
                <label for="km_litro">Média de consumo do veículo:</label>
                <b-input-group size="sm" class="mb-3" append="Km/litro">
                  <b-form-input type="number" id="mediaConsumoVeiculo"
                                v-model="dataForm.mediaConsumoVeiculo" required></b-form-input>
                  <b-form-invalid-feedback id="km_litro-feedback">Insira a média de consumo.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col sm="12" md="4" class="py-sm-2">
                <b-form-checkbox id="idaEVolta" class="pt-3"
                  v-model="dataForm.idaEVolta" >Calcular ida e volta</b-form-checkbox>
              </b-col>
            </b-row>

            <b-row class="pt-5">
              <div class="">
                <button type="button" class="btn btn-secondary mx-2 float-end" @click="resetarForm()">
                  Limpar
                  <b-icon icon="trash" scale="1" class="ml-2"></b-icon>
                </button>
                <button type="submit" id="submitFormViagem" class="btn btn-success float-end px-5">
                  Enviar
                  <b-icon icon="check-lg" scale="1" class="ml-2"></b-icon>
                </button>
              </div>

            </b-row>
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped>
.cor-tertiary {
  background-color: rgba(248, 249, 250)
}
</style>
