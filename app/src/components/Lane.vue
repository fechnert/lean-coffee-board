<template>
  <div>

    <div>
      <p>Lane "{{ lane.title }}"</p>
    </div>

    <div>
      <Card v-for="card in cards" :key="card.id" :title="card.title"></Card>
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
