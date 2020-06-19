import "bootstrap/dist/css/bootstrap.css";
import BootstrapVue from "bootstrap-vue";
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuelidate from 'vuelidate';
import UploadImage from 'vue-upload-image';


Vue.component('upload-image', UploadImage)
Vue.use(Vuelidate);
Vue.use(BootstrapVue);


Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
