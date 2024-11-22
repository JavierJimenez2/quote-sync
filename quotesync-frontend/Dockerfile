# Frontend Dockerfile
FROM node:18

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
# Install dependencies (make sure the node_modules are properly installed)
# RUN rm -rf node_modules && npm install
RUN npm install && npm install rollup @rollup/plugin-commonjs @rollup/plugin-node-resolve --save-dev

# Copy the project files
COPY . .

# Expose the port for Vite's development server
EXPOSE 5173

# Run the Vite development server, specifying host as 0.0.0.0 to allow external access
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
