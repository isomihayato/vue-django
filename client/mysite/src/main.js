import { createApp } from 'vue'
import ToDoList from './ToDoList.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import '../node_modules/vuetify/dist/vuetify-labs.css'
import axios from 'axios'

loadFonts()

axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true

const app = createApp(ToDoList)
app.config.globalProperties.$axios = axios
app.use(vuetify)
app.mount('#app')