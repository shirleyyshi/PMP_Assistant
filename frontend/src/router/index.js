import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Profile from '../views/Profile.vue'

const routes = [
    { path: '/login', component: Login },
    { path: '/profile', component: Profile },
    { path: '/', redirect: '/login' },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

// 路由守卫：保护 profile 路由，未登录跳转 login
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('access')

    if (to.path === '/profile' && !token) {
        // 访问个人资料页面，但没 token，跳登录
        next('/login')
    } else {
        // 访问登录页或其他页面，允许
        next()
    }
})

export default router
