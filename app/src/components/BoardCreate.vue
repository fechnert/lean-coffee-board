<template>
  <div>
    <h1 class="text-lg">Create a Board</h1>

    <div class="mt-4">
      <h2>Board settings</h2>
      <input type="text" v-model="title" placeholder="Board Title">
      <input type="number" v-model="thinkTimeLimit">
      <input type="number" v-model="discussTimeLimit">
    </div>

    <div class="mt-4">
      <h2>Lanes</h2>
      <div class="py-4">
        <draggable :list="lanes" item-key="title" handle=".handle">
          <template #item="{element}">
            <div class="bg-white rounded shadow mt-2 p-2 max-w-md flex items-center">
              <div class="handle cursor-move mr-4"><MenuIcon class="h-auto w-5"></MenuIcon></div>
              <div><input type="text" v-model="element.title"></div>
            </div>
          </template>
        </draggable>
      </div>
    </div>

    <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold rounded px-2 shadow" type="submit" @click="createBoard">Create</button>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import { MenuIcon } from "@heroicons/vue/outline";
import api from "../api";

export default {
  name: "BoardCreate",
  components: {
    draggable,
    MenuIcon,
  },
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
