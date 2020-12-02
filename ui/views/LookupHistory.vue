<template>
  <main class="form-signin">
    <ul id="example-1">
      <li v-for="vehical in previouslyDecodedVIN">
        {{ vehical.vin }}
      </li>
    </ul>
  </main>
</template>

<script>
import {http} from "../http";

export default {
  name: 'LookupHistory',
  props: {
  },
  data() {
    return {
        previouslyDecodedVIN : null,
    }
  },
  methods: {
  },
  created() {
    http.get('history')
          .then(res => this.previouslyDecodedVIN = res.data)
  },
}
</script>
