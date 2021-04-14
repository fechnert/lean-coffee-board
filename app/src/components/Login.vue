<template>
  <div>
    <h1>Login</h1>

    <div class="flex">
      <input v-model="color" type="color">
      <input v-model="name" type="text" placeholder="Name">
    </div>

    <div class="mt-4">
      <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold rounded px-2 shadow" @click="login">Create User</button>
    </div>

  </div>
</template>

<script>
import api from "../api";

export default {
  name: "Login",
  data() {
    return {
      name: '',
      color: '',
    }
  },
  methods: {
    async login() {
      await api.login(this.name, this.color).then((response) => {
        this.$store.commit('login', response.data)
        this.$router.push(this.$route.query.redirect || '/')
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
