FROM ghcr.io/paperclipai/paperclip:latest

# Install gcloud CLI (required by Cloudy)
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
