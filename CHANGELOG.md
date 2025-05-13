## 1.3.1 (2025-05-13)

No changes.


# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.1] (2025-05-13)

Update Vault version. 

## [1.3.0] - 2025-04-18
- Updated many components to implement Consumer version 1.3.0.
- Moved Redis and PostgreSQL components to Common Agent.
- Added Notification component to Common Agent.


### Kafka

#### 1.0.1 (2025-03-03)

#### Changed
- Remove ingress.issuer from values - cleanup


### eck-monitoring

#### 0.1.12 (2025-03-07)

#### Added
- Added logs parsing for new containers
- Added end user manual for dashboards

#### Changed
- Changed default values for kibana resources

#### Fixed
- Moved changelog file to correct directory
- Upgrade ELK to 8.16.0


### Notification

#### 0.0.2 (2025-03-12)

#### Added
- (SIMPL-10454) asyncAPI created
- (SIMPL-10731) retry mechanism for Kafka created

#### Changed
- (SIMPL-10405) webConfig refactored
- (SIMPL-10551) interfaces refactored; notification channel introduced; default "email" channel added
- (SIMPL-10007) Sonar fixes
- (SPGRLOG-1630) REST API removed