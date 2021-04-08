<template>
  <div>

    <div class="p-4">
      <p class="font-bold">{{ lane.title }}</p>
    </div>

    <div>
      <Card
          v-for="card in cards"
          :key="card.id"
          :board="board"
          :lane="lane"
          :card="card"
          @delete="deleteCard">
      </Card>
    </div>

    <div v-if="lane.type === 'g'" class="p-4 rounded mb-4 text-gray-400 bg-white shadow focus-within:ring-2">
      <input
          class="w-full focus:outline-none"
          type="text"
          v-model="form.title"
          @keypress.enter="createCard(form.title)"
          placeholder="+ Add Card">
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
    board: Object,
    lane: Object,
  },
  components: {
    Card
  },
  data: function() {
    return {
      loading: false,
      cards: [],
      form: {
        title: '',
      }
    }
  },
  async created() {
    await this.loadCards()
  },
  methods: {
    async loadCards() {
      this.cards = await api.getCardsOfLane(this.lane.id)
    },
    async createCard(title) {
      if (title !== "") {
        this.cards.push(await api.createCard(1, this.board.id, this.lane.id, title))
        this.form.title = ''
      }
    },
    async deleteCard(cardId) {
      await api.deleteCard(cardId)
      this.cards = this.cards.filter(item => item.id !== cardId)
    },
  }
}
</script>

<style scoped>

</style>
