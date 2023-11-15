# Next, FastAPI and PostgreSQL Full Stack Notes App

## to build using docker compose

    docker compose up -d
    docker compose exec backend-notes alembic upgrade head

## to build using docker
    
    docker network create network-notes
    
    docker run -p 5432:5432 --network network-notes -e  POSTGRES_USER=rahul -e POSTGRES_PASSWORD=wwe --name postgres_db --rm postgres
    
    docker run --name frontend-notes -p 3000:3000 --rm --network network-notes frontend-notes
    
    docker run --rm --name backend-notes -p 8000:8000 --network network-notes backend-notes


This is to be done after creating docker images using docker build . -t <image-name>. Also, do "docker pull postgres" for postgres container.

# for backend

## nfp-backend

Setup:

    python -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Run the development server:

    uvicorn main:app --reload




## for frontend


This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

### Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

### Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

### Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
