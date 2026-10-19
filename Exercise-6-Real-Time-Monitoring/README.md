# Exercise 6: Real-Time Operations Monitoring and Alerting

## Objective
Build a monitoring setup for the ZAPPTTO delivery service using Python, Prometheus, Grafana, Docker, and Jenkins.

## Components
- `delivery_metrics.py` — Simulates delivery activity and exposes Prometheus metrics on port 8000.
- `prometheus.yml` — Configures Prometheus scraping for the Python application.
- `alert_rules.yml` — Defines alerts for high pending deliveries and high average delivery time.
- `Jenkinsfile` — Checks Prometheus health, Grafana health, and availability of the pending-deliveries metric.

## Metrics
- Total deliveries
- Pending deliveries
- Deliveries on the way
- Average delivery time

## Services
- Python metrics endpoint: http://localhost:8000/metrics
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Jenkins: http://localhost:8080

## Alert Rules
- `HighPendingDeliveries`: Fires when pending deliveries remain above 10 for 15 seconds.
- `HighAverageDeliveryTime`: Fires when average delivery time remains above 30 seconds for 15 seconds.

## Verification
- Confirmed the delivery metrics endpoint returns metrics.
- Confirmed Prometheus targets are UP.
- Configured a Grafana dashboard with four delivery metric panels.
- Verified the pending-deliveries alert can fire.
- Ran a Jenkins pipeline successfully to check Prometheus, Grafana, and the delivery metrics query.

## Note
The Jenkins pipeline verifies the availability of the monitoring services. It does not deploy or restart those services.
