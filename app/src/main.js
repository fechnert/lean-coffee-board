import { createApp } from 'vue/dist/vue.esm-bundler';
import { createRouter, createWebHistory } from 'vue-router';

import './index.css';

import App from "./App";
import Home from "./components/Home";
import Board from "./components/Board";
import BoardCreate from "./components/BoardCreate";
import BoardJoin from "./components/BoardJoin";

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/board/create/', name: 'boardCreate', component: BoardCreate },
  { path: '/board/join/:id/', name: 'boardJoin', component: BoardJoin },
  { path: '/board/:id/', name: 'boardDetail', component: Board },
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
})

const app = createApp(App)
app.use(router)
app.mount('#app')
