# CivicCloud SLOs

## Availability SLO
99.9% of API requests should return non-5xx responses over a rolling 30-day window.

## Availability SLI
Good requests divided by total requests.

```promql
sum(rate(http_requests_total{status!~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
```

## Latency SLO
95% of API requests should complete under 300ms.

```promql
histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))
```

## Error Budget
For 99.9% availability, allowed monthly unavailability is 0.1%, or about 43.2 minutes in 30 days.
