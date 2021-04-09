<template>
  <div>

    <div class="p-4">
      <p class="font-bold">{{ lane.title }}</p>
    </div>

    <div v-if="loading" class="px-4 pb-4">
      <p class="text-gray-400"><i>Loading cards ...</i></p>
    </div>
    <div v-else>
      <div>
        <Card
            v-for="card in cards"
            :key="card.id"
            :board="board"
            :lane="lane"
            :card="card"
            @delete="deleteCard"
            @update="updateCard">
        </Card>
      </div>
    </div>

    <div v-if="lane.type === 'g'" class="p-4 rounded mb-4 text-gray-400 bg-white shadow focus-within:ring-2">
      <input
          class="w-full focus:outline-none bg-white"
          type="text"
          v-model="form.title"
          @keypress.enter="createCard(form.title)"
          placeholder="+ Add Card">
    </div>

    <div v-if="lane.type === 'd'" class="px-4">
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
      loading: true,
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
      await api.getCardsOfLane(this.lane.id).then(response => {
        this.cards = response.data
      }).catch(error => {
        console.log(error)
      }).finally(() => {
        this.loading = false;
      })
    },
    async createCard(title) {
      if (title !== "") {
        await api.createCard(1, this.board.id, this.lane.id, title).then(response => {
          this.cards.push(response.data)
          this.form.title = ''
        }).catch(error => {
          console.log(error)
        })
      }
    },
    async updateCard(cardId, title) {
      await api.updateCard(cardId, title).then(response => {
        let index = this.cards.findIndex((card => card.id === cardId))
        this.cards[index] = response.data

        // this.cards.forEach(card => {
        //   if (card.id === cardId) {
        //     card = response.data
        //   }
        // })
      })
    },
    async deleteCard(cardId) {
      await api.deleteCard(cardId).then(() => {
        this.cards = this.cards.filter(item => item.id !== cardId)
      }).catch(error => {
        console.log(error)
      })
    },
  }
}
</script>

<style scoped>

</style>
