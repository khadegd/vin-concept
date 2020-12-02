<template>
  <div class="align-left">
    <div v-if="vinDetails == null" class="spinner-border m-5" role="status"></div>
    <table v-else class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Key</th>
          <th scope="col">Value</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="value, name, index in vinDetails">
          <th>{{ index }}</th>
          <td class="align-right">{{ name }}</td>
          <td class="align-left">{{ value }}</td>
        </tr>
      </tbody>
    </table>
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
