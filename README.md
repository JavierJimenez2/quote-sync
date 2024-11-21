# QuoteSync

QuoteApp is a full-stack application for managing authors, books, and their respective quotes. The project is divided into two main parts:

- **Frontend**: Built using Vue.js with Vuetify and other libraries for smooth UI/UX.
- **Backend**: A RESTful API built with Django that serves author details, books, and quotes data.

## Project Structure

The project consists of two main directories:

1. **`quotesync-backend`**: The backend application built with Django.
2. **`quotesync-frontend`**: The frontend application built with Vue.js.

## Features

- **Authors**: View information about authors, their books, and quotes.
- **Books**: Display books by specific authors.
- **Quotes**: List and display quotes by authors, with dynamic rendering for a smooth experience.
- **UI/UX**: Utilizes Vuetify for the UI, with components like cards, breadcrumbs, and more for a clean and responsive interface.
- **Responsive Layout**: The frontend is optimized to display data in a structured way, with a 3-column layout for quotes, and intelligent redistribution of elements.

## Frontend Details

The frontend is developed using Vue 3 and Vuetify, with dynamic routing and state management using Pinia. The app loads author data dynamically through routes and displays books and quotes associated with each author.

### Key Components:

- **`BaseBreadcrumb`**: Displays breadcrumbs for easy navigation.
- **`UiParentCard`**: A card layout used for displaying content like books and quotes.
- **`CardsData`**: Displays the books and quotes of a selected author.
- **`vue3-perfect-scrollbar`**: Custom scrollbars for a smooth user experience.
- **`vue3-apexcharts`**: For displaying charts, if needed.
- **PrimeVue**: Used for rich UI elements.

## Docker Setup

This project also includes Docker support. You can use Docker Compose and Dockerfile to set up and run the application in a containerized environment.

To start the application using Docker Compose, run:
```bash
docker-compose up --build
```

### How to Run the Frontend

1. Navigate to the `quotesync-frontend` directory:
   ```bash
   cd quotesync-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Visit `http://localhost:8080` in your browser.

## Backend Details

The backend is a Django-based RESTful API that serves author data (including books and quotes). It fetches this data from a mock data source (or a database if implemented) and serves it to the frontend.

### How to Run the Backend

1. Navigate to the `quotesync-backend` directory:
   ```bash
   cd quotesync-backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://localhost:8000` to test the API endpoints.

## Environment Variables

Make sure you have a `.env` file in the root directory with the necessary configurations for both frontend and backend:

```env
API_URL=http://localhost:8000/api
```

## Technologies Used

- **Frontend**: Vue 3, Vuetify, Pinia, Axios, Vue Router
- **Backend**: Django, Django Rest Framework (DRF)
- **Styling**: Vuetify, PrimeVue, GridJS



## License

This project is licensed under the MIT License.
