<template>
  <main class="form-signin">
    <form @submit.prevent="validateVIN">
      <h1 class="h1 mb-3 fw-normal">VIN decoder</h1>
      <label for="inputVIN" class="visually-hidden">VIN</label>
      <input v-model="inputVIN"
             @keyup="validateVIN"
             type="text"
             id="inputVIN"
             class="form-control"
             placeholder="VIN"
             required autofocus>
      <br>
      <p v-if="isValid">{{ inputVIN }} is valid</p>
      <p v-else>{{ inputVIN }} is invalid</p>
      <button class='btn btn-primary'>Submit</button>
    </form>
  </main>
</template>

<script>
import http from '../http';

export default {
  name: 'VINDecoder',
  props: {
  },
  data() {
    return {
      inputVIN: null,
      isValid: false,
      count: 0
    }
  },
  methods: {
    validateVIN() {
      if(this.inputVIN.length !== 17 ) {
        this.isValid = false;
        return
      }
      let calculatedCheckDigit = this.calculateCheckDigit(this.inputVIN);
      if (calculatedCheckDigit == this.inputVIN[8]) {
        this.isValid = true;
      } else {
        this.isValid = false;
      }
    },
    decodeValueOf(char) {
      //Transliteration key: values for VIN decoding
      return '0123456789.ABCDEFGH..JKLMN.P.R..STUVWXYZ'.indexOf(char) % 10;
    },
    getWeightOf(index) {
      // weights assigned for each 17 digits
      let weights = '8765432X098765432';
      // every weight stands for it's own value
      // except x represents 10
      let values = '0123456789X';
      return values.indexOf(weights[index]);
    },
    calculateCheckDigit(vin) {
      // Ref - https://en.wikipedia.org/wiki/Vehicle_identification_number#Check-digit_calculation
      let total = 0;
      for (let i = 0; i < 17; ++i) {
        total += this.decodeValueOf(vin[i]) * this.getWeightOf(i);
      }
      let result = total % 11;
      return result === 10 ? X : result;
    }
  }
}
</script>
