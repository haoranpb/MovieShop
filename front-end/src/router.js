import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Cart from './views/Cart.vue'
import Action from './views/Action.vue'
import Pay from './views/Pay.vue'
import War from './views/War.vue'
import Fiction from './views/Fiction.vue'
import Documentary from './views/Documentary.vue'
import Disaster from './views/Disaster.vue'
import Comedy from './views/Comedy.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/action',
      name: 'action',
      component: Action
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    },
    {
      path: '/pay',
      name: 'pay',
      component: Pay
    },
    {
      path: '/war',
      name: 'war',
      component: War
    },
    {
      path: '/fiction',
      name: 'fiction',
      component: Fiction
    },
    {
      path: '/documentary',
      name: 'documentary',
      component: Documentary
    },
    {
      path: '/disaster',
      name: 'disaster',
      component: Disaster
    },
    {
      path: '/comedy',
      name: 'comedy',
      component: Comedy
    }
  ]
})
