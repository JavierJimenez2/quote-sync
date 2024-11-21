<template>
    <v-card class="mx-auto" max-width="344" @click="goToAuthor">

        <!-- routelink -->
            
        <v-img height="200px" src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg" cover rounded></v-img>

        <v-card-title>
            {{ author }}
        </v-card-title>

        <v-card-subtitle>
            {{ subtitle }}
        </v-card-subtitle>
        <v-card-text>
            {{ description }}
        </v-card-text>

        <!-- <v-divider></v-divider>
        <v-card-actions>
            <v-btn color="orange-lighten-2" text="Explore"></v-btn>

            <v-spacer></v-spacer>

            <v-btn :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'" @click="show = !show"></v-btn>
        </v-card-actions> -->
        <!-- <v-col align-self="end">
            <v-sheet class="pa-2 ma-2">
                <v-btn color="orange-lighten-2" text="Read More"></v-btn>
            </v-sheet>
        </v-col> -->


    </v-card>
</template>

<script>
// go to author page
export default {
    props: {
        id: {
            type: Number,
            required: true,
        },
        author: {
            type: String,
            required: true,
        },
        subtitle: {
            type: String,
            required: true,
        },
        description: {
            type: String,
            required: true,
        },
        // imageSrc: {
        //     type: String,
        //     required: true,
        // },
        // imageHeight: {
        //     type: String,
        //     default: '200px',
        // },
    },
    methods: {
        goToAuthor() {
            // const encodedAuthor = encodeURIComponent(this.author); // Codificar el nombre del autor
            //string to integer
            // const encodedAuthor = parseInt(this.id);
            this.$router.push(`/authors/${this.id}`);
        },
    },
};



</script>