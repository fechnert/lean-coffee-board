import { createApp } from 'vue/dist/vue.esm-bundler';
import { createRouter, createWebHistory } from 'vue-router';

import './index.css';

import App from "./App";
import Home from "./components/Home";
import CreateBoard from "./components/CreateBoard";
import Board from "./components/Board";

const routes = [
  { path: '/', component: Home },
  { path: '/create', component: CreateBoard },
  { path: '/board', component: Board },
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')

//createApp(App).mount('#app')
