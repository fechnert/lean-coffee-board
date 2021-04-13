<template>

  <div class="shadow mb-4 focus-within:ring-2 rounded">
    <div class="rounded-t bg-gray-500 px-4 py-2 flex justify-between cursor-move">
      <p>{{ card.owner.name }}</p>
      <XCircleIcon v-if="!deleteClicked" class="h-auto w-5 text-white cursor-pointer hover:text-red-300" @click="confirmDelete()"></XCircleIcon>
      <ExclamationCircleIcon v-if="deleteClicked" class="h-auto w-5 text-white cursor-pointer hover:text-red-300" @click="deleteCard(card.id)"></ExclamationCircleIcon>
    </div>
    <div class="rounded-b bg-white p-4">
      <Editable v-model:title="title" @keyup="updateCard(card.id, title)"></Editable>
    </div>
  </div>
</template>

<script>
import Editable from "./Editable";

import { XCircleIcon, ExclamationCircleIcon } from '@heroicons/vue/outline'

export default {
  name: "Card",
  props: {
    board: Object,
    lane: Object,
    card: Object
  },
  components: {
    Editable,
    XCircleIcon,
    ExclamationCircleIcon,
  },
  data() {
    return {
      deleteClicked: false,
      title: this.card.title,
    }
  },
  methods: {
    async confirmDelete() {
      this.deleteClicked = true
    },
    async deleteCard(cardId) {
      this.$emit('delete', cardId)
    },
    async updateCard(cardId, title) {
      this.$emit('update', cardId, title)
    }
  },
  emits: [
      'update',
      'delete',
  ]
}
</script>

<style scoped>

</style>
