(window.webpackJsonp=window.webpackJsonp||[]).push([[4],{350:function(t,e,o){var content=o(352);content.__esModule&&(content=content.default),"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);(0,o(113).default)("09a6e41a",content,!0,{sourceMap:!1})},351:function(t,e,o){"use strict";o(350)},352:function(t,e,o){var r=o(112)((function(i){return i[1]}));r.push([t.i,".cor-tertiary[data-v-54c393bb]{background-color:#f8f9fa}",""]),r.locals={},t.exports=r},355:function(t,e,o){"use strict";o.r(e);var r,d=o(27),n=(o(63),o(8)),m=Object(n.defineComponent)({name:"Main",data:function(){return{dismissSecs:10,dismissCountDown:0,showDismissibleAlert:!1,alertVariant:"danger",messageAlert:"Aguardando menssagem...",dados_viajem:{distancia:"dist",vias_da_rota:"vias_da_rota",consumo_total_de_combustivel:"consumo_total_de_combustivel"},dataForm:{origemLatitude:"",origemLongitude:"",destinoLatitude:"",destinoLongitude:"",mediaConsumoVeiculo:"",idaEVolta:!1},dataFormDefault:{origemLatitude:"",origemLongitude:"",destinoLatitude:"",destinoLongitude:"",mediaConsumoVeiculo:"",idaEVolta:!1},showRelatorioViagem:!1,relatorioViagem:{consumo_total_de_combustivel:"",distancia_km:"",vias_da_rota:""}}},methods:{dataFormSnakeCase:function(){return{origem_latitude:this.dataForm.origemLatitude,origem_longitude:this.dataForm.origemLongitude,destino_latitude:this.dataForm.destinoLatitude,destino_longitude:this.dataForm.destinoLongitude,media_consumo_veiculo:this.dataForm.mediaConsumoVeiculo,ida_e_volta:this.dataForm.idaEVolta}},submeterForm:(r=Object(d.a)(regeneratorRuntime.mark((function t(){var e=this;return regeneratorRuntime.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=4,this.$axios.post("https://match-calc-combustivel.vercel.app/viagem",this.dataFormSnakeCase()).then((function(t){200===t.status&&(e.relatorioViagem=t.data,e.showRelatorioViagem=!0,e.messageAlert="Relatório de Viagem recebido com sucesso.",e.alertVariant="success",e.showAlert())})).catch((function(t){console.log(t),t.response.data.detail?e.messageAlert=t.response.data.detail:t.response?e.messageAlert="Erro ".concat(t.response.status):e.messageAlert=t,e.alertVariant="danger",e.showAlert()}));case 4:case"end":return t.stop()}}),t,this)}))),function(){return r.apply(this,arguments)}),resetarForm:function(){this.dataForm=Object.assign({},this.dataFormDefault)},countDownChanged:function(t){this.dismissCountDown=t},showAlert:function(){this.dismissCountDown=this.dismissSecs}}}),c=m,l=(o(351),o(71)),component=Object(l.a)(c,(function(){var t=this,e=t._self._c;t._self._setupProxy;return e("div",{staticClass:"py-3 pt-lg-3 cor-tertiary w-100"},[e("b-container",[e("b-alert",{attrs:{show:t.dismissCountDown,dismissible:"",variant:t.alertVariant},on:{dismissed:function(e){t.dismissCountDown=0},"dismiss-count-down":t.countDownChanged}},[e("p",[t._v(t._s(t.messageAlert))]),t._v(" "),e("b-progress",{attrs:{variant:"warning",max:t.dismissSecs,value:t.dismissCountDown,height:"4px"}})],1),t._v(" "),e("b-row",{staticClass:"g-5"},[e("b-col",{attrs:{sm:"12",md:"4"}},[e("b-card",{staticClass:"shadow-sm mb-4",attrs:{"img-alt":"Mapa","img-top":"","no-body":"","img-src":"https://img.freepik.com/vetores-premium/ilustracao-do-mapa-da-cidade-para-o-aplicativo-de-navegacao_8276-371.jpg?w=400"}},[e("b-card-body",[t.showRelatorioViagem?e("div",[e("b-card-text",{staticClass:"card-text"},[t._v("Distância: "+t._s(t.relatorioViagem.distancia_km)+" Km")]),t._v(" "),e("b-card-text",{staticClass:"card-text"},[t._v("Principais vias da rota: "+t._s(t.relatorioViagem.vias_da_rota))]),t._v(" "),e("b-card-text",{staticClass:"card-text"},[t._v("Litros necessários: "+t._s(t.relatorioViagem.consumo_total_de_combustivel)+"\n                litros\n              ")])],1):e("b-card-text",{staticClass:"card-text"},[t._v("\n              Calcula a quantidade de combustível necessária para percorrer uma determinada distância\n              entre dois pontos, levando em consideração o consumo estimado do veículo.\n            ")])],1)],1)],1),t._v(" "),e("b-col",{attrs:{sm:"12",md:"8"}},[e("h4",{staticClass:"mb-3"},[t._v("Informe os dados da viagem")]),t._v(" "),e("b-form",{attrs:{novalidate:""},on:{submit:function(e){return e.preventDefault(),t.submeterForm.apply(null,arguments)},reset:t.resetarForm}},[e("b-row",[e("b-col",{attrs:{md:"12",lg:"4"}},[e("label",{attrs:{for:"origemLatitude"}},[t._v("Coordenadas da origem:")])]),t._v(" "),e("b-col",{attrs:{md:"6",lg:"4"}},[e("b-input-group",{staticClass:"mb-2",attrs:{size:"sm"}},[e("b-form-input",{attrs:{placeholder:"Latitude da Origem",type:"text",id:"origemLatitude",required:""},model:{value:t.dataForm.origemLatitude,callback:function(e){t.$set(t.dataForm,"origemLatitude",e)},expression:"dataForm.origemLatitude"}}),t._v(" "),e("b-form-invalid-feedback",{attrs:{id:"origemLatitude-feedback"}},[t._v("Insira a coordenada.")])],1)],1),t._v(" "),e("b-col",{attrs:{md:"6",lg:"4"}},[e("b-input-group",{staticClass:"mb-2",attrs:{size:"sm"}},[e("b-form-input",{attrs:{placeholder:"Longitude da Origem",type:"text",id:"origemLongitude",required:""},model:{value:t.dataForm.origemLongitude,callback:function(e){t.$set(t.dataForm,"origemLongitude",e)},expression:"dataForm.origemLongitude"}}),t._v(" "),e("b-form-invalid-feedback",{attrs:{id:"origemLongitude-feedback"}},[t._v("Insira a coordenada.")])],1)],1)],1),t._v(" "),e("b-row",{staticClass:"pt-3"},[e("b-col",{attrs:{md:"12",lg:"4"}},[e("label",{attrs:{for:"destinoLatitude"}},[t._v("Coordenadas do destino:")])]),t._v(" "),e("b-col",{attrs:{md:"6",lg:"4"}},[e("b-input-group",{staticClass:"mb-2",attrs:{size:"sm"}},[e("b-form-input",{attrs:{placeholder:"Latitude do destino",type:"text",id:"destinoLatitude",required:""},model:{value:t.dataForm.destinoLatitude,callback:function(e){t.$set(t.dataForm,"destinoLatitude",e)},expression:"dataForm.destinoLatitude"}}),t._v(" "),e("b-form-invalid-feedback",{attrs:{id:"destinoLatitude-feedback"}},[t._v("Insira a coordenada.")])],1)],1),t._v(" "),e("b-col",{attrs:{md:"6",lg:"4"}},[e("b-input-group",{staticClass:"mb-2",attrs:{size:"sm"}},[e("b-form-input",{attrs:{placeholder:"Longitude do Destino",type:"text",id:"destinoLongitude",required:""},model:{value:t.dataForm.destinoLongitude,callback:function(e){t.$set(t.dataForm,"destinoLongitude",e)},expression:"dataForm.destinoLongitude"}}),t._v(" "),e("b-form-invalid-feedback",{attrs:{id:"destinoLongitude-feedback"}},[t._v("Insira a coordenada.")])],1)],1)],1),t._v(" "),e("b-row",{staticClass:"pt-3"},[e("b-col",{attrs:{sm:"12",md:"6"}},[e("label",{attrs:{for:"km_litro"}},[t._v("Média de consumo do veículo:")]),t._v(" "),e("b-input-group",{staticClass:"mb-3",attrs:{size:"sm",append:"Km/litro"}},[e("b-form-input",{attrs:{type:"number",id:"mediaConsumoVeiculo",required:""},model:{value:t.dataForm.mediaConsumoVeiculo,callback:function(e){t.$set(t.dataForm,"mediaConsumoVeiculo",e)},expression:"dataForm.mediaConsumoVeiculo"}}),t._v(" "),e("b-form-invalid-feedback",{attrs:{id:"km_litro-feedback"}},[t._v("Insira a média de consumo.")])],1)],1),t._v(" "),e("b-col",{staticClass:"py-sm-2",attrs:{sm:"12",md:"4"}},[e("b-form-checkbox",{staticClass:"pt-3",attrs:{id:"idaEVolta"},model:{value:t.dataForm.idaEVolta,callback:function(e){t.$set(t.dataForm,"idaEVolta",e)},expression:"dataForm.idaEVolta"}},[t._v("Calcular ida e volta")])],1)],1),t._v(" "),e("b-row",{staticClass:"pt-5"},[e("div",{},[e("button",{staticClass:"btn btn-secondary mx-2 float-end",attrs:{type:"button"},on:{click:function(e){return t.resetarForm()}}},[t._v("\n                Limpar\n                "),e("b-icon",{staticClass:"ml-2",attrs:{icon:"trash",scale:"1"}})],1),t._v(" "),e("button",{staticClass:"btn btn-success float-end px-5",attrs:{type:"submit",id:"submitFormViagem"}},[t._v("\n                Enviar\n                "),e("b-icon",{staticClass:"ml-2",attrs:{icon:"check-lg",scale:"1"}})],1)])])],1)],1)],1)],1)],1)}),[],!1,null,"54c393bb",null);e.default=component.exports}}]);