import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import '../src/assets/css/main/app.css'
// import '../src/assets/css/main/app-dark.css'
//import './assets/js/app.js'
//import './assets/js/pages/dashboard.js'
import 'bootstrap/dist/css/bootstrap.min.css'
// import "bootstrap"
// import "bootstrap"
// import "bootstrap/dist/js/bootstrap.min.js"
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
// import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'

// library.add(faUserSecret)
library.add(far,fas,fab);
import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).component('i', FontAwesomeIcon).use(store).use(router, axios).mount('#app')

import 'bootstrap/dist/js/bootstrap.js'

import "bootstrap/dist/css/bootstrap.min.css"
import "datatables.net-bs5"
import "datatables.net-bs5/css/dataTables.bootstrap5.min.css"
import "jszip"
import "pdfmake"
import "datatables.net-buttons-bs5"
import "datatables.net-buttons-bs5/css/buttons.bootstrap5.min.css"
import "datatables.net-buttons/js/buttons.colVis"
import "datatables.net-buttons/js/buttons.flash"
import "datatables.net-buttons/js/buttons.html5"
import "datatables.net-buttons/js/buttons.print"
