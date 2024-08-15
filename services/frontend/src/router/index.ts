import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DocView from '../views/DocView.vue'
import GenerateCvPdf from  '../views/GenerateCvPdf.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/doc',
      name: 'doc',
      component: DocView
    },
    {
      path: '/pdf',
      name: 'generatepdf',
      component: GenerateCvPdf
    },
   
    
  ]
})

export default router
