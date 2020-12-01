<template>
  <main class="form-signin">
      {{ vin }}
  </main>
</template>

<script>
export default {
  name: 'VINDetails',
  props: {
    vin: String
  },
  data() {
    return {
    }
  },
  methods: {
  }
}
</script>
