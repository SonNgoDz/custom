<template>
  <div class="flex h-screen w-screen">
    <div v-if="showSidebar" class="h-full border-r bg-surface-menu-bar">
      <AppSidebar />
    </div>
    <div class="flex-1 flex flex-col h-full overflow-auto bg-surface-white">
      <slot />
    </div>
  </div>
</template>
<script setup>
import AppSidebar from '@/components/Layouts/AppSidebar.vue'
import { ref } from 'vue'

const showSidebar = ref(false)
</script>
