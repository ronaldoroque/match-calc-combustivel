<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Header",
  data() {
    return {
      expanded: false,
    }
  }
})
</script>

<template>
  <div class="w-100 bg-dark">
    <b-container>
      <b-navbar toggleable type="dark" variant="dark">
        <b-navbar-brand href="#">Calculadora de Combustível</b-navbar-brand>
        <button v-if="expanded" type="button" class="btn btn-secondary float-end ml-auto py-0 py-md-1" size="sm" @click="expanded=!expanded">
                Sobre o Projeto <b-icon icon="chevron-bar-up" class="ml-2"></b-icon></button>
        <button v-else type="button" class="btn btn-secondary float-end ml-auto py-0 py-md-1" size="sm" @click="expanded=!expanded">
                Sobre o Projeto <b-icon icon="chevron-bar-down" class="ml-2"></b-icon></button>

        <b-collapse id="navbar-toggle-collapse" v-model="expanded" is-nav>
          <div class="container text-white">
            <div class="row">
              <div class="col-sm-8 col-md-7 py-4">
                <h4>Sobre o Projeto</h4>
                <p class="text-body-secondary">
                  Neste projeto, os alunos criarão uma aplicação em Python que calculará a quantidade de
                  combustível necessária para percorrer uma determinada distância entre dois pontos,
                  levando em consideração o consumo estimado do veículo fornecido pelo usuário. A
                  aplicação utilizará uma API de mapas para calcular a distância entre os pontos.
                </p>
              </div>
              <div class="col-sm-4 offset-md-1 py-4">
                <h4>Participantes</h4>
                <ul class="list-unstyled">
                  <li><a href="https://www.linkedin.com/in/andrade-rog" class="text-light border-bottom">
                    Rogério Andrade <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon></a></li>
                  <li><a href="https://www.linkedin.com/in/doroque" class="text-light border-bottom">
                    Ronaldo Roque <b-icon icon="linkedin" scale="1" class="ml-2"></b-icon></a></li>
                </ul>
              </div>
            </div>
          </div>
        </b-collapse>
      </b-navbar>
    </b-container>
  </div>
</template>
