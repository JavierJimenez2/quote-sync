<script setup lang="ts">
import { ref, shallowRef, onMounted } from 'vue';
import axios from 'axios';
import "gridjs/dist/theme/mermaid.css"; // Importar el tema de Grid.js

import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import CardsData from '@/components/shared/CardsData.vue';

const page = ref({ title: 'Books' });
const breadcrumbs = shallowRef([
  { title: 'Others', disabled: false, href: '#' },
  { title: 'Sample Page', disabled: true, href: '#' }
]);

interface BookData {
  title: string;
}

const data = ref<BookData[]>([]);

const fetchAuthorData = () => {
  axios.get('http://localhost:8000/api/v1/book/')
    .then(response => {
      // Mapeamos los datos correctamente
      data.value = response.data.map((item: { title: string }) => ({
        title: item.title,  // Solo asignamos el título del libro
      }));
    }).then(() => {
      console.log(data.value);
    })
    .catch(error => {
      console.error("Error fetching author data:", error);
    });
};

onMounted(() => {
  fetchAuthorData();
});
</script>
<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <v-col cols="12" md="12">
      <UiParentCard title="Books">
        <v-container>
          <v-row no-gutters>
            <!-- Iterar sobre los elementos de los datos -->
            <v-col v-for="(item, index) in data" :key="index" cols="12" sm="4">
              <v-sheet class="ma-2 pa-2">
                <!-- Aquí pasamos el título del libro como dato -->
                <CardsData :author="item.title" :subtitle="item.title" :books="[item.title]"
                  :description="'Description goes here'" />
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
