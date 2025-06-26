<template>
  <div>
    <h2>个人资料</h2>
    <p>用户名: {{ user.username }}</p>
    <p>邮箱: {{ user.email }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const user = ref({ username: '', email: '' })

onMounted(async () => {
  const token = localStorage.getItem('access')
  if (!token) return
  try {
    const res = await fetch('http://127.0.0.1:8000/api/users/me/', {
      headers: { 'Authorization': 'Bearer ' + token }
    })
    if (res.ok) {
      user.value = await res.json()
    } else {
      console.error('获取用户信息失败')
    }
  } catch (e) {
    console.error(e)
  }
})
</script>
