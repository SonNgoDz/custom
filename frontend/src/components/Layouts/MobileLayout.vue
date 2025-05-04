<template>
  <div class="flex h-screen w-screen">
    <MobileSidebar v-if="showSidebar" />
    <div class="flex h-full flex-1 flex-col overflow-auto bg-surface-white">
      <MobileAppHeader />
      <slot />
    </div>
  </div>
</template>
<script setup>
import MobileSidebar from '@/components/Mobile/MobileSidebar.vue'
import MobileAppHeader from '@/components/Mobile/MobileAppHeader.vue'
import { ref } from 'vue'

const showSidebar = ref(false)
</script>
