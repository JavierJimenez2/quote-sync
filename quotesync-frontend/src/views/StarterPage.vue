<script setup lang="ts">
import { ref, shallowRef, onMounted } from 'vue';
import { DownloadIcon, RefreshDotIcon, UploadIcon } from 'vue-tabler-icons';


interface Quote {
  book: {
    author: {
      name: string;
    };
    title: string;
  };
  tags: {
    title: string;
  }[];
  body: string;
}
import axios from 'axios';

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

import Button from 'primevue/button';

import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

// Página y breadcrumbs
const page = ref({ title: 'Quotes Table' });
const breadcrumbs = shallowRef([
  { title: 'Home', disabled: false, href: '/' },
  { title: 'Quotes Table', disabled: true, href: '#' },
]);

// Datos de la tabla
const quotes = ref<Quote[]>([]);

// Cargar los datos de la API
const fetchQuotes = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/quote-detail/');
    quotes.value = response.data.map((quote: Quote) => ({
      author: quote.book.author.name,
      book: quote.book.title,
      tags: quote.tags.map((tag) => tag.title).join(', '),
      body: quote.body,
    }));
  } catch (error) {
    console.error('Error fetching quotes:', error);
  }
};

// Ejecutar al montar el componente
onMounted(() => {
  fetchQuotes();
});

// Método para descargar CSV

const downloadCSV = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/v1/quote-detail/');
    if (response.data.length === 0) {
      console.error('No quotes to download');
      return;
    }

    const csvRows = [];
    const headers = ['Author', 'Book', 'Tag', 'Quote']; // Cabecera del CSV
    csvRows.push(headers.join(',')); // Añadir cabecera

    interface CsvQuote {
      book: {
        author: {
          name: string;
        };
        title: string;
      };
      tags: {
        title: string;
      }[];
      body: string;
    }

    const fetchedQuotes: CsvQuote[] = response.data;

    fetchedQuotes.forEach((item: CsvQuote) => {
      const tags = item.tags.map(tag => tag.title).join(', ');
      const row = [
        `"${item.book.author.name}"`,
        `"${item.book.title}"`,
        `"${tags}"`,
        `"${item.body}"`,
      ];
      csvRows.push(row.join(','));
    });

    const csvString = csvRows.join('\n');
    const bom = '\ufeff';
    const blob = new Blob([bom, csvString], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'quotes.csv';
    link.click();
  } catch (error) {
    console.error('Error downloading CSV:', error);
  }
};



// Método para importar archivo TXT
const snackbarMessage = ref('');
const snackbar = ref(false);
const snackbarColor = ref('success');

const addTXTFile = (event: Event) => {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (file) {
    const formData = new FormData();
    formData.append('file', file);

    axios.post('http://localhost:8000/api/v1/upload/', formData)
      .then(() => {
        console.log('File uploaded successfully!');
        snackbarMessage.value = "File uploaded successfully!";
        snackbar.value = true;
        fetchQuotes();
        // this.$router.go();
        // this.$router.push('/');
      })
      .catch(() => {
        snackbarMessage.value = "Error uploading file";
        snackbarColor.value = 'error';
        snackbar.value = true;
      });
  }
};




</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs" />

  <v-row>
    <v-col cols="12" md="12">
      <UiParentCard title="Quotes Table">
        
      </UiParentCard>
      <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="3000">
        {{ snackbarMessage }}
      </v-snackbar>
    </v-col>
  </v-row>
</template>
