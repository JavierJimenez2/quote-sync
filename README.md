# QuoteSync

QuoteApp is a full-stack application for managing authors, books, and their respective quotes. The project is divided into three main parts:

- **Frontend**: Built using Vue.js with Vuetify and other libraries for smooth UI/UX.
- **Backend**: A RESTful API built with Django that serves author details, books, and quotes data.
- **Database**: PostgreSQL for storing author, book, and quote information.

# Preview
![Preview](ui.gif)
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

The backend is a Django-based RESTful API that serves author data (including books and quotes). The API endpoints are used by the frontend to fetch and display author information.
The database is PostgreSQL, which stores author, book, and quote data.

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
- **Styling**: Vuetify, PrimeVue

## Features to Introduce

- [ ] **Caching with Redis**: Implement caching to enhance application performance and reduce database queries.  
- [ ] **User Authentication**: Add secure authentication for users to manage their personalized experience.  
- [ ] **Import Notes**: Allow importing notes from Google Documents and Google Play Books.  
- [ ] **AI-Generated Tags**: Automatically generate tags for quotes using AI-based algorithms.  
- [ ] **Author Information**: Scrape and display data about authors, including a short biography.  
- [ ] **Favorite Quotes List**: Enable users to create and manage a favorite list of quotes.  
- [ ] **Quote Playlists**: Allow users to create "playlists" of quotes for thematic or curated collections.  
- [ ] **User Collaboration**: Enable users to create collaborative collections of quotes or playlists.  
- [ ] **Reading Statistics**: Display data such as the number of quotes viewed, most consulted authors, or favorite topics.  
- [ ] **Admin Dashboard**: Design a homepage for admins to display all application statistics in a single view.  
- [ ] **Cloud Backup (AWS)**: Allow users to save their data (favorites, playlists, etc.) to the cloud for access from any device.
- [ ] **Goodreads Integration**: Sync favorite books and authors with existing literary platforms like Goodreads.  
- [ ] **Personal Annotations**: Let users add comments or personal notes to quotes or books.  






## License

This project is licensed under the MIT License.
