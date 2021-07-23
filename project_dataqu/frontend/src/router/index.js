import Vue from 'vue'
import Router from 'vue-router'
import Maintainer from '@/components/main/Maintainer'
import Indicators from '@/components/main/Indicators'
import Charts from '@/components/main/Charts'
import Functions from '@/components/main/Functions'

Vue.use(Router)

const router = new Router({
    routes: [
        {
            path: '/maintainer',
            component: Maintainer,
            name: 'Mantenedor Datos'
        },
        {
            path: '/indicators',
            component: Indicators,
            name: 'Indocadores'
        },
        {
            path: '/charts',
            component: Charts,
            name: 'Graficos'
        },
        {
            path: '/functions',
            component: Functions,
            name: 'funciones'
        },
    ],
    mode: 'history'
})

export default router