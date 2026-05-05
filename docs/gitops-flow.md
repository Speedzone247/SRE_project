# GitOps Flow

## Desired workflow

1. Developer pushes application code to GitHub.
2. GitHub Actions builds and publishes a container image to GHCR.
3. GitHub Actions updates the Kubernetes Kustomize overlay with the new image tag.
4. Argo CD detects the Git change.
5. Argo CD syncs the desired state into Kubernetes.
6. SRE validates health, SLOs, latency, and error budget burn in Grafana.
7. Incidents are documented with runbooks and RCAs.

## Key principle
Kubernetes is not changed manually for normal releases. Git is the source of truth.
