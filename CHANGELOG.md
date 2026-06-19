# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.4] - 2026-06-18

### fixed (1 change)
- fixed issue #33

### changed (1 change)
- added documentation changes suggested by Marco Moschetti

## [3.1.3] - 2026-06-03

### fixed (1 change)
- fixed issue #6 from Governance Authority agent repository

### added (1 change)
- added a needed-by-development argocd deployer file

## [3.1.2] - 2026-05-26

### fixed (1 changes)
- missed monitoring version number in values

## [3.1.1] - 2026-05-26

### changed (3 changes)
- eck-monitoring to v0.5.6
- notifications to v2.6.2
- infrastructure-consumption-monitoring-service to v2.6.1

### fixed (1 changes)
- fixed Gitlab issues #24 and #26 (probes and pgadmin parameters)

## [3.1.0] - 2026-05-20

### fixed (2 changes)
- icms values in application.yaml
- various changes in user-manuals

### changed (16 changes)
- added HA and automatic unsealing after environment changes to OpenBao
- added ignoring differences in ArgoCD to improve app health
- rebuilt and improved deployment parts of README.md
- openbao-init to v1.1.0
- openbao-config to v1.3.6
- openbao to v0.26.2
- monitoring to v0.5.5
- vault webhook to v0.22.2
- confluent operator to v0.1514.19
- kafka to v1.2.2
- postgres operator to v1.15.1
- pgadmin to v1.62.0
- pg-cluster to v1.2.0
- notifications to v2.6.1
- mailpit to v0.31.3
- icms to v2.6.0

## [3.0.2] - 2026-04-21

### fixed (1 change)
- various documentation fixes

## [3.0.1] - 2026-03-11

### fixed (2 changes)
- updated Monitoring stack version to 0.3.3 (SIMPL-24671)
- updated Readme (SIMPL-24688)

## [3.0.0] - 2026-02-25

### fixed (3 changes)
- list of agents interpreted by pg-cluster
- memory limits of pg-cluster
- typos and image links in README.md

### changed (5 changes)
- openbao-config to v1.2.3
- monitoring to v0.3.1
- pg-cluster to v1.1.1
- notifications to v2.1.1
- icms to v2.3.1
