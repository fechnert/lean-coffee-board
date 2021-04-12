<template>
  <textarea
    class="w-full focus:outline-none bg-white resize-none"
    rows="1"
    spellcheck="false"
    :value="title"
    @input="$emit('update:title', $event.target.value)"
    @keypress="resize"
    @keypress.enter.prevent>
  </textarea>
</template>

<script>
export default {
  name: "Editable",
  props: [
    'title'
  ],
  methods: {
    async resize(event) {
      event.target.style.height = "auto";
      event.target.style.height = `${event.target.scrollHeight}px`;
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.$el.setAttribute("style", "height: " + `${this.$el.scrollHeight}px`)
    })
  },
  emits: [
    'update:title'
  ]
}
</script>

<style scoped>

</style>
