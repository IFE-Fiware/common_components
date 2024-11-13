
# SIMPL Agents

A brief description of what this project does

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Install the Governance Authority agent](#authority-deployment)
    * [Description](#description)
    * [Prerequisites](#pre-requisites) 
    * [Create the Namespace](#create-the-namespace)
      * [Step 1: Create the Namespace](#step-1-create-the-namespace)
      * [Step 2: Verify the Namespace](#step-2-verify-the-namespace)
    * [Deploy the Namespace](#deploy-the-namespace)
      * [Step 1: Modify YAML Configuration Files](#step-1-modify-yaml-configuration-files)
        * [Redis](#redis)
          * [Example of values.yaml](#example-of-valuesyaml)
        * [Postgresql](#postgresql)
          * [Example of values-authority.yaml](#example-of-values-authorityyaml)
        * [Keycloak](#keycloak)
          * [Example of values.yaml](#example-of-valuesyaml-1)
        * [EJBCA](#EJBCA)
          * [Example of values.yaml](#example-of-valuesyaml-2)
        * [Onboarding](#onboarding)
          * [Prerequisites](#prerequisites)
          * [Example of values.yaml](#example-of-valuesyaml-3)
          * [Configuration](#configuration)
        * [Security Attributes Provider](#security-attributes-provider)
          * [Example of values.yaml](#example-of-valuesyaml-4)
          * [Configuration](#configuration-1)
        * [Simpl Cloud Gateway](#simpl-cloud-gateway)
          * [Example of values.yaml](#example-of-valuesyaml-5)
          * [Configuration](#configuration-2)
          * [Profiles](#profiles)
          * [Common configuration](#common-configuration)
        * [User Roles](#users-roles)
          * [Prerequisites](#prerequisites-1)
          * [Example of values.yaml](#example-of-valuesyaml-6)
          * [Configuration](#configuration-3)
        * [Frontend](#frontend)
          * [Example of values.yaml](#example-of-valuesyaml-7)
          * [Configuration](#configuration-4)
        * [TLS Gateway](#tls-gateway)
          * [Prerequisites](#prerequisites-2)
          * [Example of values.yaml](#example-of-valuesyaml-8)
          * [Configuration](#configuration-5)
          * [Get the TLS Gateway Truststore](#get-the-tls-gateway-truststore)
          * [Profile-Based Configuration](#profile-based-configuration)
      * [Step 2: Deploy the Application Using Helm Charts](#step-2-deploy-the-application-using-helm-charts)
    * [Change the namespace](#change-the-namespace)
    * [Delete the deployment](#delete-the-deployment)
    * [Troubleshooting](#troubleshooting)          
3. [Install a Data Provider Agent](#data-provider-deployment)
    * [Description](#description-1)
    * [Prerequisites](#pre-requisites-1)
    * [Create the Namespace](#create-the-namespace-1)
      * [Step 1: Create the Namespace](#create-the-namespace-1)
      * [Step 2: Verify the Namespace](#step-2-verify-the-namespace-1)
    * [Installation](#installation)
      * [Files preparation](#files-preparation)
      * [Manual steps](#manual-steps)
    * [Deploy the Namespace](#deploy-the-namespace-1)
      * [Step 1: Modify YAML configuration files](#step-1-modify-yaml-configuration-files-1)
        * [Redis](#redis-1)
          * [Example of values.yaml](#example-of-valuesyaml-9)
        * [Postgresql](#postgresql-1)
          * [Example of values-participant.yaml](#example-of-values-participantyaml)
        * [Keycloak](#keycloak-1)
          * [Example of values.yaml](#example-of-valuesyaml-10)
        * [SIMPL Cloud Gateway](#simpl-cloud-gateway-1)
          * [Example of values.yaml](#example-of-valuesyaml-11)
          * [Profiles](#profiles-2)
          * [Common configuration](#common-configuration-1)
        * [User & Roles](#user--roles)
          * [Example of values.yaml](#example-of-valuesyaml-12)
          * [Configuration](#configuration-6)
        * [Frontend](#frontend-1)
          * [Example of values.yaml](#example-of-valuesyaml-13)
          * [Configuration](#configuration-7)
      * [Step 2: Deploy the Application Using Helm Charts](#step-2-deploy-the-application-using-helm-charts-1)
   * [Change the Namespace](#change-the-namespace-1)
   * [Delete the Deployment](#delete-the-deployment-1)
   * [Troubleshooting](#troubleshooting-1)
4. [Install a Consumer Agent](#consumer-deployment)
     * [Description](#description-2)
   * [Prerequisites](#prerequisites-4)
   * [Create the Namespace](#create-the-namespace-2)
     * [Step 1: Create the Namespace](#create-the-namespace-2)
     * [Step 2: Verify the Namespace](#step-2-verify-the-namespace-2)
   * [Deploy the Namespace](#deploy-the-namespace-2)
     * [Step 1: Modify YAML configuration files](#step-1-modify-yaml-configuration-files-2)
       * [Redis](#redis-2)
         * [Example of values.yaml](#example-of-valuesyaml-14)
       * [Postgresql](#postgresql-2)
         * [Example of values-participant.yaml](#example-of-values-participantyaml-1)
       * [Keycloak](#keycloak-2)
         * [Example of values.yaml](#example-of-valuesyaml-15)
       * [SIMPL CLoud Gateway](#simpl-cloud-gateway-2)
         * [Example of values.yaml](#example-of-valuesyaml-16)
         * [Profiles](#profiles-3)
         * [Common configuration](#common-configuration-2)
       * [User & Roles](#user--roles)
         * [Prerequisites](#prerequisites-6)
         * [Example of values.yaml](#example-of-valuesyaml-17)
         * [Configuration](#configuration-8)
       * [Frontend](#frontend-2)
         * [Example of values.yaml](#example-of-valuesyaml-18)       
         * [Configuration](#configuration-9)
       * [Step 2: Deploy the Application Using Helm Charts](#step-2-deploy-the-application-using-helm-charts-2)
   * [Change the Namespace](#change-the-namespace-2)
   * [Delete the Deployment](#delete-the-deployment-2)
   * [Troubleshooting](#troubleshooting-2)

# Prerequisites

| Tool                |        Version        | Description                                                                                                                                                                                  |
|---------------------|:---------------------:|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Git                 |   2.47.x or higher    | Version control system for tracking and managing changes to agents https://git-scm.com/downloads                                                                                             |
| Helm                |   3.14.x or higher    | Package Manager for Kubernetes https://github.com/helm/helm/releases                                                                                                                         |
| Kubernetes Cluster  |    1.29.x or newer    | Other version *might* work but tests were performed using 1.29.x version                                                                                                                     |
| Argo CD             |    2.11.x or newer    | Used as GitOps tool . App of apps concept. <br/> Other version *might* work but tests were performed using 2.11.x version. <br/> Image used: `quay.io/argoproj/argocd:v2.11.3`               |
| DNS sub-domain name |          N/A          | This domain will be used to address all services of the agent. <br/> example: `*.authority1.int.simpl-europe.eu`                                                                             |
| nginx-ingress       |    1.10.x or newer    | Used as ingress controller. <br/> Other version *might* work but tests were performed using 1.10.x version. <br/> Image used: `registry.k8s.io/ingress-nginx/controller:v1.10.0`             |
| cert-manager        |    1.15.x or newer    | Used for automatic cert management. <br/> Other version *might* work but tests were performed using 1.15.x version. <br/> Image used: `quay.io/jetstack/cert-manager-controller::v1.15.3`    |
| Hashicorp Vault     |    1.17.x or newer    | Other version *might* work but tests were performed using 1.17.x version. <br/> Image used: `hashicorp/vault:1.17.2`                                                                         |
| nfs-provisioner     |    4.0.x or newer     | Backend for *Read/Write many* volumes. <br/> Other version *might* work but tests were performed using 4.0.x version. <br/> Image used: `registry.k8s.io/sig-storage/nfs-provisioner:v4.0.8` |

# Authority Deployment

## Description
This project contains the configuration files required for deploying an application using Helm and ArgoCD.
- the deployment will be done by master helm chart allowing to deploy a **Governance Authority** agent using a single command.
- templates of values.yaml files used inside *Integration* environment under `app-values` folder

## Pre-Requisites

Make sure you have installed the required tools from [Prerequisites](#prerequisites)

## Create the Namespace
Before deploying the application, ensure that the **authority** (i.e. authority1) namespace exists in your Kubernetes cluster. If the expected namespace does not exist yet you can create it with the following steps:

### Step 1: Create the Namespace
Once the namespace variable is set, you can create the namespace using the following kubectl command:

`kubectl create namespace authority1`

### Step 2: Verify the Namespace
To ensure that the namespace was created successfully, run the following command:

`kubectl get namespaces`
<br/>This will list all the namespaces in your cluster, and you should see the one you just created listed.

## Deploy the namespace
Deploying a dedicated namespace, such as **authority1**, helps isolate resources and applications within a Kubernetes cluster.

Filling the namespace with content requires the following activity:

### Step 1: Modify YAML Configuration Files

The first step in configuring the application is to update the necessary YAML files. These files contain key values that define the application's environment, behavior, and settings.


#### Redis

##### Example of values.yaml
```bash
replica:
  replicaCount: 0
architecture: standalone
```

#### Postgresql

##### Example of values-authority.yaml

```yaml
primary:
  initdb:
    scripts:
      init.sql: |
        CREATE USER ejbca WITH PASSWORD 'ejbca2123' CREATEDB;
        CREATE DATABASE ejbca OWNER ejbca;
        CREATE USER keycloak WITH PASSWORD 'keycloak' CREATEDB;
        CREATE DATABASE keycloak OWNER keycloak;
        CREATE USER securityattributesprovider WITH PASSWORD 'securityattributesprovider' CREATEDB;
        CREATE DATABASE securityattributesprovider OWNER securityattributesprovider;
        CREATE USER onboarding WITH PASSWORD 'onboarding' CREATEDB;
        CREATE DATABASE onboarding OWNER onboarding;
        CREATE USER usersroles WITH PASSWORD 'usersroles' CREATEDB;
        CREATE DATABASE usersroles OWNER usersroles;
        CREATE USER identityprovider WITH PASSWORD 'identityprovider' CREATEDB;
        CREATE DATABASE identityprovider OWNER identityprovider;

```

#### Keycloak

<!-- TODO: remove {{ .Release.Namespace }} ? -->
##### Example of values.yaml
```yaml
apiUrl: "<authority endpoint>" # example: https://authority.be.aruba-simpl.cloud

extraEnvVars: 
  - name: KC_HOSTNAME_ADMIN_URL
    value: "< apiUrl as above >/auth" # update
  - name: KC_HOSTNAME_URL
    value: "< apiUrl as above >/auth" # update
  - name: USERS_ROLES_BASE_URL
    value: "http://users-roles.<namespace>.svc.cluster.local:8080" # update
  - name: KEYCLOAK_BASE_URL
    value: "< apiUrl as above >/auth" # update
  - name: REALM
    value: "<authority>" # set this

auth:
  adminPassword: "admin"

keycloakConfigCli:
  enabled: true
  configuration:
    authority.json: | 
      {{- $.Files.Get "kc-init/authority-realm-export.json" -}}

postgresql:
  enabled: false

externalDatabase:
  annotations: {}
  database: keycloak
  existingSecret: ""
  existingSecretDatabaseKey: ""
  existingSecretHostKey: ""
  existingSecretPasswordKey: ""
  existingSecretPortKey: ""
  existingSecretUserKey: ""
  host: "postgresql.<namespace>.svc.cluster.local"
  password: keycloak
  port: 5432
  user: keycloak
```

#### EJBCA

> **⚠️** *Step only needed for the governance authority*

Before installing EJBCA, update the values in `values.yaml` reasonably to interact with the Postgresql instance.

##### Example of values.yaml

```yaml
hostname: &hostname ejbca-community-helm.<namespace>.svc.cluster.local # update this
fullnameOverride: ejbca-community-helm
ejbca:
  env:
    HTTPSERVER_HOSTNAME: *hostname
    TLS_SETUP_ENABLED: "true"
    DATABASE_JDBC_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/ejbca # update this
    DATABASE_USER: "ejbca"
    DATABASE_PASSWORD: "ejbca2123"
nginx:
  host: *hostname
```

<!-- helm repo add <repo name> https://code.europa.eu/api/v4/projects/<project_id>/packages/helm/<channel> -->


#### Onboarding
> **⚠️** *Step only needed for the governance authority*

#### Prerequisites

- Possess EJBCA SuperAdmin credentials (i.e. PKCS#12 certificate - also named TrustStore - and password)
- Possess ManagementCA (also named Keystore and its password)

<!-- TODO: update "<password used for the keystore of onboarded participant> explain!!!! -->
##### Example of values.yaml
```yaml
global:
  hostTls: "tls.authority.dev.simpl-europe.eu" # this is an example, update this field
  
  # TODO: find a name to refer to this password in the configuration of the following microservices 
  keystore:
    password: "<define a password for the keystore of onboarded participant>" # update this

env:
  SPRING_DATASOURCE_URL: "jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/onboarding"
  SPRING_DATASOURCE_USERNAME: "onboarding"
  SPRING_DATASOURCE_PASSWORD: "onboarding"

ejbca:
  keystore:
    base64: "<base64 of the keystore>" 
    password: "<password of the keystore>"
  truststore:
    base64: "<base64 of the truststore>"
    password: "<password of the truststore>"
  enrollConfig:
    url: "https://ejbca-community-helm.<namespace>.cluster.local:30443"
    profileName: "<End Entity Certificate Profile>" # update this field, example "Onboarding TLS Profile"
    endEntityName: "<EndEntity Profile>" # update this field, example "TLS Server Profile"
    caName: "<SubCA>" # update this field, example "OnBoardingCA"
```

> **💡** Tip: Generate the *base64* of the keystore and truststore with the following command: `<keystore or trustore> | base64 --wrap=0` (0 is used to disable line wrapping)

##### Configuration
The environment variables listed below are used to define the connection details, credentials and file locations required to interact with EJBCA and manage SSL Certificates. For further configuration, view the Helm template and update the values as required.

- **Certificate Configuration**
  - The `global.hostTls` set `SIMPL_CERTIFICATE_SAN`: The Subject Alternative Name (SAN) for the certificate.
  - The value `global.keystore.password` set `SIMPL_CERTIFICATE_PASSWORD`: The password for the certificate used by the service.

- **Database Configuration**
  - `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to the PostgreSQL database.
    - Format: `jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/onboarding`
  - `SPRING_DATASOURCE_USERNAME`: The username for the PostgreSQL database.
  - `SPRING_DATASOURCE_PASSWORD`: The password for the PostgreSQL database.

- **EJBCA Configuration**
  - The value `ejbca.enrollConfig.url` set `EJBCA_URL`: The URL for the EJBCA enrollment service.
  - The value `ejbca.enrollConfig.profileName` set `EJBCA_PROFILE_NAME`: The profile name to be used when enrolling with EJBCA.
  - The value `ejbca.enrollConfig.endEntityName` set `EJBCA_END_ENTITY_NAME`: The name of the end entity in EJBCA.
  - The value `ejbca.enrollConfig.caName` set `EJBCA_CA_NAME`: The name of the Certificate Authority (CA) in EJBCA.

- **SSL Configuration - Keystore and Truststore**
  - The value `ejbca.keystore.password` set `SPRING_SSL_BUNDLE_JKS_EJBCA_KEYSTORE_PASSWORD`: The password for the EJBCA keystore.
  - The value `ejbca.truststore.password` set `SPRING_SSL_BUNDLE_JKS_EJBCA_TRUSTSTORE_PASSWORD`: The password for the EJBCA truststore.
  - `SPRING_SSL_BUNDLE_JKS_EJBCA_KEY_ALIAS`: The alias for the key within the keystore. Default value: `superadmin`
  - `SPRING_SSL_BUNDLE_JKS_EJBCA_KEYSTORE_LOCATION`: The file path for the EJBCA keystore. Default path: `/etc/certs/keystore.p12`
  - `SPRING_SSL_BUNDLE_JKS_EJBCA_TRUSTSTORE_LOCATION`: The file path for the EJBCA truststore. Default path: `/etc/certs/truststore.jks`


#### Security Attributes Provider
> **⚠️** *Step only needed for the governance authority*

##### Example of values.yaml
```yaml
env:
  MICROSERVICE_ONBOARDING_URL: http://onboarding.<namespace>.svc.cluster.local:8080
  MICROSERVICE_USERS_ROLES_URL: http://users-roles.<namespace>.svc.cluster.local:8080
  SIMPL_EPHEMERAL_PROOF_EXPIRE_AFTER: 3D
  SPRING_DATA_REDIS_HOST: redis-master.<namespace>.svc.cluster.local
  SPRING_DATA_REDIS_PASSWORD: admin
  SPRING_DATA_REDIS_PORT: "6379"
  SPRING_DATA_REDIS_USERNAME: default
  SPRING_DATASOURCE_PASSWORD: securityattributesprovider
  SPRING_DATASOURCE_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/securityattributesprovider
  SPRING_DATASOURCE_USERNAME: securityattributesprovider

global:
  hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
  hostTls: tls.authority.dev.simpl-europe.eu # this is an example, update this field
  keystore:
    password: < password defined in the oboarding component >
```

##### Configuration

The environment variables listed below are used to define the connection details and credentials for PostgreSQL, Redis, and other services. For further configuration, view the Helm template and update the values as required.

**PostgreSQL Configuration**
- `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to the PostgreSQL database. Format: `jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles`
- `SPRING_DATASOURCE_USERNAME`: The username for the PostgreSQL database. Default value: `usersroles`
- `SPRING_DATASOURCE_PASSWORD`: The password for the PostgreSQL database. Default value: `usersroles`

**Redis Configuration**
- `SPRING_DATA_REDIS_HOST`: The host address for the Redis service. Format: `redis-master.<namespace>.svc.cluster.local`
- `SPRING_DATA_REDIS_PORT`: The port on which Redis is running. Default value: `6379`
- `SPRING_DATA_REDIS_USERNAME`: The username for connecting to Redis. Default value: `default`
- `SPRING_DATA_REDIS_PASSWORD`: The password for connecting to Redis. Default value: `admin`

**Ephemeral Proof Issuer Configuration**
- The value `tls.gateway.url` set `SIMPL_EPHEMERAL_PROOF_ISSUER_URL`: The URL for the Ephemeral Proof Issuer service.
- The value `global.keystore.password` set `SIMPL_CERTIFICATE_PASSWORD`: The password for the certificate used by the service.
- `SIMPL_EPHEMERAL_PROOF_EXPIRE_AFTER` : The time to Live of the ephemeral proof in redis. Default value: `3D`, follow the spring standard of the Duration class.


#### Simpl Cloud Gateway

##### Example of values.yaml
```yaml
global:
  cors: # this is an example, update this field
    allowOrigin: https://authority.fe.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:3000
  hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
  hostFe: authority.fe.dev.simpl-europe.eu  # this is an example, update this field
  hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
  ingress:
    issuer: dev-prod
  profile: < authority >

microservices:
  ejbcaUrl: http://ejbca-community-helm.<namespace>.svc.cluster.local:30080
  keycloakUrl: http://keycloak.<namespace>.svc.cluster.local
  onboardingUrl: http://onboarding.<namespace>.svc.cluster.local:8080
  securityAttributesProviderUrl: http://security-attributes-provider.<namespace>.svc.cluster.local:8080
  usersRolesUrl: http://users-roles.<namespace>.svc.cluster.local:8080
```

##### Configuration

This configuration supports two main profiles: authority and participant. Depending on the specified profile, different environment variables will be set. For further configuration, view the Helm template and update the values as required.

##### Profiles
- The value `global.profile` set `SPRING_PROFILES_ACTIVE`: This sets the active Spring profile. The value should be `authority`.
- `SAP_URL`: URL for the Security Attributes Provider. Format: `http://security-attributes-provider.<namespace>.svc.cluster.local:8080`
- `ONBOARDING_URL`: URL for the Onboarding. Format: `http://onboarding.<namespace>.svc.cluster.local:8080`
- `EJBCA_URL`: URL for the EJBCA. Format: `http://ejbca-community-helm.<namespace>.svc.cluster.local:30080`
- `IDENTITY_PROVIDER_URL`: URL for the Identity Provider. Format: `http://identity-provider.<namespace>.svc.cluster.local:8080`

##### Common Configuration

Regardless of the profile, the following environment variables are configured:

- The value `global.cors.allowOrigin` set `CORS_ALLOWED_ORIGINS`: Specifies which origins are allowed to make cross-origin requests.
- The value `miroservices.keycloakUrl` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
- The value `miroservices.usersRolesUrl` set `USERSROLES_URL`: The URL for the Users&Roles service.
- `CORS_ALLOWED_HEADERS`: Specifies which HTTP headers are allowed in cross-origin requests.
  - Default value: `Access-Control-Allow-Headers, Access-Control-Allow-Credentials, Access-Control-Allow-Origin, Access-Control-Allow-Methods, Keep-Alive, User-Agent, Content-Type, Authorization, Tenant, Channel, Platform, Set-Cookie, geolocation, x-mobility-mode, device, Cache-Control, X-Request-With, Accept, Origin`.

#### Users Roles

##### Prerequisites

- *simpl-cloud-gateway* up and running
- *security-attributes-provider* up and running

##### Example of values.yaml
```yaml
env:
  KEYCLOAK_MASTER_PASSWORD: admin # this password was set in keycloak values.yaml
  KEYCLOAK_MASTER_USER: user
  SPRING_DATA_REDIS_HOST: redis-master.<namespace>.svc.cluster.local
  SPRING_DATA_REDIS_PASSWORD: admin
  SPRING_DATA_REDIS_PORT: "6379"
  SPRING_DATA_REDIS_USERNAME: default
  SPRING_DATASOURCE_PASSWORD: usersroles
  SPRING_DATASOURCE_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles
  SPRING_DATASOURCE_USERNAME: usersroles

global:
  hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
  hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
  keystore:
    password: < password defined in the oboarding component >
  profile: <authority>
```

#### Configuration

The environment variables listed below are used to define the connection details for PostgreSQL, Redis, Keycloak, and other services. For further configuration, view the Helm template and update the values as required.

**Database Configuration**
- `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to the PostgreSQL database. Format: `jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles`
- `SPRING_DATASOURCE_USERNAME`: The username for the PostgreSQL database.
- `SPRING_DATASOURCE_PASSWORD`: The password for the PostgreSQL database.

**Redis Configuration**
- `SPRING_DATA_REDIS_HOST`: The host address for the Redis service. Format: `redis-master.<namespace>.svc.cluster.local`
- `SPRING_DATA_REDIS_PORT`: The port on which Redis is running. Default value: `6379`
- `SPRING_DATA_REDIS_USERNAME`: The username for connecting to Redis.
- `SPRING_DATA_REDIS_PASSWORD`: The password for connecting to Redis.

**Keycloak Configuration**
- The value `global.hostBe` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
- The value `global.profile` set `KEYCLOAK_APP_REALM`: The realm to be used for the application within Keycloak.

**Client Authority Configuration**
- The value `global.hostTls` set `CLIENT_AUTHORITY_URL`: The URL for the client authority service.
- The value `global.keystore.password` set `CLIENT_CERTIFICATE_PASSWORD`: The password for the client certificate.

#### Frontend

##### Example of values.yaml
```yaml
hostFe: authority.fe.dev.simpl-europe.eu # this is an example, update this field
cors: # this is an example, update this field
  allowOrigin: https://authority.be.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:4203,http://localhost:3000
ingress:
  issuer: dev-prod

env:
- name: APPLICATION
  value: <onboarding or participant-utility>
- name: API_URL
  value: "https://authority.be.dev.simpl-europe.eu" # this is an example, update this field
- name: KEYCLOAK_URL
  value: "https://authority.be.dev.simpl-europe.eu/auth" # this is an example, update this field
- name: KEYCLOAK_REALM
  value: "<authority>" 
- name: KEYCLOAK_CLIENT_ID
  value: "frontend-cli"
```

##### Configuration
The configuration provides details on the backend and frontend host URLs, CORS allowed origins, ingress issuer, and environment variables for the onboarding application. For further configuration, view the Helm template and update the values as required.

**Frontend Host Configuration**
- `hostFe`: The hostname for the frontend service. Value: `my.frontend.host`

**CORS Configuration - Allowed Origins**
- `cors.allowOrigin`: Specifies the origins that are allowed to access the application resources via cross-origin requests.
  - Value: `https://my.frontend.host, https://participant.fe.aruba-simpl.cloud, http://localhost:4202, http://localhost:4203, http://localhost:3000`

**Ingress Configuration - Issuer**
- `ingress.issuer`: The issuer for the ingress, which is typically used for managing TLS certificates. Value: `your-issuer-ingress`

**Environment Variables**
- `APPLICATION`: The name of the application. Value: `onboarding`.
- `API_URL`: The URL for the API backend. Value: `https://my.backend.host`
  
**Keycloak Configuration**
- `KEYCLOAK_URL`: The URL for the Keycloak authentication service. Value: `https://my.backend.host/auth`
- `KEYCLOAK_REALM`: The Keycloak realm that the application uses for authentication. Value: `authority`
- `KEYCLOAK_CLIENT_ID`: The client ID used by the application to authenticate with Keycloak. Value: `frontend-cli`

#### TLS Gateway

This microservice is a gateway for inbound Tier 2 API operation between agents and work only in https on mTLS.

##### Prerequisites

- All the previous microservices up and runnning

##### Example of values.yaml
```yaml
global:
  authorityUrl: https://authority.be.dev.simpl-europe.eu # this is an example, update this field
  cors: # this is an example, update this field
    allowOrigin: https://authority.fe.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:3000
  profile: <authority>
microservices:
  securityAttributesProviderUrl: http://security-attributes-provider.<namespace>.svc.cluster.local:8080
ssl:
  keyStore:
    base64: "<base64 of the keystore>" # get the keystore as explained in Configuration
    password: "<password defined in the oboarding component>"
  trustStore:
    base64:  "<base64 of the truststore>" # get the truststore as explained in Configuration
    password: "<password defined in the oboarding component>"
```

> **💡** Tip: Generate the *base64* of the keystore and truststore with the following command: `<keystore or trustore> | base64 --wrap=0` (0 is used to disable line wrapping)

##### Configuration

######  Download the TLS Gateway Governance Authority keystore
> **⚠️** *Step required for governance only, a participant MUST be onboarded through the application UI by following the onboarding process*

To initialize the authority, you must send a `POST` request to the following API endpoint of the `security-attributes-provider`: `http://localhost:8080/participant/initialize`.

To initialize the authority, you must call this API `POST` of the `security-attributes-provider`. Since the API requires authentication, you need to obtain a JWT from Keycloak for a user with the **T2IAA_M** role. In this example, we use the preconfigured user `e.j`. Here is an example of how to obtain the token and call the API.

```bash
# Authentication flow - Direct Access Grants must be enbled for frontend-cli in Keycloak clients settings
curl --location 'https://authority.be.dev.simpl-europe.eu/auth/realms/authority/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=frontend-cli' \
--data-urlencode 'password=password' \
--data-urlencode 'username=e.j'
```

Alternately, you can obtain a JWT without needing to modify the Keycloak client settings for the `frontend-cli` by interacting with the authority frontend through the following API:
`https://<your-domain>/application/additional-request`, for example `https://authority.fe.authority1.int.simpl-europe.eu/application/additional-request`.

To retrieve the token open your browser and navigate to that url. Perform the requested login and open the *Network* tab in the browser's *DevTools*.

![](./imgs/Access%20token.png)

Since this is an internal endpoint, you'll need to set up a port forward on the microservice to access it. In this example, we assume that you've forwarded the service port to your local port `8080`.

```bash
kubectl port-forward security-attributes-provider 8080:8080

curl --location 'http://localhost:8080/participant/initialize' \
-X POST \
--header 'Authorization: Bearer <JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "organizationName" : "<my-organization>",
  "identityAttributes" : [ ]
}'
```

Then download the credentials, i.e. the **keystore**, from `user-roles`. Since this is an internal endpoint, you'll need to set up a port forward on the microservice to access it. In this example, we assume that you've forwarded the service port to your local port `8080`.

```bash
kubectl port-forward users-roles 8080:8080

curl --location 'http://localhost:8080/credential/download' \
-o keystore-tls-gateway.p12
```

#####  Get the TLS Gateway truststore

Authorities can download the truststore, i.e. OnBoardingCa.jks, from EJBCA Admin dashboard, as done similarly [here](/doc/EJBCA.md#download-the-managementca-certificate). 

##### Profile-Based Configuration

###### Profiles

- The value `global.profile` set `SPRING_PROFILES_ACTIVE`: This sets the active Spring profile. The value is `authority`.
- The value `microservices.securityAttributesProviderUrl` set `SAP_URL`: The URL for the Security Attributes Provider (SAP) microservice.

#### CORS Configuration

- The value `global.cors.allowOrigin` set `CORS_ALLOWED_ORIGINS`: The allowed origins for CORS requests.
  - Default value includes: `Access-Control-Allow-Headers`, `Access-Control-Allow-Credentials`, `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Keep-Alive`, `User-Agent`, `Content-Type`, `Authorization`, `Tenant`, `Channel`, `Platform`, `Set-Cookie`, `geolocation`, `x-mobility-mode`, `device`, `Cache-Control`, `X-Request-With`, `Accept`, `Origin`.

##### SSL Configuration
<!-- - `SERVER_SSL_TRUST_STORE`: The location of the truststore file. -->
<!-- - `SERVER_SSL_KEY_STORE`: The location of the keystore file. -->
- The value `ssl.keyStore.password` set `SERVER_SSL_KEY_STORE_PASSWORD`: The password for the keystore.
- The value `ssl.trustStore.password` set `SERVER_SSL_TRUST_STORE_PASSWORD`: The password for the truststore.


### Step 2: Deploy the Application Using Helm Charts

Once the YAML configuration files have been updated, the next step is to deploy the application using Helm charts. Helm is a package manager for Kubernetes, allowing you to manage and deploy Kubernetes applications efficiently.

Go to master charts directory:

`cd .\charts\`

Now you can deploy the namespace:

`helm install authority . `

:rotating_light: :rotating_light: :rotating_light: **Attention!!!** :rotating_light: :rotating_light: :rotating_light: <br>
<b><i>After installing the namespace, there are services that connect using the TLS protocol (e.g. EJBCA). In the current phase of application development, this element must be configured manually.
The entire procedure is described in confuence:</i></b>

https://confluence.simplprogramme.eu/display/SIMPL/EJBCA+Configuration

<b><i>For the namespace authority to work correctly, it is necessary to perform the actions described in the link above.</i></b>

## Change the namespace

The process of implementing changes is analogous to deploying the namespace for the first time:

`helm upgrade authority . `

## Delete the deployment:

`helm uninstall authority .`


# Troubleshooting
If you encounter issues during deployment, check the following:

- Ensure that ArgoCD is properly set up and running.
- Verify that the authority namespace exists in your Kubernetes cluster.
- Check the ArgoCD application logs and Helm error messages for specific issues.


---

# Data Provider Deployment

## Description

This repo contains:
- a master helm chart allowing to deploy a **Dataprovider** agent using a single command.
- templates of values.yaml files used inside *Integration* environment under `app-values` folder

## Pre-Requisites

Make sure you have installed the required tools from Prerequisites

## Create the Namespace
Before deploying the application, ensure that the **data-provider** (i.e. data-provider1) namespace exists in your Kubernetes cluster. If the expected namespace does not exist yet you can create it with the following steps:

### Step 1: Create the Namespace
Once the namespace variable is set, you can create the namespace using the following kubectl command:

`kubectl create namespace data-provider1`

### Step 2: Verify the Namespace
To ensure that the namespace was created successfully, run the following command:

`kubectl get namespaces`
<br/>This will list all the namespaces in your cluster, and you should see the one you just created listed.

## Installation

The deployment is based on master helm chart which, when applied on Kubernetes cluster, should deploy the Data Provider to it using ArgoCD.

### Files preparation

The suggested way for deployment, is to unpack the released package to a folder on a host where you have kubectl and helm available and configured.

There is basically one file that you need to modify - values.yaml.
There are a couple of variables you need to replace.

| Variable name          |     Example         | Description     |
| ---------------------- |     :-----:         | --------------- |
| ${NAMESPACE}           | dataprovider01-iaa  | Namespace on the cluster, also used as ArgoCD application name |
| ${NAMESPACETAG}        | dataprovider01      | Namespace tag - that will be in FQDN differentiating the deployment, used for example in participant.be.**dataprovider01**.int.simpl-europe.eu  |
| ${DOMAINSUFFIX}        | int.simpl-europe.eu | Domain suffix in FQDN, used for example in participant.be.dataprovider01.**int.simpl-europe.eu** |

You might also need to modify (if needed) the values in keys:

| Variable key           |     Example         | Description     |
| ---------------------- |     :-----:         | --------------- |
| values.repo_URL        | https://....git     | URL for repo with app-values folder |
| values.branch          | develop             | Branch of this repo to use          |

### Manual steps

Two volumes needs to be created manually at the moment:
* nfs-storage-pvc-xsfc
* nfs-storage-pvc-sdapibe

This will be fixed in future versions.

In values of TLS Gateway you need to input the base64 encoded keystore and truststore, with their passwords, in those keys:

```
ssl:
  keyStore:
    base64: "yourbase64keystore"
    password: "yourpassword"
  trustStore:
    base64: "yourbase64truststore"
    password: "yourpassword"
```


## Deploy the namespace
Deploying a dedicated namespace, such as **data-provider1**, helps isolate resources and applications within a Kubernetes cluster.

Filling the namespace with content requires the following activity:

### Step 1: Modify YAML configuration files

The first step in configuring the application is to update the necessary YAML files. These files contain key values that define the application's environment, behavior, and settings.

#### Redis

##### Example of values.yaml
```yaml
replica:
  replicaCount: 0
architecture: standalone
```

#### Postgresql

##### Example of values-participant.yaml
```yaml
primary:
  initdb:
    scripts:
      init.sql: |
        CREATE USER keycloak WITH PASSWORD 'keycloak' CREATEDB;
        CREATE DATABASE keycloak OWNER keycloak;
        CREATE USER usersroles WITH PASSWORD 'usersroles' CREATEDB;
        CREATE DATABASE usersroles OWNER usersroles;
```
> **⚠️** The configuration examples use the users and passwords mentioned above. If you change them, ensure that your configuration reflects those changes accordingly.

#### Keycloak

##### Example of values.yaml
```yaml
apiUrl: "<participant endpoint>" # example: https://participant.be.aruba-simpl.cloud
                                  
extraEnvVars:
- name: KC_HOSTNAME_ADMIN_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: KC_HOSTNAME_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: USERS_ROLES_BASE_URL
  value: "http://users-roles.<namespace>.svc.cluster.local:8080" # update
- name: KEYCLOAK_BASE_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: REALM
  value: participant
 
auth:
adminPassword: "admin"
 
keycloakConfigCli:
  enabled: true
  configuration:
    participant.json: |
      {{- $.Files.Get "kc-init/participant-realm-export.json" -}}
 
postgresql:
enabled: false
 
externalDatabase:
annotations: {}
database: keycloak
existingSecret: ""
existingSecretDatabaseKey: ""
existingSecretHostKey: ""
existingSecretPasswordKey: ""
existingSecretPortKey: ""
existingSecretUserKey: ""
host: "postgresql.<namespace>.svc.cluster.local"
password: keycloak
port: 5432
user: keycloak
```

#### SIMPL Cloud Gateway

##### Example of values.yaml

```yaml
global:
cors: # this is an example, update this field
  allowOrigin: https://authority.fe.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:3000
hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
hostFe: authority.fe.dev.simpl-europe.eu  # this is an example, update this field
hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
ingress:
  issuer: dev-prod
profile: < participant >

microservices:
ejbcaUrl: http://ejbca-community-helm.<namespace>.svc.cluster.local:30080
keycloakUrl: http://keycloak.<namespace>.svc.cluster.local
onboardingUrl: http://onboarding.<namespace>.svc.cluster.local:8080
securityAttributesProviderUrl: http://security-attributes-provider.<namespace>.svc.cluster.local:8080
usersRolesUrl: http://users-roles.<namespace>.svc.cluster.local:8080
```

##### Profiles

The value `global.profile` set `SPRING_PROFILES_ACTIVE`: This sets the active Spring profile. The value should be `participant`.

The value `global.authorityUrl` set `AUTHORITY_URL`: URL of the authority backend.

##### Common configuration:

The value `global.cors.allowOrigin` set `CORS_ALLOWED_ORIGINS`: Specifies which origins are allowed to make cross-origin requests.
The value `miroservices.keycloakUrl` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
The value `miroservices.usersRolesUrl` set `USERSROLES_URL`: The URL for the Users&Roles service.
`CORS_ALLOWED_HEADERS`: Specifies which HTTP headers are allowed in cross-origin requests.
Default value: `Access-Control-Allow-Headers, Access-Control-Allow-Credentials, Access-Control-Allow-Origin, Access-Control-Allow-Methods, Keep-Alive, User-Agent, Content-Type, Authorization, Tenant, Channel, Platform, Set-Cookie, geolocation, x-mobility-mode, device, Cache-Control, X-Request-With, Accept, Origin.`

#### User & Roles

##### Prerequisites

*simpl-cloud-gateway* up and running

*security-attribute-provider* up and running

#### Example of values.yaml

```yaml
env:
  KEYCLOAK_MASTER_PASSWORD: admin # this password was set in keycloak values.yaml
  KEYCLOAK_MASTER_USER: user
  SPRING_DATA_REDIS_HOST: redis-master.<namespace>.svc.cluster.local
  SPRING_DATA_REDIS_PASSWORD: admin
  SPRING_DATA_REDIS_PORT: "6379"
  SPRING_DATA_REDIS_USERNAME: default
  SPRING_DATASOURCE_PASSWORD: usersroles
  SPRING_DATASOURCE_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles
  SPRING_DATASOURCE_USERNAME: usersroles

global:
  hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
  hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
  keystore:
    password: < password defined in the oboarding component >
  profile: <participant>
```
##### Configuration

The environment variables listed below are used to define the connection details for PostgreSQL, Redis, Keycloak, and other services. For further configuration, view the Helm template and update the values as required.

**Database Configuration**

- `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to the PostgreSQL database. Format: `jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles`
- `SPRING_DATASOURCE_USERNAME`: The username for the PostgreSQL database.
- `SPRING_DATASOURCE_PASSWORD`: The password for the PostgreSQL database.

**Redis Configuration**

- `SPRING_DATA_REDIS_HOST`: The host address for the Redis service. Format: `redis-master.<namespace>.svc.cluster.local`
- `SPRING_DATA_REDIS_PORT`: The port on which Redis is running. Default value: `6379`
- `SPRING_DATA_REDIS_USERNAME`: The username for connecting to Redis.
- `SPRING_DATA_REDIS_PASSWORD`: The password for connecting to Redis.

**Keycloak Configuration**

- The value `global.hostBe` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
- The value `global.profile` set `KEYCLOAK_APP_REALM`: The realm to be used for the application within Keycloak.

**Client Authority Configuration**

- The value `global.hostTls` set `CLIENT_AUTHORITY_URL`: The URL for the client authority service.
- The value `global.keystore.password` set `CLIENT_CERTIFICATE_PASSWORD`: The password for the client certificate.

#### Frontend

##### Example of values.yaml

```yaml
hostFe: authority.fe.dev.simpl-europe.eu # this is an example, update this field
cors: # this is an example, update this field
  allowOrigin: https://authority.be.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:4203,http://localhost:3000
ingress:
  issuer: dev-prod

env:
- name: APPLICATION
  value: <participant-utility>
- name: API_URL
  value: "https://authority.be.dev.simpl-europe.eu" # this is an example, update this field
- name: KEYCLOAK_URL
  value: "https://authority.be.dev.simpl-europe.eu/auth" # this is an example, update this field
- name: KEYCLOAK_REALM
  value: "<participant>"
- name: KEYCLOAK_CLIENT_ID
  value: "frontend-cli"
```

##### Configuration

The configuration provides details on the backend and frontend host URLs, CORS allowed origins, ingress issuer, and environment variables for the onboarding application. For further configuration, view the Helm template and update the values as required.

**Frontend Host Configuration**

- `hostFe`: The hostname for the frontend service. Value: `my.frontend.host`

**CORS Configuration - Allowed Origins**

- `cors.allowOrigin`: Specifies the origins that are allowed to access the application resources via cross-origin requests.
  Value: `https://my.frontend.host, https://participant.fe.aruba-simpl.cloud, http://localhost:4202, http://localhost:4203, http://localhost:3000`

**Ingress Configuration - Issuer**

- `ingress.issuer`: The issuer for the ingress, which is typically used for managing TLS certificates. Value: `your-issuer-ingress`

**Environment Variables**

- `APPLICATION`: The name of the application. Value: participant-utility
- `API_URL`: The URL for the API backend. Value: `https://my.backend.host` **Keycloak Configuration**
- `KEYCLOAK_URL`: The URL for the Keycloak authentication service. Value: `https://my.backend.host/auth`
- `KEYCLOAK_REALM`: The Keycloak realm that the application uses for authentication. Value: `authority`
- `KEYCLOAK_CLIENT_ID`: The client ID used by the application to authenticate with Keycloak. Value: `frontend-cli`

### Step 2: Deploy the Application Using Helm Charts
Go to master charts directory:

`cd .\charts\`

Now you can deploy the namespace:

`helm install data-provider . `

:rotating_light: :rotating_light: :rotating_light: **Attention!!!** :rotating_light: :rotating_light: :rotating_light: <br>
<b><i>After installing the namespace, there are services that connect using the TLS protocol (e.g. EJBCA). In the current phase of application development, this element must be configured manually.
The entire procedure is described in confuence:</i></b>

https://confluence.simplprogramme.eu/display/SIMPL/EJBCA+Configuration

<b><i>For the namespace data-provider to work correctly, it is necessary to perform the actions described in the link above.</i></b>

## Change the namespace

The process of implementing changes is analogous to deploying the namespace for the first time:

`helm upgrade data-provider . `

## Delete the deployment:

To remove the deployment you need to do two things:

* `helm uninstall data-provider` - which will remove the application from argocd
* `kubectl delete ns ${NAMESPACE}` - which will remove the namespace ${NAMESPACE} that holds all of the components.

# Troubleshooting
If you encounter issues during deployment, check the following:

- Ensure that ArgoCD is properly set up and running.
- Verify that the data-provider namespace exists in your Kubernetes cluster.
- Check the ArgoCD application logs and Helm error messages for specific issues.

---

# Consumer Deployment

## Description

This repo contains:
- a master helm chart allowing to deploy a **Consumer** agent using a single command.
- templates of values.yaml files used inside *Integration* environment under `app-values` folder

## Prerequisites

Make sure you have installed the required tools from [Prerequisites](#prerequisites)

## Create the Namespace
Before deploying the application, ensure that the **consumer** (i.e. consumer) namespace exists in your Kubernetes cluster. If the expected namespace does not exist yet you can create it with the following steps:

### Step 1: Create the Namespace
Once the namespace variable is set, you can create the namespace using the following kubectl command:

`kubectl create namespace consumer1`

### Step 2: Verify the Namespace
To ensure that the namespace was created successfully, run the following command:

`kubectl get namespaces`
<br/>This will list all the namespaces in your cluster, and you should see the one you just created listed.

## Deploy the namespace
Deploying a dedicated namespace, such as **consumer1**, helps isolate resources and applications within a Kubernetes cluster.

Filling the namespace with content requires the following activity:

### Step 1: Modify YAML configuration files

The first step in configuring the application is to update the necessary YAML files. These files contain key values that define the application's environment, behavior, and settings.

#### Redis

##### Example of values.yaml
```yaml
replica:
  replicaCount: 0
architecture: standalone
```

#### Postgresql

##### Example of values-participant.yaml
```yaml
primary:
  initdb:
    scripts:
      init.sql: |
        CREATE USER keycloak WITH PASSWORD 'keycloak' CREATEDB;
        CREATE DATABASE keycloak OWNER keycloak;
        CREATE USER usersroles WITH PASSWORD 'usersroles' CREATEDB;
        CREATE DATABASE usersroles OWNER usersroles;
```
> **⚠️** The configuration examples use the users and passwords mentioned above. If you change them, ensure that your configuration reflects those changes accordingly.

#### Keycloak

##### Example of values.yaml
```yaml
apiUrl: "<participant endpoint>" # example: https://participant.be.aruba-simpl.cloud
                                  
extraEnvVars:
- name: KC_HOSTNAME_ADMIN_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: KC_HOSTNAME_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: USERS_ROLES_BASE_URL
  value: "http://users-roles.<namespace>.svc.cluster.local:8080" # update
- name: KEYCLOAK_BASE_URL
  value: "< apiUrl as above with /auth, example: https://participant.be.aruba-simpl.cloud/auth>" # update
- name: REALM
  value: participant
 
auth:
adminPassword: "admin"
 
keycloakConfigCli:
  enabled: true
  configuration:
    participant.json: |
      {{- $.Files.Get "kc-init/participant-realm-export.json" -}}
 
postgresql:
enabled: false
 
externalDatabase:
annotations: {}
database: keycloak
existingSecret: ""
existingSecretDatabaseKey: ""
existingSecretHostKey: ""
existingSecretPasswordKey: ""
existingSecretPortKey: ""
existingSecretUserKey: ""
host: "postgresql.<namespace>.svc.cluster.local"
password: keycloak
port: 5432
user: keycloak
```

#### SIMPL Cloud Gateway

##### Example of values.yaml

```yaml
global:
cors: # this is an example, update this field
  allowOrigin: https://authority.fe.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:3000
hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
hostFe: authority.fe.dev.simpl-europe.eu  # this is an example, update this field
hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
ingress:
  issuer: dev-prod
profile: < participant >

microservices:
ejbcaUrl: http://ejbca-community-helm.<namespace>.svc.cluster.local:30080
keycloakUrl: http://keycloak.<namespace>.svc.cluster.local
onboardingUrl: http://onboarding.<namespace>.svc.cluster.local:8080
securityAttributesProviderUrl: http://security-attributes-provider.<namespace>.svc.cluster.local:8080
usersRolesUrl: http://users-roles.<namespace>.svc.cluster.local:8080
```

##### Profiles

The value `global.profile` set `SPRING_PROFILES_ACTIVE`: This sets the active Spring profile. The value should be `participant`.

The value `global.authorityUrl` set `AUTHORITY_URL`: URL of the authority backend. 

##### Common configuration:
  
The value `global.cors.allowOrigin` set `CORS_ALLOWED_ORIGINS`: Specifies which origins are allowed to make cross-origin requests.
The value `miroservices.keycloakUrl` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
The value `miroservices.usersRolesUrl` set `USERSROLES_URL`: The URL for the Users&Roles service.
`CORS_ALLOWED_HEADERS`: Specifies which HTTP headers are allowed in cross-origin requests.
Default value: `Access-Control-Allow-Headers, Access-Control-Allow-Credentials, Access-Control-Allow-Origin, Access-Control-Allow-Methods, Keep-Alive, User-Agent, Content-Type, Authorization, Tenant, Channel, Platform, Set-Cookie, geolocation, x-mobility-mode, device, Cache-Control, X-Request-With, Accept, Origin.`

#### User & Roles

##### Prerequisites
    
*simpl-cloud-gateway* up and running

*security-attribute-provider* up and running

##### Example of values.yaml
  
```yaml
env:
  KEYCLOAK_MASTER_PASSWORD: admin # this password was set in keycloak values.yaml
  KEYCLOAK_MASTER_USER: user
  SPRING_DATA_REDIS_HOST: redis-master.<namespace>.svc.cluster.local
  SPRING_DATA_REDIS_PASSWORD: admin
  SPRING_DATA_REDIS_PORT: "6379"
  SPRING_DATA_REDIS_USERNAME: default
  SPRING_DATASOURCE_PASSWORD: usersroles
  SPRING_DATASOURCE_URL: jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles
  SPRING_DATASOURCE_USERNAME: usersroles

global:
  hostBe: authority.be.dev.simpl-europe.eu  # this is an example, update this field
  hostTls: tls.authority.dev.simpl-europe.eu  # this is an example, update this field
  keystore:
    password: < password defined in the oboarding component >
  profile: <participant>
```
##### Configuration
    
The environment variables listed below are used to define the connection details for PostgreSQL, Redis, Keycloak, and other services. For further configuration, view the Helm template and update the values as required.

**Database Configuration**

  - `SPRING_DATASOURCE_URL`: The JDBC URL for connecting to the PostgreSQL database. Format: `jdbc:postgresql://postgresql.<namespace>.svc.cluster.local:5432/usersroles`
  - `SPRING_DATASOURCE_USERNAME`: The username for the PostgreSQL database.
  - `SPRING_DATASOURCE_PASSWORD`: The password for the PostgreSQL database.

**Redis Configuration**

  - `SPRING_DATA_REDIS_HOST`: The host address for the Redis service. Format: `redis-master.<namespace>.svc.cluster.local`
  - `SPRING_DATA_REDIS_PORT`: The port on which Redis is running. Default value: `6379`
  - `SPRING_DATA_REDIS_USERNAME`: The username for connecting to Redis.
  - `SPRING_DATA_REDIS_PASSWORD`: The password for connecting to Redis.

**Keycloak Configuration**

  - The value `global.hostBe` set `KEYCLOAK_URL`: The URL for the Keycloak authentication service.
  - The value `global.profile` set `KEYCLOAK_APP_REALM`: The realm to be used for the application within Keycloak.

**Client Authority Configuration**

  - The value `global.hostTls` set `CLIENT_AUTHORITY_URL`: The URL for the client authority service.
  - The value `global.keystore.password` set `CLIENT_CERTIFICATE_PASSWORD`: The password for the client certificate.

#### Frontend

##### Example of values.yaml

```yaml
hostFe: authority.fe.dev.simpl-europe.eu # this is an example, update this field
cors: # this is an example, update this field
  allowOrigin: https://authority.be.dev.simpl-europe.eu,https://authority.fe.dev.simpl-europe.eu,http://localhost:4202,http://localhost:4203,http://localhost:3000
ingress:
  issuer: dev-prod

env:
- name: APPLICATION
  value: <participant-utility>
- name: API_URL
  value: "https://authority.be.dev.simpl-europe.eu" # this is an example, update this field
- name: KEYCLOAK_URL
  value: "https://authority.be.dev.simpl-europe.eu/auth" # this is an example, update this field
- name: KEYCLOAK_REALM
  value: "<participant>"
- name: KEYCLOAK_CLIENT_ID
  value: "frontend-cli"
```

##### Configuration

The configuration provides details on the backend and frontend host URLs, CORS allowed origins, ingress issuer, and environment variables for the onboarding application. For further configuration, view the Helm template and update the values as required.

**Frontend Host Configuration**

- `hostFe`: The hostname for the frontend service. Value: `my.frontend.host`
      
**CORS Configuration - Allowed Origins**

- `cors.allowOrigin`: Specifies the origins that are allowed to access the application resources via cross-origin requests.
  Value: `https://my.frontend.host, https://participant.fe.aruba-simpl.cloud, http://localhost:4202, http://localhost:4203, http://localhost:3000`

**Ingress Configuration - Issuer**

- `ingress.issuer`: The issuer for the ingress, which is typically used for managing TLS certificates. Value: `your-issuer-ingress`

**Environment Variables**

- `APPLICATION`: The name of the application. Value: participant-utility
- `API_URL`: The URL for the API backend. Value: `https://my.backend.host` **Keycloak Configuration**
- `KEYCLOAK_URL`: The URL for the Keycloak authentication service. Value: `https://my.backend.host/auth`
- `KEYCLOAK_REALM`: The Keycloak realm that the application uses for authentication. Value: `authority`
- `KEYCLOAK_CLIENT_ID`: The client ID used by the application to authenticate with Keycloak. Value: `frontend-cli`

### Step 2: Deploy the Application Using Helm Charts
Go to master charts directory:

`cd .\charts\`

Now you can deploy the namespace:

`helm install consumer . `

:rotating_light: :rotating_light: :rotating_light: **Attention!!!** :rotating_light: :rotating_light: :rotating_light: <br>
<b><i>After installing the namespace, there are services that connect using the TLS protocol (e.g. EJBCA). In the current phase of application development, this element must be configured manually.
The entire procedure is described in confuence:</i></b>

https://confluence.simplprogramme.eu/display/SIMPL/EJBCA+Configuration

<b><i>For the namespace consumer to work correctly, it is necessary to perform the actions described in the link above.</i></b>

## Change the namespace

The process of implementing changes is analogous to deploying the namespace for the first time:

`helm upgrade consumer . `

## Delete the deployment:

`helm uninstall consumer .`


# Troubleshooting
If you encounter issues during deployment, check the following:

- Ensure that ArgoCD is properly set up and running.
- Verify that the consumer namespace exists in your Kubernetes cluster.
- Check the ArgoCD application logs and Helm error messages for specific issues.
