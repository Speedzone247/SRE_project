# SRE GitOps Platform

A Free Tier–friendly AWS SRE portfolio project using EC2, k3s Kubernetes, GitHub Actions, GHCR, Argo CD, Prometheus, Grafana, SLOs, error budgets, runbooks, and RCA documentation.

## What this demonstrates

- Kubernetes production operations
- GitOps deployment model with Argo CD
- CI/CD with GitHub Actions
- Container publishing to GitHub Container Registry
- SLO/SLI/error budget thinking
- Prometheus metrics and Grafana dashboards
- Incident response and RCA documentation
- Lightweight AWS Free Tier architecture

## GitOps flow

```text
Code push -> GitHub Actions -> Build image -> Push GHCR image -> Update Kustomize overlay -> Argo CD syncs Kubernetes
```

## Local app test

```bash
cd app/api
docker build -t civic-api:dev .
docker run -p 8080:8080 civic-api:dev
curl http://localhost:8080/metrics
```

## Kubernetes deploy test

```bash
kubectl apply -k k8s/overlays/dev
kubectl get pods -n platform
kubectl port-forward svc/civic-api 8080:80 -n platform
curl http://localhost:8080/
```

## Install Argo CD

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl get pods -n argocd
```

Apply the Argo CD app after replacing `YOUR_GITHUB_USERNAME`:

```bash
kubectl apply -f gitops/argocd/application-dev.yaml
```

## SLOs
See `docs/slos.md`.

## Incidents
See `incidents/playbooks` and `incidents/completed-rcas`.
