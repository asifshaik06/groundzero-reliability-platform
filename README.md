\# GroundZero â€” Reliability Monitoring \& Alerting Platform



A self-hosted reliability monitoring and alerting prototype built using Docker and open-source monitoring technologies.



\## Overview



GroundZero monitors system performance, evaluates predefined alert conditions, and delivers notifications through Telegram.



\## Technology Stack



\- Docker and Docker Compose

\- Prometheus

\- Node Exporter

\- Grafana

\- Alertmanager

\- Loki and Promtail

\- Python

\- Telegram Bot API



\## Architecture



\*\*GroundZero:\*\* Metrics collection, alert rules, dashboard visualization and notification routing.



\*\*Sherlock:\*\* Lightweight Python HTTP service for receiving alert webhooks. Further log investigation and root-cause analysis are planned.



\## Demonstrated Features



\- CPU and memory monitoring.

\- Grafana system metrics dashboard.

\- Prometheus alert rules.

\- CPU alert threshold: 30%.

\- Memory alert threshold: 80%.

\- Alertmanager notification routing.

\- Successful Telegram notification tests from Windows 11.

\- Docker-based deployment.



\## Current Status



The Grafana dashboard, Prometheus metrics collection, alert rules and Alertmanager-to-Telegram delivery have been demonstrated.



Sherlock's Docker networking, advanced incident analysis and automated remediation remain under development.



\## Configuration



Use the supplied Alertmanager example file as a template. Add your own Telegram bot token and chat ID locally. Never commit actual credentials.



\## Demonstration



The GroundZero Windows demonstration video will be available under the repository's Releases section.



\## Project Status



Working prototype under active development.
