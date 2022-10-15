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

# run server
CMD ["gunicorn", "aymaneboukrouh.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]