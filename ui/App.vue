<template>
  <main class="form-signin">
    <router-link :to="{ name: 'vin-decoder' }">Decoder</router-link> |
    <router-link :to="{ name: 'lookup-history' }">History</router-link>

    <router-view/>
  </main>
</template>
