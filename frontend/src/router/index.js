import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ListFilm from '@/components/Film/ListFilm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/films',
      name: 'ListFilm',
      component: ListFilm
    }
  ],
  mode: 'history'
})
