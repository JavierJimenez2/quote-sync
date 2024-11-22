<script setup lang="ts">
import { ref, onMounted, shallowRef } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import "gridjs/dist/theme/mermaid.css"; // Importar el tema de Grid.js

import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

const page = ref({ title: 'Author' });


const author = ref('');
const books = ref([]);
interface Quote {
  quote: string;
  book: string;
}

const quotes = ref<Quote[]>([]);
const data = ref({});

const breadcrumbs = shallowRef([
  { title: 'Authors', disabled: false, href: '#' },
  { title: "Author", disabled: true, href: '#' }
]);
const route = useRoute();
const authorName = ref(route.params.authorName);  // Obtén el nombre del autor desde la ruta


// Función para cargar los libros y citas del autor
const fetchAuthorDetails = async () => {
  try {
    // hacer encode del nombre del autor para evitar problemas con caracteres especiales
    // const encodedAuthorName = encodeURIComponent(authorName.value as string);
    const response = await axios.get(`http://localhost:8000/api/v1/authors/${authorName.value}/`);
    data.value = response.data;
    author.value = response.data.author;
    books.value = response.data.books;
    quotes.value = response.data.quotes;
    console.log("Author details:", data);
  } catch (error) {
    console.error("Error fetching author details:", error);
  }
};

onMounted(() => {
  fetchAuthorDetails();
});
</script>


<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>

  <v-row>
    <v-col cols="12" md="12">
      <UiParentCard :title="author">
        <v-container>
          <v-row>
            <!-- Author Information Card -->
            <v-col cols="12" sm="12">
              <!-- <v-card-title>
                  <h1>{{ author }}</h1>
                </v-card-title> -->

              <v-card-title class="mt-2">
                <h3>Books by {{ author }}</h3>
              </v-card-title>

              <!-- List of Books -->
              <v-list>
                <v-list-item-group v-if="books.length">
                  <v-list-item v-for="(book, index) in books" :key="index">
                    <v-list-item-content>
                      <v-list-item-title>{{ book }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
                <v-alert v-else type="info">No books available for this author.</v-alert>
              </v-list>

              <v-divider class="my-4"></v-divider>

              <v-card-title class="mt-2">
                <h3>Quotes from {{ author }}</h3>
              </v-card-title>

              <!-- Cards for Quotes - 3 per row -->
              <v-row>
                <v-col v-for="(quote) in quotes" :key="quote.quote" cols="12" sm="4">
                  <v-card class="ma-2 pa-3" outlined>
                    <v-card-text>
                      <p>{{ quote.quote }}</p>
                      <!-- poner texto a la derecha -->
                    </v-card-text>
                    <p class="text-right font-weight-thin text-medium-emphasis" >- {{ quote.book }}</p>
                  </v-card>
                </v-col>
              </v-row>

              <v-alert v-if="quotes.length === 0" type="info">No quotes available for this author.</v-alert>
            </v-col>
          </v-row>
        </v-container>
      </UiParentCard>
    </v-col>
  </v-row>
</template>
