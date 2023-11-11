FROM python:3.10
WORKDIR /app/
ENV DATABASE_URL=postgresql://rahul:wwe@localhost/rahul
ENV DB_USER=rahul
ENV DB_PASSWORD=wwe
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--reload" ]
