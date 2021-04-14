import dayjs from 'dayjs';
import { createApp } from 'vue/dist/vue.esm-bundler';

import './index.css';

import router from "@/router";
import store from "@/store";

import App from './components/App';

const app = createApp(App)
app.config.globalProperties.$dayjs = dayjs

app.use(router)
app.use(store)
app.mount('#app')
