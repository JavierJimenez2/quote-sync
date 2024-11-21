<script setup lang="ts">
import { onMounted } from 'vue';
import { RefreshDotIcon } from 'vue-tabler-icons';
// importar icons primevue


interface Quote {
    id: number;
    author: string;
    book: {
        title: string;
        author: {
            name: string;
        };
    };
    tags: {
        title: string;
    }[];
    body: string;
}
import axios from 'axios';

import DataTable from 'primevue/datatable';
import type { DataTableFilterMetaData, DataTableOperatorFilterMetaData } from 'primevue/datatable';
import Column from 'primevue/column';

import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import Toolbar from 'primevue/toolbar';
// import FileUpload from 'primevue/fileupload';
import Dialog from 'primevue/dialog';
import Textarea from 'primevue/textarea';
import Tag from 'primevue/tag';

// import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';



// Página y breadcrumbs

// Datos de la tabla
const quotes = ref<Quote[]>([]);
const loading = ref(false);
const filters = ref<{ [key: string]: DataTableFilterMetaData | DataTableOperatorFilterMetaData }>({ global: { value: null, matchMode: 'contains' } });
const selectedProducts = ref<Quote[]>([]);
// const quote = ref<Quote | null>(null);

const submitted = ref(false);
const quoteDialog = ref(false);
const deleteQuoteDialog = ref(false);
const deleteQuotesDialog = ref(false);

import { ref } from 'vue';




// Cargar los datos de la API
const fetchQuotes = async () => {
    try {
        const response = await axios.get('http://localhost:8000/api/v1/quote-detail/');
        quotes.value = response.data.map((quote: Quote) => ({
            id: quote.id,
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





const snackbarMessage = ref('');
const snackbar = ref(false);
const snackbarColor = ref('success');

const addTXTFile = (event: Event) => {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    loading.value = true;

    if (file) {
        const formData = new FormData();
        formData.append('file', file);

        axios.post('http://localhost:8000/api/v1/upload/', formData)
            .then(() => {
                loading.value = false;
                console.log('File uploaded successfully!');
                fetchQuotes();
                snackbarMessage.value = "File uploaded successfully!";
                snackbarColor.value = 'success';
                snackbar.value = true;
                // router.go();

                // Reset the input to allow re-uploading the same file if necessary
                input.value = ''; // This is the key step
            })
            .catch((error) => {
                snackbarMessage.value = "Failed to upload file: " + error;
                snackbarColor.value = 'error';
                snackbar.value = true;
            });
    }
};




const quoteForm = ref({
    author: '',
    book: '',
    tags: '',
    body: ''
});

const openNew = () => {
    quoteForm.value = {
        author: '',
        book: '',
        tags: '',
        body: ''
    };
    submitted.value = false;
    quoteDialog.value = true;
};

const confirmDeleteSelected = () => {
    if (selectedProducts.value && selectedProducts.value.length === 1) {
        deleteQuoteDialog.value = true; // Muestra el diálogo de confirmación
    }
    else{
        deleteQuotesDialog.value = true;

    }
};

const deleteSelectedQuotes = async () => {
    if (!selectedProducts.value || !selectedProducts.value.length) return;

    try {
        // Extrae los IDs de las filas seleccionadas
        // const idsToDelete = 
        if (selectedProducts.value.length > 1) {
            const idsToDelete = selectedProducts.value.map((quote) => quote.id);
            console.log('Deleting quotes:', idsToDelete);
            await axios.post('http://localhost:8000/api/v1/quote-delete/bulk-delete/', { ids: idsToDelete });
        }
        else{
            const quoteToDelete = selectedProducts.value[0];
            console.log('Deleting quotes:', quoteToDelete);
            await axios.delete(`http://localhost:8000/api/v1/quote-delete/${quoteToDelete.id}/`);
        }

        // Realiza la solicitud DELETE al backend
        // await axios.post('http://localhost:8000/api/v1/quotes/bulk-delete/', { ids: idsToDelete });

        // Actualiza la tabla eliminando las filas localmente
        // quotes.value = quotes.value.filter((quote) => !idsToDelete.includes(quote.id));

        // Limpia la selección y cierra el diálogo
        selectedProducts.value = [];
        deleteQuoteDialog.value = false;
        deleteQuotesDialog.value = false;
        
        // Muestra un mensaje de éxito
        fetchQuotes();
        snackbarMessage.value = 'Quotes deleted successfully!';
        snackbarColor.value = 'success';
        snackbar.value = true;
    } catch (error) {
        console.error('Error deleting quotes:', error);
        snackbarMessage.value = 'Failed to delete quotes.';
        snackbarColor.value = 'error';
        snackbar.value = true;
    }
};





const hideQuoteDialog = () => {
    quoteDialog.value = false;
};

// const deleteSelectedQuotes = () => {
//     console.log('Selected quotes deleted');
//     // Add your logic to delete selected quotes here
// };



const saveQuote = async () => {
    submitted.value = true;

    // Validate required fields
    if (quoteForm.value.author && quoteForm.value.book && quoteForm.value.tags && quoteForm.value.body) {
        try {
            // Send the data to your backend API using axios
            // enviar tags como un array de strings
            const response = await axios.post('http://localhost:8000/api/v1/quotePost/', {
                author: quoteForm.value.author,
                book: quoteForm.value.book,
                tags: quoteForm.value.tags,
                body: quoteForm.value.body
            });


            console.log('Quote saved:', response.data);
            snackbarMessage.value = 'Quote saved successfully!';
            snackbarColor.value = 'success';
            snackbar.value = true;
            quoteDialog.value = false;
            // Optionally, clear the form after successful save
            quoteForm.value = { author: '', book: '', tags: '', body: '' };
            fetchQuotes();
        } catch (error) {
            snackbarMessage.value = 'Failed to save quote.'+error;
            snackbarColor.value = 'error';
            snackbar.value = true;
            
            console.error('Error saving quote:', error);
        }
    }
};

// Removed redundant computed function definition
</script>

<template>
    <v-row>
        <v-col cols="12" md="12">

            <UiParentCard title="List of quotes">

                <Toolbar class="mb-6">
                    <template #start>
                        <Button label="New" icon="pi pi-plus" class="mr-2" @click="openNew" />
                        <Button label="Delete" icon="pi pi-trash" severity="danger" outlined
                            @click="confirmDeleteSelected" :disabled="!selectedProducts || !selectedProducts.length" />
                    </template>

                    <template #end>
                        <!-- <FileUpload mode="basic" accept=".txt" :maxFileSize="1000000" label="Import" @change="addTXTFile"
                            chooseLabel="Import" class="mr-2" auto :chooseButtonProps="{ severity: 'secondary' }"  /> -->
                        
                        
                        <Button class="mr-2" label="Import from Kindle" icon="pi pi-download" severity="secondary"
                            @click="$refs.txtFileInput.click()" />

                        <Button class="mr-2" label="Export" icon="pi pi-upload" severity="secondary"
                            @click="downloadCSV" />
                        <IconField class="mr-2">
                            <InputIcon>
                                <i class="pi pi-search" />
                            </InputIcon>
                            <InputText v-model="(filters.global as DataTableFilterMetaData).value"
                                placeholder="Keyword Search" />
                        </IconField>
                    </template>
                </Toolbar>
                <DataTable v-model:filters="filters" v-model:selection="selectedProducts" filterDisplay="menu"
                    :loading="loading" :value="quotes" paginator showGridlines :rows="5"
                    :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem"
                    paginatorTemplate="RowsPerPageDropdown FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
                    currentPageReportTemplate="{first} to {last} of {totalRecords}" removableSort>
                    <!-- <template #header>
                        <div class="flex justify-end">

                        </div>
                    </template> -->
                    <template #empty> Not found. </template>
                    <template #loading> Loading customers data. Please wait. </template>
                    <template #paginatorstart>
                        <Button type="button" text @click="fetchQuotes">
                            <RefreshDotIcon />
                        </Button>
                    </template>

                    <template #paginatorend>
                        <input type="file" accept=".txt" @change="addTXTFile" style="display: none"
                            ref="txtFileInput" />
                            <Button class="mr-2" label="Import from Kindle" icon="pi pi-download" severity="secondary"
                            @click="$refs.txtFileInput.click()" />

                        <Button class="mr-2" label="Export" icon="pi pi-upload" severity="secondary"
                            @click="downloadCSV" />
                        <!-- <Button type="button" text @click="$refs.txtFileInput.click()">
                            <UploadIcon />
                        </Button>
                        <Button type="button" text @click="downloadCSV">
                            <DownloadIcon />
                        </Button> -->
                    </template>

                    <Column selectionMode="multiple" style="width: 3rem" :exportable="false" />
                    <Column field="author" header="Author" sortable style="width: 25%" />
                    <Column field="book" header="Book" sortable style="width: 25%" />
                    <Column field="tags" header="Tags" sortable style="width: 25%">
                        <template #body="{ data }">
                            <div v-if="data.tags!==''" class="">
                                <Tag v-for="(tag, index) in data.tags.split(',')" :key="index" :value="tag.trim()"
                                    class="mr-2" severity="success" />
                            </div>
                        </template>
                    </Column>
                    <Column field="body" header="Quote" sortable style="width: 25%" />
                </DataTable>


                <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="3000">
                    {{ snackbarMessage }}
                </v-snackbar>
            </UiParentCard>
        </v-col>
    </v-row>
    <!-- Quote Dialog -->
    <Dialog v-model:visible="quoteDialog" :style="{ width: '450px' }" header="Quote Details" :modal="true">
        <div class="flex flex-col gap-6">
            <div>
                <label for="author" class="block font-bold mb-3">Author</label>
                <InputText id="author" v-model.trim="quoteForm.author" fluid :invalid="submitted" />
            </div>
            <div>
                <label for="book" class="block font-bold mb-3">Book</label>
                <InputText id="book" v-model.trim="quoteForm.book" required fluid />
            </div>
            <div>
                <label for="tags" class="block font-bold mb-3">Tags</label>
                <InputText id="tags" v-model.trim="quoteForm.tags" required fluid />
            </div>
            <div>
                <label for="body" class="block font-bold mb-3">Quote</label>
                <Textarea id="body" v-model.trim="quoteForm.body" required rows="3" cols="20" fluid />
            </div>
        </div>

        <template #footer>
            <Button label="Cancel" icon="pi pi-times" text @click="hideQuoteDialog" />
            <Button label="Save" icon="pi pi-check" @click="saveQuote" />
        </template>
    </Dialog>


    <!-- Confirm Delete Dialog -->
    <Dialog v-model:visible="deleteQuoteDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
        <div class="flex items-center gap-4">
            <i class="pi pi-exclamation-triangle !text-3xl" />
            <span> Are you sure you want to delete the quote by <b>{{ selectedProducts[0].author }}</b>?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="deleteQuoteDialog = false" />
            <Button label="Yes" icon="pi pi-check" @click="deleteSelectedQuotes" />
        </template>
    </Dialog>

    <!-- Confirm Delete Selected Quotes -->
    <Dialog v-model:visible="deleteQuotesDialog" :style="{ width: '450px' }" header="Confirm" :modal="true">
        <div class="flex items-center gap-4">
            <i class="pi pi-exclamation-triangle !text-3xl" />
            <span> Are you sure you want to delete {{ selectedProducts.length }} quotes?</span>
        </div>
        <template #footer>
            <Button label="No" icon="pi pi-times" text @click="deleteQuotesDialog = false" />
            <Button label="Yes" icon="pi pi-check" text @click="deleteSelectedQuotes" />
        </template>
    </Dialog>

    <!-- Loading Modal -->
    <Dialog v-model:visible="loading"  header="Loading" :modal="true" :closable="false">
    <div class="flex justify-center items-center h-full w-full">
        <v-progress-circular
            indeterminate
            color="primary"
            :size="70"
            :width="8"
        >
            <!-- Loading... -->
        </v-progress-circular>
    </div>
</Dialog>


</template>
