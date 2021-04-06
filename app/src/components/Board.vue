<template>
  <div class="container mx-auto">

    <div>
      <h1>Board view</h1>
    </div>

    <div>
      <Lane v-for="lane in lanes" :key="lane.id" :lane="lane"></Lane>
    </div>

  </div>
</template>

<script>
import Lane from "./Lane";
import api from "../api";

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
    this.loadBoard()
    this.loadLanes()
  },
  methods: {
    async loadBoard() {
      this.board = await api.getBoard('2e86f49e-f5e2-4c2f-af58-21300f5290c7')
      console.log(this.board)
    },
    async loadLanes() {
      this.lanes = await api.getLanes()
      console.log(this.lanes)
    }
  }
}
</script>

<style scoped>

</style>
