FROM node:alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:alpine
WORKDIR /app
COPY --from=builder /app/build app/build
RUN npm install -g serve
EXPOSE 3000
CMD serve -p 3000 -s build
