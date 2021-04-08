<template>

  <div class="shadow mb-4">
    <div class="rounded-t bg-gray-500 px-4 py-2 flex justify-between">
      <p>By {{ card.owner }}</p>
      <XCircleIcon v-if="!deleteClicked" class="h-auto w-5 text-white cursor-pointer hover:text-red-300" @click="confirmDelete()"></XCircleIcon>
      <ExclamationCircleIcon v-if="deleteClicked" class="h-auto w-5 text-white cursor-pointer hover:text-red-300" @click="deleteCard(card.id)"></ExclamationCircleIcon>
    </div>
    <div class="rounded-b bg-white p-4">
    <p>{{ card.title }}</p>
  </div>
  </div>
</template>

<script>
import { XCircleIcon, ExclamationCircleIcon } from '@heroicons/vue/outline'

export default {
  name: "Card",
  props: {
    board: Object,
    lane: Object,
    card: Object
  },
  components: {
    XCircleIcon,
    ExclamationCircleIcon,
  },
  data: function() {
    return {
      deleteClicked: false,
    }
  },
  methods: {
    async confirmDelete() {
      this.deleteClicked = true
    },
    async deleteCard(cardId) {
      this.$emit('delete', cardId)
    }
  },
  emits: [
      'delete',
  ]
}
</script>

<style scoped>

</style>
