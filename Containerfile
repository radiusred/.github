# Stage 1: Install packages using Debian tooling
FROM --platform=linux/amd64 debian:bookworm-slim AS deps

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
    && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
        | tee /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
        | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        google-cloud-cli \
        python3-pandas \
        python3-numpy \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Copy installed packages into the runtime image
FROM --platform=linux/amd64 ghcr.io/paperclipai/paperclip:latest

COPY --from=deps /usr/lib/google-cloud-sdk/ /usr/lib/google-cloud-sdk/
COPY --from=deps /usr/bin/gcloud /usr/bin/gcloud
COPY --from=deps /usr/bin/gsutil /usr/bin/gsutil
COPY --from=deps /usr/bin/bq /usr/bin/bq
COPY --from=deps /usr/lib/python3/dist-packages/pandas/ /usr/lib/python3/dist-packages/pandas/
COPY --from=deps /usr/lib/python3/dist-packages/numpy/ /usr/lib/python3/dist-packages/numpy/
