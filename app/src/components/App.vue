<template>
  <div class="flex flex-row">

    <!-- navigation -->
    <div class="h-screen w-20 flex flex-col justify-between">

        <div class="flex flex-col">

          <div class="my-4">
            <img class="object-contain max-w-full" src="../assets/logo.png" alt="Logo">
          </div>

          <div class="flex justify-center mt-4">
            <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/">
              <HomeIcon class="h-8 w-8"></HomeIcon>
            </router-link>
          </div>
          <div class="flex justify-center mt-4">
            <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/boards">
              <ViewGridIcon class="h-8 w-8"></ViewGridIcon>
            </router-link>
          </div>
          <div class="flex justify-center mt-4">
            <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/boards/create">
              <PlusCircleIcon class="h-8 w-8"></PlusCircleIcon>
            </router-link>
          </div>
        </div>

        <div class="flex flex-col mb-4">
          <div class="flex justify-center mt-4">
            <a class="p-1 text-gray-100 rounded hover:bg-gray-600" href="https://github.com/fechnert/lean-coffee-board" target="_blank">
              <CodeIcon class="h-8 w-8"></CodeIcon>
            </a>
          </div>
          <div class="flex justify-center mt-4">
            <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/imprint">
              <InformationCircleIcon class="h-8 w-8"></InformationCircleIcon>
            </router-link>
          </div>
        </div>

    </div>

    <!-- app content -->
    <div class="w-full bg-gray-300 rounded-l-xl shadow">
      <div class="container mx-auto mt-8">
        <router-view class="mx-4"></router-view>
      </div>
    </div>


  </div>
</template>

<script>
import { HomeIcon, PlusCircleIcon, ViewGridIcon, CodeIcon, InformationCircleIcon } from '@heroicons/vue/outline'

export default {
  name: "App",
  components: {
    HomeIcon,
    PlusCircleIcon,
    ViewGridIcon,
    CodeIcon,
    InformationCircleIcon,
  },
  computed: {
    user() {
      return this.$store.state.user
    }
  }
}
</script>

<style scoped>

</style>
