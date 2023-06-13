FROM node:14-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH


COPY package.json /app/package.json
RUN npm install --silent
RUN npm install react-scripts@4.0.3 -g --silent

COPY . /app

# start app
CMD ["npm", "start"]
