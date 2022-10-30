FROM node:latest

# set working directory
WORKDIR /app

# copy package*.json
COPY package.json .
COPY package-lock.json .

# install dependencies
RUN npm install


FROM python:latest

# upgrade pip
RUN pip install --upgrade pip

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy source code
COPY . .

# copy node_modules
COPY --from=0 /app/node_modules ./node_modules

# run server
CMD ["gunicorn", "aymaneboukrouh.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]