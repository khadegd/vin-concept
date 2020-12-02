<template>
  <main class="form-signin">
    <div v-if="previouslyDecodedVIN == null" class="spinner-border m-5" role="status"></div>
    <table v-else class="table table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">VIN</th>
          <th scope="col">Updated</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="vehical, name, index in previouslyDecodedVIN">
          <th>{{ index }}</th>
          <td class="align-right">{{ vehical.vin }}</td>
          <td class="align-left">{{ vehical.updated_at }}</td>
        </tr>
      </tbody>
    </table>
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
