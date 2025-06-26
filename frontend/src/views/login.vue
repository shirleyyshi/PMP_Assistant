<template>
  <div class="login">
    <h2>登录</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="用户名" />
      <input v-model="password" type="password" placeholder="密码" />
      <button type="submit">登录</button>
    </form>
    <p v-if="error" style="color:red">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()

// 登录页加载时清除 token，避免自动跳转
onMounted(() => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
})

const login = async () => {
  error.value = ''
  try {
    const res = await fetch('http://127.0.0.1:8000/api/users/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.value, password: password.value })
    })

    if (!res.ok) {
      throw new Error('登录失败')
    }

    const data = await res.json()
    localStorage.setItem('access', data.access)
    localStorage.setItem('refresh', data.refresh)

    // 显示登录成功提示
    alert('登录成功！')

    // 延迟1秒后跳转
    setTimeout(() => {
      router.push('/profile')
    }, 1000)
  } catch (err) {
    error.value = err.message
  }
}

</script>
