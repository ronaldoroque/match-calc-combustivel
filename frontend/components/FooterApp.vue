<script>
export default {
  name: 'FooterApp'
}
</script>

<template>
<div class="text-body-secondary py-5">
    <div class="container" style="max-width: 1185px;">
        <p class="mb-1">Projeto desenvolvido no âmbito da
          <a href="https://match.mastertech.com.br" target="_blank">Formação
            <v-img height=".8rem" width="4rem" contain src="match.png" class="d-inline-flex"></v-img></a>
          - turma julho/2023.</p>

        <p class="mb-1">Para ver o código fonte do projeto, acesse o
          <a href="https://github.com/ronaldoroque/match-calc-combustivel" target="_blank">repositório do Github.
            <v-icon class="ml-2" medium>mdi-github</v-icon>
          </a>
          </p>

        <p class="mb-1">Link para visualização da playlist de demonstração no
          <a href=" https://youtube.com/playlist?list=PLgXMeadf-pzu4iCCTY4NEzu7c3Xp3jtyw&si=QNoFMHTNxnuC5pur"
             target="_blank">Youtube
             <v-icon class="ml-2" medium>mdi-youtube</v-icon>

          </a>

        </p>

    </div>
</div>
</template>

<style scoped>
a{
  color: blue;
}
</style>
