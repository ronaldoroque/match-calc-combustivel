<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Main",
  data() {
    return {
      dismissSecs: 10,
      dismissCountDown: 0,
      showDismissibleAlert: false,
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
      try {
        // Enviar a requisição para o Backend:
        const baseUrlBackend = process.env.NODE_ENV === 'production' ? "https://match-calc-combustivel.vercel.app": "http://localhost:8000"
        const endpoint = "/distance"
        const data = this.dataFormSnakeCase()
        let response = await this.$axios.post(baseUrlBackend + endpoint, data)
        if (response.status === 200) {
          this.messageAlert = response.data.detail
          this.showAlert()
          this.$store.commit('setloading', {loading: false})
        }
      } catch (error) {
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
        this.showAlert()
      }
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
      <b-alert :show="dismissCountDown" dismissible variant="danger" @dismissed="dismissCountDown=0"
               @dismiss-count-down="countDownChanged">
        <p>{{ messageAlert }}</p>
        <b-progress variant="warning" :max="dismissSecs" :value="dismissCountDown" height="4px"></b-progress>
      </b-alert>
      <b-row class="g-5">
        <b-col sm="12" md="4">
          <b-card class="shadow-sm mb-4" img-alt="Mapa" img-top no-body
                img-src="https://img.freepik.com/vetores-premium/ilustracao-do-mapa-da-cidade-para-o-aplicativo-de-navegacao_8276-371.jpg?w=400">
            <b-card-body>
              <b-card-text class="card-text">
                Calcula a quantidade de combustível necessária para percorrer uma determinada distância
                entre dois pontos, levando em consideração o consumo estimado do veículo.
              </b-card-text>
              <b-card-text class="card-text">Distância: {{ dados_viajem.distancia }} Km</b-card-text>
              <b-card-text class="card-text">Principais vias da rota: {{ dados_viajem.vias_da_rota }}</b-card-text>
              <b-card-text class="card-text">Litros necessários: {{ dados_viajem.consumo_total_de_combustivel }} litros</b-card-text>

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
                  <b-form-input placeholder="Latitude da Origem" type="text" v-model="dataForm.origemLatitude" required></b-form-input>
                  <b-form-invalid-feedback id="origemLatitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Longitude da Origem" type="text" v-model="dataForm.origemLongitude" required></b-form-input>
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
                  <b-form-input placeholder="Latitude do destino" type="text" v-model="dataForm.destinoLatitude" required></b-form-input>
                  <b-form-invalid-feedback id="destinoLatitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col md="6" lg="4">
                <b-input-group size="sm" class="mb-2">
                  <b-form-input placeholder="Longitude do Destino" type="text" v-model="dataForm.destinoLongitude" required></b-form-input>
                  <b-form-invalid-feedback id="destinoLongitude-feedback">Insira a coordenada.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
            </b-row>

            <b-row class="pt-3">
              <b-col sm="12" md="6">
                <label for="km_litro">Média de consumo do veículo:</label>
                <b-input-group size="sm" class="mb-3" append="Km/litro">
                  <b-form-input type="number" v-model="dataForm.mediaConsumoVeiculo" required></b-form-input>
                  <b-form-invalid-feedback id="km_litro-feedback">Insira a média de consumo.</b-form-invalid-feedback>
                </b-input-group>
              </b-col>
              <b-col sm="12" md="4" class="py-sm-2">
                <b-form-checkbox v-model="dataForm.idaEVolta" class="pt-3">Calcular ida e volta</b-form-checkbox>
              </b-col>
            </b-row>

            <b-row class="pt-5">
              <div class="">
                <button type="button" class="btn btn-secondary mx-2 float-end" @click="resetarForm()">
                  Limpar <b-icon icon="trash" scale="1" class="ml-2"></b-icon></button>
                <button type="submit" class="btn btn-success float-end px-5">
                  Enviar <b-icon icon="check-lg" scale="1" class="ml-2"></b-icon></button>
              </div>

            </b-row>
          </b-form>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped>
.cor-tertiary{
  background-color: rgba(248, 249, 250)
}
</style>
