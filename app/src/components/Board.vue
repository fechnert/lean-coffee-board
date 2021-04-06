<template>
  <div class="container mx-auto mt-8">

    <div>
      <h1>Board view</h1>
    </div>

    <div class="grid grid-cols-3 gap-4 mt-8">
      <Lane v-for="lane in lanes" :key="lane.id" :lane="lane"></Lane>
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
      board: null,
      lanes: [],
    }
  },
  async created() {
    await this.loadBoard()
    await this.loadLanes()
  },
  methods: {
    async loadBoard() {
      this.board = await api.getBoard('3f025178-3777-4890-ab0a-ac0f4df3c36d')
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
