# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.3] - 2026-07-17

### changed (1 change)
- openbao-init to v1.1.1 (fixing issue #31)
- restored changelog entries (fixing issue #21)

## [4.0.2] - 2026-07-14

### changed (1 change)
- openbao-config to v1.4.1

## [4.0.1] - 2026-07-09

### changed (2 changes)
- Added configOverrides possibility to kafka deployment
- Added OIDC information to README.md (issue #19)

## [4.0.0] - 2026-07-08

### changed (8 changes)
- mailpit configuration (added persistence)
- openbao-config to v1.4.0
- openbao to v0.28.4
- vault-webhook to v1.23.1
- kafka to v1.3.0
- pg-admin to v1.64.0
- pg-cluster to v1.3.0
- notifications to v2.7.0

## [3.1.5] - 2026-07-03

### fixed (3 changes)
- fixed duplicate configuration in documentation (SIMPL-28416)
- altered links in Component Chart Sources (SIMPL-28373)
- fixed links in README.md (SIMPL-28359)

## [3.1.4] - 2026-06-26

### fixed (3 changes)
- fixed issue #33 and #34
- change README.md location (SIMPL-28359)
- added information about resourcePreset key (SIMPL-28199)
 
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

## [2.4.2] - 2025-12-04

### fixed (2 changes)
- Fix the waved deployment and change the split between applications. (SIMPL-21565)
- Fixed SIMPL-21567 bug.

## [2.4.1] - 2025-11-28

### fixed (2 changes)
- Apply fixes to bugs found in OpenBao init scripts.
- Update Notifications app.

## [2.4.0] - 2025-11-15

### changed (2 changes)
- Updated many components to implement Consumer version 2.4.0.
- Update monitoring stack to version 0.1.20.

## [2.3.2] - 2025-10-30

### changed (1 change)
- Replace Vault by OpenBao (fixing bug SIMPL-19876)

## [2.3.1] - 2025-10-29

### changed (1 change)
- Update monitoring stack to version 0.1.20.

## [2.3.0] - 2025-10-10

### changed (2 change)
- Updated many components to implement Common Components agent version 2.3.0.
- Replace Vault with OpenBao

## [2.1.3] - 2025-09-19

### fixed (1 change)
- bitnamilegacy related fixes

## [2.1.2] - 2025-09-01

### fixed (1 change)
- Hotfix for SIMPL-17511

## [2.1.1] - 2025-07-21

### fixed (2 changes)
- Hotfix for SIMPL-14454
- Hotfix for SIMPL-14418

## [2.1.0] - 2025-06-27

### changed (1 change)
- Updated many components to implement Consumer version 2.1.0.
