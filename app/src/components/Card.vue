<template>
  <div class="bg-white p-4 rounded shadow mb-4">
    <p>{{ card.title }}</p>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    card: Object
  }
}
</script>

<style scoped>

</style>
