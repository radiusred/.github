FROM --platform=linux/amd64 ghcr.io/paperclipai/paperclip:latest AS base

# Install gcloud CLI (required by Cloudy), pandas, and numpy
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
        | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
        | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        google-cloud-cli \
        python3-pandas \
        python3-numpy \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

FROM base AS runtime
