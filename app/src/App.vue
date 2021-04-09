<template>
  <div class="flex flex-row">

    <!-- navigation -->
    <div class="h-screen w-20 bg-gray-500 shadow">
      <div class="my-4">
        <img class="object-contain max-w-full" src="./assets/logo.png" alt="Logo">
      </div>
      <div class="flex flex-col">
        <div class="flex justify-center mt-4">
          <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/">
            <HomeIcon class="h-8 w-8"></HomeIcon>
          </router-link>
        </div>
        <div class="flex justify-center mt-4">
          <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/board/create">
            <PlusCircleIcon class="h-8 w-8"></PlusCircleIcon>
          </router-link>
        </div>
<!--        <div class="flex justify-center mt-4">-->
<!--          <router-link class="p-1 text-gray-100 rounded hover:bg-gray-600" to="/board">-->
<!--            <ViewGridIcon class="h-8 w-8"></ViewGridIcon>-->
<!--          </router-link>-->
<!--        </div>-->
      </div>
    </div>

    <!-- app content -->
    <div class="container mx-auto mt-8">
      <router-view class="mx-4"></router-view>
    </div>

  </div>
</template>

<script>
import { HomeIcon, PlusCircleIcon, /*ViewGridIcon*/ } from '@heroicons/vue/outline'

export default {
  name: "App",
  components: {
    HomeIcon,
    PlusCircleIcon,
    // ViewGridIcon,
  }
}
</script>

<style scoped>

</style>
