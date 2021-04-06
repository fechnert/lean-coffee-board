<template>
  <div>
    <p>This is a Card with title "{{ title }}"</p>
  </div>
</template>

<script>
export default {
  name: "Card",
  props: {
    title: String
  }
}
</script>

<style scoped>

</style>
