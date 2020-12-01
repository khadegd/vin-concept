import { createWebHistory, createRouter } from "vue-router";
import VINDecoder from "../views/VINDecoder.vue"
import VINDetails from "../views/VINDetails.vue"
import LookupHistory from "../views/LookupHistory.vue"

const routes = [
    {
      path: '/',
      name: "vin-decoder",
      component: VINDecoder,
    },
    {
      path: '/details/:vin',
      name: "vin-details",
      component: VINDetails,
      props: true
    },
    {
      path: '/history/',
      name: "lookup-history",
      component: LookupHistory,
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router
