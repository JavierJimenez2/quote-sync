import { fileURLToPath, URL } from 'url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import vuetify from 'vite-plugin-vuetify';
import dotenv from 'dotenv';


// https://vitejs.dev/config/
export default defineConfig({
  server: {
    port: Number(dotenv.config().parsed?.PORT) || 5173,
    host: true, // Esto permite conexiones externas (0.0.0.0)
  },  
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: (tag) => ['v-list-recognize-title'].includes(tag)
        }
      }
    }),
    vuetify({
      autoImport: true
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '@ag-grid-community/core': 'node_modules/@ag-grid-community/core',
      '@ag-grid-community/vue3': 'node_modules/@ag-grid-community/vue3',
    }
  },
  css: {
    preprocessorOptions: {
      scss: {}
    }
  },
  build: {
    chunkSizeWarningLimit: 1024 * 1024 // Set the limit to 1 MB
  },
  optimizeDeps: {
    exclude: ['vuetify'],
    entries: ['./src/**/*.vue']
  }
});

