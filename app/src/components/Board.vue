<template>
  <div>
    <div v-if="loading">
      <p>Loading Board ...</p>
    </div>
    <div v-else>
      <div v-if="board !== null">
        <div class="rounded bg-white px-4 py-2 shadow">
          <h1 class="text-2xl font-bold">{{ board.title }}</h1>
          <div class="flex justify-between text-md text-gray-500">
            <p>Created by {{ board.owner.name }} at {{ $dayjs(board.created).format('YYYY-MM-DD') }}</p>
            <p>{{ members.length }} Members</p>
          </div>
        </div>

        <div class="grid grid-flow-col auto-cols-fr gap-8 mt-8">
          <Lane v-for="lane in lanes" :key="lane.id" :board="board" :lane="lane"></Lane>

          <!-- Board meta -->
          <div>
            <p>Phase: {{ currentPhase.name }}</p>
            <p>Members:</p>
            <p v-for="member in members" :key="member.id">- {{ member.name }}</p>
          </div>

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
  computed: {
    members() {
      return [this.board.owner, ...this.board.members]
    },
    currentPhase() {
      return this.board.phases.find(phase => phase.id === this.board.phase)
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
        this.lanes = response.data.results
      })
    }
  }
}
</script>

<style scoped>

</style>
