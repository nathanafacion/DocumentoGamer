import Vue from "vue";
import Router from "vue-router";
import Carteirinha from "../components/Carteirinha.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "carteirinha",
      component: Carteirinha
    }
  ]
});