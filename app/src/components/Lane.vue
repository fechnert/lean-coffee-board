<template>
  <div>

    <div class="p-4">
      <p class="font-bold">{{ lane.title }}</p>
    </div>

    <div>
      <Card v-for="card in cards" :key="card.id" :card="card"></Card>
    </div>

    <div v-if="lane.type === 'g'" class="p-4 rounded mb-4 text-gray-400 hover:bg-white hover:text-blue-600 hover:shadow">
      <a>+ Add Card</a>
    </div>

    <div v-if="lane.type === 'd'" class="p-4">
      <p class="text-gray-400">
        <i>Cards will be moved into this lane automatically after the voting phase has finished</i>
      </p>
    </div>

  </div>
</template>

<script>
import api from "../api";
import Card from "./Card";

export default {
  name: "Lane",
  props: {
    lane: Object,
  },
  components: {
    Card
  },
  data: function() {
    return {
      loading: false,
      cards: [],
    }
  },
  async created() {
    await this.loadCards()
  },
  methods: {
    async loadCards() {
      this.cards = await api.getCardsOfLane(this.lane.id)
    }
  }
}
</script>

<style scoped>

</style>
