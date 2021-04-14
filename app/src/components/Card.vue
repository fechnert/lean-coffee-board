<template>

  <div class="shadow hover:shadow-lg mb-4 rounded-md focus-within:ring-2">
    <div class="rounded-t-md bg-white text-gray-500 pl-4 pr-2 py-1 flex justify-between border-l-4 border-gray-500" :style="{'border-color': card.owner.color}">
      <p>{{ card.owner.name }}</p>
      <div class="flex">
        <XIcon v-if="!deleteClicked" class="h-auto w-5 text-gray-300 cursor-pointer hover:text-yellow-500" @click="confirmDelete()"></XIcon>
        <TrashIcon v-if="deleteClicked" class="h-auto w-5 text-gray-300 cursor-pointer hover:text-red-500" @click="deleteCard(card.id)"></TrashIcon>
        <MenuIcon class="h-auto w-5 cursor-move handle"></MenuIcon>
      </div>
    </div>
    <div class="rounded-b-md bg-white px-4 py-2 border-l-4 border-gray-500" :style="{'border-color': card.owner.color}">
      <Editable v-model:title="title" @keyup="updateCard(card.id, title)"></Editable>
    </div>
  </div>
</template>

<script>
import Editable from "./Editable";

import { MenuIcon, XIcon, TrashIcon } from '@heroicons/vue/outline'

export default {
  name: "Card",
  props: {
    board: Object,
    lane: Object,
    card: Object
  },
  components: {
    Editable,
    MenuIcon,
    XIcon,
    TrashIcon,
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
      window.setTimeout(() => {this.deleteClicked = false}, 2000)
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
