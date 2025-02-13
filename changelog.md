# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.2] - 2025-02-13

### Changed
- Fixed Filebeat deployment
- Update ECK Operator to 2.16.1
- Update readme

## [1.1.1] - 2025-02-12

### Changed
- Added deployment of CRDs for monitoring

## [1.1.0] - 2025-01-30

### Changed
- Installation required for agent, per site (only once - can be common to more than one agent)
- Common Vault component for all credentials and secrets
- Common Kafka component used in some agents internal asynchronous communications
- Common ELK stack for monitoring ang logs centralisation of one or more agents"
