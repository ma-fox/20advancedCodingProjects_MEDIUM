# Lightweight base image
FROM node:14-alpine

# Set up working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install all dependencies
RUN npm ci

# Copy the application code
COPY . .

# Build the application
RUN npm run build

# Expose to port 3000
EXPOSE 3000

# Start the application
CMD [ "npm", "start" ]
