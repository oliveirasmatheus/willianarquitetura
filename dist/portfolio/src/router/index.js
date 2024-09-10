import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Projetos from '../components/Projetos.vue'
import Home from '../components/Home.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/projetos',
      name: 'projetos',
      component: Projetos
    }
  ]
})

export default router
