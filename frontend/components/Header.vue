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
</template>

<style scoped>

.bd-placeholder-img {
  font-size: 1.125rem;
  text-anchor: middle;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

@media (min-width: 768px) {
  .bd-placeholder-img-lg {
    font-size: 3.5rem;
  }
}

.b-example-divider {
  width: 100%;
  height: 3rem;
  background-color: rgba(0, 0, 0, .1);
  border: solid rgba(0, 0, 0, .15);
  border-width: 1px 0;
  box-shadow: inset 0 .5em 1.5em rgba(0, 0, 0, .1), inset 0 .125em .5em rgba(0, 0, 0, .15);
}

.b-example-vr {
  flex-shrink: 0;
  width: 1.5rem;
  height: 100vh;
}

.bi {
  vertical-align: -.125em;
  fill: currentColor;
}

.nav-scroller {
  position: relative;
  z-index: 2;
  height: 2.75rem;
  overflow-y: hidden;
}

.nav-scroller .nav {
  display: flex;
  flex-wrap: nowrap;
  padding-bottom: 1rem;
  margin-top: -1px;
  overflow-x: auto;
  text-align: center;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}

.btn-bd-primary {
  --bd-violet-bg: #712cf9;
  --bd-violet-rgb: 112.520718, 44.062154, 249.437846;

  --bs-btn-font-weight: 600;
  --bs-btn-color: var(--bs-white);
  --bs-btn-bg: var(--bd-violet-bg);
  --bs-btn-border-color: var(--bd-violet-bg);
  --bs-btn-hover-color: var(--bs-white);
  --bs-btn-hover-bg: #6528e0;
  --bs-btn-hover-border-color: #6528e0;
  --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
  --bs-btn-active-color: var(--bs-btn-hover-color);
  --bs-btn-active-bg: #5a23c8;
  --bs-btn-active-border-color: #5a23c8;
}

.bd-mode-toggle {
  z-index: 1500;
}

.bd-mode-toggle .dropdown-menu .active .bi {
  display: block !important;
}
</style>
