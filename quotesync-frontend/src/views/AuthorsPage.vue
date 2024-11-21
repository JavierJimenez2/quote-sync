<script setup lang="ts">
import { ref, shallowRef, onMounted } from 'vue';
import axios from 'axios';
import "gridjs/dist/theme/mermaid.css"; // Importar el tema de Grid.js

import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import CardsData from '@/components/shared/CardsData.vue';

const page = ref({ title: 'Authors' });
const breadcrumbs = shallowRef([
  { title: 'Others', disabled: false, href: '#' },
  { title: 'Sample Page', disabled: true, href: '#' }
]);

interface AuthorData {
  id: number;
  author: string;
  books: string;
}

const data = ref<AuthorData[]>([]);

const fetchAuthorData = () => {
  axios.get('http://localhost:8000/api/v1/author-books/')
    .then(response => {
      // Mapeamos los datos como en el ejemplo dado
      data.value = response.data.map((item: { id: number; author: string; books: string[] }) => ({
        id: item.id,
        author: item.author, // El nombre del autor
        books: item.books.join(", ") // Unimos los libros con una coma
      }));
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
      <UiParentCard title="Authors' Books">
        <v-container class="">
          <v-row no-gutters>
            <!-- Iterar sobre los elementos de los datos -->
            <v-col v-for="(item, index) in data" :key="index" cols="12" sm="4">
              <v-sheet class="ma-2 pa-2">
                <!-- Aquí agregamos el componente CardsData -->
                <CardsData :id="item.id" :author="item.author" :subtitle="item.books" :books="item.books"
                  description="" />
              </v-sheet>
            </v-col>
          </v-row>
        </v-container>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
