import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Home'
import Dashboard from '@/pages/Dashboard'
import Buses from '@/components/Buses/index'
import Trayectos from '@/components/Trayectos/index'
import Pasajeros from '@/components/Pasajeros/index'
import Choferes from '@/components/Choferes/index'
import About from '@/pages/About'
import error404 from '@/pages/404'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: { name: 'Home' }
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/Dashboard',
      name: 'Dashboard',
      component: Dashboard,
      children: [
        {
          // /Dashboard/Buses
          path: 'Trayectos/Buses/:id',
          name: 'Buses',
          component: Buses
        },
        {
          path: 'Trayectos',
          name: 'Trayectos',
          component: Trayectos
        },
        {
          path: 'Pasajeros',
          name: 'Pasajeros',
          component: Pasajeros
        },
        {
          path: 'Choferes',
          name: 'Choferes',
          component: Choferes
        }
      ]
    },
    {
      path: '/About',
      name: 'About',
      component: About
    },
    {
      path: '*',
      name: 'error404',
      component: error404
    }
  ]
})
