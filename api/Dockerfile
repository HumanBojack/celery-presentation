FROM python:3.11

WORKDIR /api

# Disable pip's cache
ARG PIP_NO_CACHE_DIR=1
# Avoid creating compiled .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Disable the logging buffering in order to have real time logs
ENV PYTHONUNBUFFERED 1

# Copy and install the requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]