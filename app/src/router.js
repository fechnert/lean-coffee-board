import { createRouter, createWebHistory } from 'vue-router';

import store from "@/store";

import Login from "./components/Login";
import Home from "./components/Home";
import BoardList from "./components/BoardList";
import BoardCreate from "./components/BoardCreate";
import BoardJoin from "./components/BoardJoin";
import Board from "./components/Board";

const routes = [
  {path: '/', name: 'home', component: Home},
  {path: '/login/', name: 'login', component: Login},
  {path: '/boards/', name: 'boardList', component: BoardList, meta: {requireUser: true}},
  {path: '/boards/create/', name: 'boardCreate', component: BoardCreate, meta: {requireUser: true}},
  {path: '/boards/join/:id/', name: 'boardJoin', component: BoardJoin, meta: {requireUser: true}},
  {path: '/boards/:id/', name: 'boardDetail', component: Board, meta: {requireUser: true}},
]

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireUser)) {
    // todo: ask api if user really exists or else this would never change
    if (store.state.user == null) {
      next({name: 'login', query: {redirect: to.fullPath}})
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
