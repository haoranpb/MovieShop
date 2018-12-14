import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Fiction from './views/Fiction.vue'
import Cart from './views/Cart.vue'

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
      path: '/fiction',
      name: 'fiction',
      component: Fiction
    },
    {
      path: '/cart',
      name: 'cart',
      component: Cart
    }
  ]
})
