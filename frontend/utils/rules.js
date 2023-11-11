export default {
  ruleLatitude: function (value) {
    let state = true
    let message = ""
    let latitudeFloat = parseFloat(value.replace(",", '.'))
    if (isNaN(latitudeFloat)) {
      state = false
      message = 'Insira uma coordenada numérica.'
    }
    if (latitudeFloat < -90) {
      state = false
      message = 'A latitude não pode ser menor do que -90'
    }
    if (latitudeFloat > 90) {
      state = false
      message = 'A latitude não pode ser maior do que 90'
    }
    let valueClear = state ? latitudeFloat: null
    return {state, message, valueClear}
  },
  ruleLongitude: function (value) {
    let state = true
    let message = ""
    const longitudeFloat = parseFloat(value.replace(",", '.'))
    if (isNaN(longitudeFloat)) {
      state = false
      message = 'Insira uma coordenada numérica.'
    }
    if (longitudeFloat < -180) {
      state = false
      message = 'A longitude não pode ser menor do que -180'
    }
    if (longitudeFloat > 180) {
      state = false
      message = 'A longitude não pode ser maior do que 180'
    }
    let valueClear = state ? longitudeFloat: null
    return {state, message, valueClear}
  },
  ruleIsNumberPositive: function (value) {
    let state = true
    let message = ""
    const numFloat = parseFloat(value.replace(",", '.'))
    if (isNaN(numFloat)) {
      state = false
      message = 'Insira um valor numérico.'
    }
    if (numFloat <= 0) {
      state = false
      message = 'Insira um valor maior que zero.'
    }
    let valueClear = state ? numFloat: null
    return {state, message, valueClear}
  }
}
