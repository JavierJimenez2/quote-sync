import { createVuetify } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg';
import { icons } from './mdi-icon'; // Import icons from separate file
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import { DarkTheme } from '@/theme/DarkTheme';
import { LightTheme } from '@/theme/LightTheme';
import { ref } from 'vue';



export const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi',
    aliases: {
      ...aliases,
      ...icons
    },
    sets: {
      mdi
    }
  },
  theme: {
    defaultTheme: 'DarkTheme',
    themes: {
      DarkTheme,
      LightTheme,
    }
  },
  defaults: {
    VBtn: {},
    VCard: {
      rounded: 'md'
    },
    VTextField: {
      rounded: 'lg'
    },
    VTooltip: {
      // set v-tooltip default location to top
      location: 'top'
    }
  }
});


// You can set a reactive `isDark` state like this:
export const isDark = ref(true); // Default to dark mode


// Function to toggle between themes
export const toggleTheme = () => {
  isDark.value = !isDark.value;
  vuetify.theme.global.name.value = isDark.value ? 'DarkTheme' : 'LightTheme';
  // document.documentElement.classList.toggle('my-app-dark');
  // tiene que cambiar a dark o light dependiendo del valor de isDark
  if (isDark.value) {
    document.documentElement.classList.add('my-app-dark');
  } else {
    document.documentElement.classList.remove('my-app-dark');
  }
  // Optionally, store the user's preference in localStorage
  localStorage.setItem('theme', isDark.value ? 'DarkTheme' : 'LightTheme');
};

// On page load, check localStorage and set the theme accordingly
if (localStorage.getItem('theme') === 'LightTheme') {
  isDark.value = false;
  vuetify.theme.global.name.value = 'LightTheme';
} else {
  isDark.value = true;
  vuetify.theme.global.name.value = 'DarkTheme';
}

