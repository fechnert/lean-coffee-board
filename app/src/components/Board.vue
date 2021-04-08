<template>
  <div>
    <div class="pl-4">
      <h1 class="text-2xl font-bold">{{ board.title }}</h1>
    </div>

    <div class="grid grid-flow-col auto-cols-fr gap-8 mt-8">
      <Lane v-for="lane in lanes" :key="lane.id" :board="board" :lane="lane"></Lane>
    </div>
  </div>
</template>

<script>
import api from "../api";
import Lane from "./Lane";

export default {
  name: "Board",
  components: {
    Lane,
  },
  data: function() {
    return {
      loading: false,
      board: {title: ""},
      lanes: [],
    }
  },
  async created() {
    await this.loadBoard()
    await this.loadLanes()
  },
  methods: {
    async loadBoard() {
      this.board = await api.getBoard('6a5c92ce-8222-4ca8-919c-89bbe09a73bd')
      console.log(this.board)
    },
    async loadLanes() {
      this.lanes = await api.getLanesOfBoard(this.board.id)
      console.log(this.lanes)
    }
  }
}
</script>

<style scoped>

</style>
