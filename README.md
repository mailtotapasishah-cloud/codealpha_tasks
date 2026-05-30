# codealpha_tasks

## Deployment

This repository contains two services:
- `Language-Translation-Tool` (Streamlit app)
- `Object-Detection-Project` (YOLOv8-based detector exposed as an HTTP API)

CI builds images and pushes them to GitHub Container Registry. To enable automatic deploys to Google Cloud Run, add these GitHub secrets to your repository:

- `GCP_PROJECT` — your GCP project id
- `GCP_REGION` — e.g. `us-central1`
- `GCP_SA_KEY` — service account JSON (base64 or raw JSON)

Service names deployed to Cloud Run:
- `codealpha-translation` (port 8501)
- `codealpha-object-detection` (port 5000)

After adding secrets, push to `main` and the workflow will build, push, and deploy the services.