# Deploying AIService to Render

## Prerequisites
- A [Render](https://render.com) account.
- A GitHub repository containing this code.
- An OpenAI API Key.

## Deployment Steps

### Option 1: Using `render.yaml` (Blueprints)
1.  In the Render Dashboard, go to **Blueprints**.
2.  Click **New Blueprint Instance**.
3.  Connect your GitHub repository.
4.  Render will detect the `render.yaml` file in the `AIService` directory (you might need to point it there if it's in a subdirectory).
5.  **Important**: You will be prompted to enter the `OPENAI_API_KEY`. Enter your actual key.
6.  Click **Apply**.

### Option 2: Manual Setup
1.  In the Render Dashboard, click **New +** and select **Web Service**.
2.  Connect your GitHub repository.
3.  **Name**: `aiservice` (or any name you like).
4.  **Root Directory**: `AIService` (This is crucial since the Dockerfile is inside this folder).
5.  **Environment**: `Docker`.
6.  **Region**: Choose the one closest to you.
7.  **Branch**: `main` (or your working branch).
8.  **Environment Variables**:
    - Key: `OPENAI_API_KEY`
    - Value: `sk-...` (your actual OpenAI API key)
9.  Click **Create Web Service**.

## Verification
- Once deployed, Render will build the Docker image. This might take a few minutes.
- Watch the logs for "Build successful" and "Deploying...".
- Once live, you can test the service by sending a POST request to `https://<your-service-url>.onrender.com/upload` with an audio file.
