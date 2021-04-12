<template>
  <div>
    <h1 class="text-lg">Create a Board</h1>

    <!-- Board properties -->
    <div class="mt-4">
      <h2>Board settings</h2>
      <input type="text" v-model="title" placeholder="Board Title">
      <input type="number" v-model="thinkTimeLimit">
      <input type="number" v-model="discussTimeLimit">
    </div>

    <!-- Lanes -->
    <div class="mt-4">
      <h2>Lanes</h2>

      <!-- Buttons -->
      <div>
        <button class="bg-gray-500 hover:bg-gray-600 text-white font-bold rounded px-2 shadow mr-4" @click="createLane">+ Add Lane</button>
        <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold rounded px-2 shadow" @click="createBoard">Create Board</button>
      </div>

      <!-- Lanes -->
      <div class="pt-4">
        <draggable :list="lanes" item-key="id" handle=".handle">
          <template #item="{element}">
            <div class="bg-white rounded shadow mb-2 p-2 max-w-md focus-within:ring-2">
              <div class="flex items-center">
                <div class="handle cursor-move mr-4"><MenuIcon class="h-auto w-5"></MenuIcon></div>
                <div class="w-full"><input class="w-full focus:outline-none bg-white" type="text" v-model="element.title"></div>
                <div v-if="element.type === 'g'" class="cursor-pointer">
                  <XIcon class="h-auto hover:text-red-500 w-5" @click="removeLane(element.id)"></XIcon>
                </div>
              </div>
              <p v-if="element.type === 'd'" class="text-gray-500 text-xs">
                Special Lane. Cards will be moved into it after voting finished to discuss them
              </p>
            </div>
          </template>
        </draggable>
      </div>
    </div>

  </div>
</template>

<script>
import draggable from "vuedraggable";
import { MenuIcon, XIcon } from "@heroicons/vue/outline";
import api from "../api";

let id = 100;

export default {
  name: "BoardCreate",
  components: {
    draggable,
    MenuIcon,
    XIcon,
  },
  data: function() {
    return {
      owner: 1,
      title: '',
      thinkTimeLimit: 360,
      discussTimeLimit: 600,
      lanes: [
        {id: 1, type: 'g', title: "Hallo!"},
        {id: 2, type: 'g', title: "Ich"},
        {id: 3, type: 'g', title: "Du"},
        {id: 999, type: 'd', title: "Discuss"},
      ]
    }
  },
  methods: {
    async createLane() {
      id++
      let tmp = this.lanes.pop()
      this.lanes.push({id: id, type: 'g', title: `Lane ${id}`})
      this.lanes.push(tmp)
    },
    async removeLane(laneId) {
      this.lanes = this.lanes.filter(lane => lane.id !== laneId)
    },
    async createBoard() {
      await api.createBoard(this.owner, this.title, this.thinkTimeLimit, this.discussTimeLimit).then(response => {
        this.createLanes(response.data.id).then(() => {
          this.$router.push({name: 'boardDetail', params: {id: response.data.id}})
        })
      }).catch(error => {
        console.log(error)
      })
    },
    async createLanes(boardId) {
      await this.lanes.forEach((lane) => {
        api.createLaneForBoard(boardId, lane)
      })
    },
  }
}
</script>

<style scoped>

</style>
