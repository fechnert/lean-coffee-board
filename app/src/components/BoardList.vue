<template>
  <div>

    <div>
      <h1 class="text-lg font-bold">Owned Boards</h1>
      <p class="mb-4 text-gray-500">Last 5 Boards which were created by you</p>
      <div class="grid grid-cols-5 gap-4">
        <router-link
            class="rounded shadow hover:shadow-lg bg-white px-4 py-2 cursor-pointer block"
            v-for="board in ownedBoards"
            :key="board.id"
            :to="{name: 'boardDetail', params: {'id': board.id}}">
          <p class="text-xs text-gray-500 mb-1">Created {{ $dayjs(board.created).format('YYYY-MM-DD') }}</p>
          <p>{{ board.title }}</p>
        </router-link>
      </div>
    </div>

    <div class="mt-8">
      <h1 class="text-lg font-bold">Joined Boards</h1>
      <p class="mb-4 text-gray-500">Last 10 Boards where you are member of</p>
      <div class="grid grid-cols-5 gap-4">
        <router-link
            class="rounded shadow hover:shadow-lg bg-white px-4 py-2 cursor-pointer block"
            v-for="board in joinedBoards"
            :key="board.id"
            :to="{name: 'boardDetail', params: {'id': board.id}}">
          <p class="text-xs text-gray-500 mb-1">Created {{ $dayjs(board.created).format('YYYY-MM-DD') }}</p>
          <p>{{ board.title }}</p>
        </router-link>
      </div>
    </div>

  </div>
</template>

<script>
import api from "../api";

export default {
  name: "BoardList",
  data() {
    return {
      ownedBoards: [],
      joinedBoards: [],
    }
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  },
  created() {
    this.getBoards()
  },
  methods: {
    async getBoards() {
      await api.getBoardsByOwner(this.user.id).then((response) => {
        this.ownedBoards = response.data.results
      })
      await api.getBoardsByMember(this.user.id).then((response) => {
        this.joinedBoards = response.data.results
      })
    }
  }
}
</script>

<style scoped>

</style>
