<template>
  <div class="align-left">
    <pre>{{ JSON.stringify(vinDetails, null, '\t') }}</pre>
  </div>
</template>

<script>
import { http } from '../http'

export default {
  name: 'VINDetails',
  props: {
    vin: String
  },
  data() {
    return {
      vinDetails: null,
    }
  },
  created() {
    let url = 'details/'+this.vin
    http.get(url).then(res => this.vinDetails = res.data)
  },
}
</script>
