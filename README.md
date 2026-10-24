# GroundZero - Reliability Monitoring & Alerting Platform

A self-hosted reliability monitoring and alerting prototype built using Docker and open-source technologies.

## Overview

GroundZero monitors system performance, evaluates predefined alert conditions, and delivers notifications through Telegram.

## Technology Stack

- Docker and Docker Compose
- Prometheus
- Node Exporter
- Grafana
- Alertmanager
- Loki and Promtail
- Python
- Telegram Bot API

## Project Components

### GroundZero

Metrics collection, alert rules, dashboard visualization, and notification routing.

### Sherlock

A lightweight Python HTTP service for receiving alert webhooks. Further log investigation and root-cause analysis are under development.

## Demonstrated Features

- Prometheus metrics collection.
- Grafana CPU, memory, network, and disk dashboard.
- CPU alert rule configured above 30%.
- Memory alert rule configured above 80%.
- Alertmanager notification routing.
- Successful Telegram notification tests from Windows.

## Current Development Status

The monitoring dashboard, Prometheus rules, and Alertmanager-to-Telegram notification workflow have been demonstrated.

Sherlock Docker networking, advanced incident analysis, and automated remediation remain under development.

## Demo Video

See the Windows demonstration video in the repository Releases section.

## Security

Never commit Telegram bot tokens, passwords, private configuration files, or runtime data.

## Project Status

Working prototype under active development.
