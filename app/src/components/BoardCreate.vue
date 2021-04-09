<template>
  <div>
    <h1>Create a Board</h1>
    <input type="text" v-model="title" placeholder="Board Title">
    <input type="number" v-model="thinkTimeLimit">
    <input type="number" v-model="discussTimeLimit">
    <button type="submit" @click="createBoard">Create</button>
  </div>
</template>

<script>
import api from "../api";

export default {
  name: "BoardCreate",
  data: function() {
    return {
      owner: 1,
      title: '',
      thinkTimeLimit: 360,
      discussTimeLimit: 600,
    }
  },
  methods: {
    async createBoard() {
      await api.createBoard(this.owner, this.title, this.thinkTimeLimit, this.discussTimeLimit).then(response => {
        this.$router.push({name: 'boardDetail', params: {id: response.data.id}})
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
