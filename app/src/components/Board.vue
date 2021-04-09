<template>
  <div>
    <div v-if="loading">
      <p>Loading Board ...</p>
    </div>
    <div v-else>
      <div v-if="board !== null">
        <div class="pl-4">
          <h1 class="text-2xl font-bold">{{ board.title }}</h1>
        </div>

        <div class="grid grid-flow-col auto-cols-fr gap-8 mt-8">
          <Lane v-for="lane in lanes" :key="lane.id" :board="board" :lane="lane"></Lane>
        </div>
      </div>
      <div v-else>
        <p>No such board!</p>
      </div>
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
      loading: true,
      board: null,
      lanes: [],
    }
  },
  async created() {
    await this.loadBoard()
    if (this.board !== null) {
      await this.loadLanes()
    }
  },
  methods: {
    async loadBoard() {
      await api.getBoard(this.$route.params.id).then(response => {
        this.board = response.data
      }).catch(error => {
        if (error.response.status !== 404) {
          console.log(error)
        }
      }).finally(() => {
        this.loading = false
      })
    },
    async loadLanes() {
      await api.getLanesOfBoard(this.board.id).then(response => {
        this.lanes = response.data
      })
    }
  }
}
</script>

<style scoped>

</style>
