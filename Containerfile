# Stage 1: Download gcloud CLI tarball (needs curl, available on Debian)
FROM --platform=linux/amd64 debian:trixie-slim AS deps

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && curl -fsSL https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz \
        | tar -xz -C /opt \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Runtime image
FROM --platform=linux/amd64 ghcr.io/davison/paperclip:local-integration-latest

COPY --from=deps /opt/google-cloud-sdk/ /opt/google-cloud-sdk/
ENV PATH="/opt/google-cloud-sdk/bin:${PATH}"

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends python3-pandas python3-numpy jq \
    && rm -rf /var/lib/apt/lists/*
