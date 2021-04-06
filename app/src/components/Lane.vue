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
import Card from "./Card";

export default {
  name: "Lane",
  props: {
    lane: Object
  },
  components: {
    Card
  },
  data: function() {
    return {
      cards: [
        {title: "Ich bin eine Card", id:"5"},
        {title: "Hier kann auch was stehen", id:"9"},
      ]
    }
  }
}
</script>

<style scoped>

</style>
