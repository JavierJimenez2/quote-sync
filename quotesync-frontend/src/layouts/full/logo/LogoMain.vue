<script setup>
import { isDark } from '@/plugins/vuetify';
import { useCustomizerStore } from '@/stores/customizer';

const customizerStore = useCustomizerStore();
// import { state } from '@/stores/customizer';

</script>
<template>
  <div v-if="isDark">
    <div v-if="customizerStore.mini_sidebar">
      <img src="@/assets/images/logos/LogoDarkSquare.png" alt="logo" class="logo w-100" />
    </div>
    <div v-else>
      <img src="@/assets/images/logos/logoDark.png" alt="logo" class="logo w-75" />
    </div>
  </div>
  <div v-else>
    <div v-if="customizerStore.mini_sidebar">
      <img src="@/assets/images/logos/LogoLightSquare.png" alt="logo" class="logo w-100" />
    </div>
    <div v-else>
      <img src="@/assets/images/logos/logo.png" alt="logo" class="logo w-75" />
    </div>
  </div>

</template>
