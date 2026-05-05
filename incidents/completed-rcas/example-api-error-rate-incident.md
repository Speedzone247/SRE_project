# RCA: Simulated API Error Rate Incident

## Summary
A simulated production incident caused elevated 5xx responses.

## Customer Impact
Availability SLO dropped below target during the test window.

## Detection
Prometheus metrics and Grafana dashboards showed elevated 5xx responses.

## Root Cause
The `/fault/error` endpoint intentionally returned HTTP 500 responses.

## Resolution
Stopped fault traffic and verified service recovery.

## Preventive Actions
- Add route-level alerting.
- Add canary promotion checks.
- Add automated rollback criteria.
- Add deployment annotations to dashboards.
