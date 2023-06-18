import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Pic from '@/components/Pic'
import Index from '@/components/Index'

Vue.use(Router)

export default new Router({
  model:'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path:'/pic',
      name:'Pic',
      component:Pic
    },
    {
      path:'/index',
      name:'index',
      component:Index
    }
  ]
})
