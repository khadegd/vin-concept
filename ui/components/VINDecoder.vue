<template>
  <main class="form-signin">
    <form>
      <h1 class="h1 mb-3 fw-normal">VIN decoder</h1>
      <label for="inputVIN" class="visually-hidden">VIN</label>
      <input v-model="inputVIN"
             @change="validateVIN"
             type="text"
             id="inputVIN"
             class="form-control"
             placeholder="VIN"
             required autofocus>
      <br>
      <p>{{ inputVIN }}</p>
    </form>
  </main>
</template>

<script>
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
    // logic to validate vin
    }
  }
}
</script>
