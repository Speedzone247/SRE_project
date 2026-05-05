# Runbook: High API Error Rate

## Alert
HighErrorRate

## Impact
Users may receive HTTP 5xx responses.

## First checks

```bash
kubectl get pods -n platform
kubectl logs deployment/civic-api -n platform
kubectl describe deployment civic-api -n platform
kubectl rollout history deployment/civic-api -n platform
```

## Mitigation

```bash
kubectl rollout undo deployment/civic-api -n platform
```

## Verification

```bash
curl http://localhost:8080/health
kubectl get pods -n platform
```
