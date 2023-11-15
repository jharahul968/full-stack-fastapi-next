FROM python:3.10
WORKDIR /app/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade
COPY . .
ENV DATABASE_URL=postgresql://rahul:wwe@full-stack-postgres_db-1:5432/rahul
ENV DB_USER=rahul
ENV DB_PASSWORD=wwe
ENV DB_HOST=full-stack-postgres_db-1
ENV DB_PORT=5432
EXPOSE 8000
COPY entrypoint.sh ./
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
