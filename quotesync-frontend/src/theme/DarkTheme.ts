import type { ThemeTypes } from '@/types/themeTypes/ThemeType';

const DarkTheme: ThemeTypes = {
  name: 'DarkTheme',
  dark: true,
  variables: {
    'border-color': '#4a4a4a', // Adjusted for dark background
    'carousel-control-size': 10,
  },
  colors: {
    primary: '#90caf9',        // Light blue for primary actions
    secondary: '#ce93d8',      // Soft purple
    info: '#4dd0e1',           // Vibrant cyan
    success: '#66bb6a',        // Bright green for success
    accent: '#ffcc80',         // Soft orange accent
    warning: '#ffb74d',        // Muted orange for warnings
    error: '#ef5350',          // Bright red for errors
    lightprimary: '#2e3a45',   // Background primary
    lightsecondary: '#3c2f41', // Background secondary
    lightsuccess: '#2e5232',   // Dark green tones for success
    lighterror: '#5a2a2a',     // Dark red tones for errors
    lightwarning: '#4f3827',   // Dark orange tones for warnings
    darkText: '#e0e0e0',       // Light text for readability
    lightText: '#bdbdbd',      // Muted light text
    darkprimary: '#1565c0',    // Same as before
    darksecondary: '#4527a0',  // Same as before
    borderLight: '#5a5a5a',    // Subtle borders
    inputBorder: '#757575',    // Grayish for input borders
    containerBg: '#121212',    // Dark background
    surface: '#1e1e1e',        // Slightly lighter than the background
    'on-surface-variant': '#333', // Slightly lighter for contrast
    facebook: '#4267b2',       // Same brand color
    twitter: '#1da1f2',        // Same brand color
    linkedin: '#0e76a8',       // Same brand color
    gray100: '#303030',        // Muted gray for dark themes
    primary200: '#64b5f6',     // Brighter blue
    secondary200: '#ab47bc',   // Vibrant purple
  },
};

export { DarkTheme };
