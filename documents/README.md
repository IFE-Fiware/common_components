# SIMPL-Open Middleware : Common Components Deployment

<!-- TOC -->
- [SIMPL-Open Middleware : Common Components Deployment](#simpl-open-middleware-common-components-deployment)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
  - [DNS entries](#dns-entries)
  - [Installation](#installation)
    - [Graphical deployment using ArgoCD](#graphical-deployment-using-argocd)
    - [Monitoring](#monitoring)
    - [HashiCorp Vault Configuration](#hashicorp-vault-configuration)
    - [Redis Commander](#redis-commander)
    - [Trouble shooting](#trouble-shooting)
<!-- /TOC -->

## Description

This project contains the configuration files required to deploy SIMPL-Open Middleware Common Components.  The Common Components are the basis required by all the others SIMPL-Open Middleware agents.  Two deployment methods are documented here under :

- manual deployment using command line tools such as Helm and kubectl.
- ArgoCD deployment using mainly graphical interface

The deployment is performed using master helm chart deploying the SIMPL-Open Middleware _Common components_ in one step.  The master helm chart requires a value file for the deployment, here under you will find an example of the master value chart, please be aware that many values must be replaced to be aligned with your environment.  These values are explained by inline comment in the values file of the master helm chart example.  The values file of each common components could found in te app-values folder of the source code repository.

## Prerequisites

The following versions of the common components will be used during the deployment process

| Prerequisites         |     Version     | Description                                                                                                                                     |
| ---------------------- |     :-----:     | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| DNS sub-domain name    |       N/A       | This domain will be used to address all services of the agent. <br> example: `*.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME>` |
| external-dns    | bitnami/external-dns:0.16.1 | Currently version docker.io/bitnami/external-dns:0.16.1-debian-12-r should be used as externaldns. Unfortunately, using a newer version caused DNS to work incorrectly. |
| Kubernetes Cluster     | 1.29.x or newer | Other version _might_ work but tests were performed using 1.29.x version                                                                        |
| nginx-ingress          | 1.10.x or newer | Used as ingress controller. <br> Other version _might_ work but tests were performed using 1.10.x version. <br> Image used: `registry.k8s.io/ingress-nginx/controller:v1.10.0`  |
| cert-manager           | 1.15.x or newer | Used for automatic cert management. <br> Other version _might_ work but tests were performed using 1.15.x version. <br> Image used: `quay.io/jetstack/cert-manager-controller:v1.15.3` |
| argocd                 | 2.11.x or newer | Used as GitOps tool . App of apps concept. <br> Other version _might_ work but tests were performed using 2.11.x version. <br> Image used: `quay.io/argoproj/argocd:v2.11.3` |
| kube-state-metrics  | 2.13.x or newer | Used for monitoring, Metricbeat statuses in Kibana dashboard    |

## DNS entries

The following DNS records will be automatically created by external dns if it is properly configured.  These records could also be manually created however this is not recommended due to potential regular update which will not be easy to maintian manually.

| Entry Name | Entries |
| ---------- | ------- |
| elastic-apm-server | apm.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| elastic-elasticsearch-http| elastic-elasticsearch-es-http.<YOUR_KUBERNETES_NAME_SPACE>.svc |
| elastic-elasticsearch-http-public | elasticsearch.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| elastic-kibana-dashboard | kibana.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| elastic-otel-collector | collector.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| logstash-api-beats | logstash.beats.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| mailpit-<YOUR_KUBERNETES_NAME_SPACE> | mailpit.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| pg-admin-<YOUR_KUBERNETES_NAME_SPACE> | pgadmin.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| redis-commander | redis-commander.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| redpanda | redpanda.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |
| vault | vault.<YOUR_KUBERNETES_NAME_SPACE>.<YOUR-DNS-FULL-QUALIFIED-DOMAIN-NAME> |

## Installation

Two methods are 2 explained here under to deploy the SIMPL-Open Middleware Common Components :
- a graphical interface one using ArgoCD
- a command line one using helm and kubectl

### Graphical deployment using ArgoCD

All the values mentioned in the sections below you can input in ArgoCD deployment. The repoURL gets the package directly from code.europa.eu.
"targetRevision" is the package version.

In the example below, please replace the marked versions with the ones applicable to your environment.

Please pay special attention to the namespace names: common03, authority03, consumer03 and dataprovider03, and also to replace the domain name testint.simpl-europe.eu and the occurrence of the testint value itself.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  doc: name of the currently deploying app in argocd, this is the name that will be displayed in ArgoCD
  name: 'common03-deployer'
spec:
  project: default
  source:
    repoURL: 'https://code.europa.eu/api/v4/projects/951/packages/helm/stable'
    path: '""'
    doc: version of package, must be aligned with code version that we want to install
    targetRevision: v2.1.1
    helm:
      values: |
        values:
          doc: Branch of the code repo which the value must be aligned with targetRevision
          branch: v2.1.1
        doc: resourcePreset set to "low" to disable requests of resources
        resourcePreset: default
        # List of all the SIMPL-Open MiddleWare agents that will be deployed on top of the current Common Tools Deployment                      
        agentList:
          authorities:
            # Name of the kubernetes NameSpace that will have to be used to deploy the Governance Authority
            - authority03
          consumers:
            # Name of the kubernetes NameSpace that will have to be used to deploy the Data Consumers
            - consumer03
          providers:
            # Name of the kubernetes NameSpace that will have to be used to deploy the Data Providers
            - dataprovider03
        project: default
        # Name of the kubernetes NameSpace in which the Common components will be deployed, this will be also part of the FQDN Fully Qualified Domain Name
        namespaceTag: common03
        # last part of FQDN Fully Qualified Domain Name
        domainSuffix: uat.simpl-europe.eu
        argocd:
          # Name of the object which will be displayed in ArgoCD
          appname: common03
          # Name of the Kubernetes NameSpace that your ArgoCD is running in
          namespace: argocd
        cluster:
          # FQDN Fully Qualified Domain Name of your kubernetes cluster
          address: https://kubernetes.default.svc
          # Name of the Kubernetes NameSpace in which the application will be deployed
          namespace: common03
          # Issuer of the certificate used by cert manager
          issuer: dev-prod
          # url to access prometheus instance
          kubeStateHost: kube-prometheus-stack-kube-state-metrics.devsecopstools.svc.cluster.local:8080
        hashicorp:
          # Name of the key value secret engine that will be created in HashiCorp Vault
          secretEngine: test-uat
          # Name of the role that will be created in HashiCorp Vault
          role: test-uat-role
        kafka:
          topic:
            # set this value to true, to have kafka creating automatically the required topics
            autocreate: true
        mailpit:
          # set this value to true, to have mailpit activated
          enabled: true
        monitoring:
          # set this value to true, to enable the monitoring features
          enabled: true
    # Name of the helm chart to deploy
    chart: common_components
  destination:
    # FQDN Fully Qualified Domain Name of your kubernetes cluster
    server: 'https://kubernetes.default.svc'
    # Name of the Kubernetes NameSpace in which the Common Tools will be deployed
    namespace: common03
```
Be patient!... Depending on the your kubernetes configuration and resources availalbe, the deployment of the Common Tools could take more than 30 minutes.

<!-- JOEL HERE -->

After starting the deployment synchronization process, the expected namespace will be created.

Initially, the status observed e.g. in ArgoCD will indicate the creation of new pods:

<img src="images/ArgoCD_01.png" alt="ArgoCD_01" width="600"><BR>

At the end, all pods should be created correctly:

<img src="images/ArgoCD_02.png" alt="ArgoCD_02" width="600"><BR>

### Monitoring

The Elastic Stack (open source version) is used to monitor the the SIMPL-Open MiddleWare. Its deployment is conditionned to the flag monitoring.enabled which required a true/false value.
When it's true, the Elastic Stack is deployed, and Kibana can be accessed at the following url <https://kibana.**namespacetag**.**domainsuffix**>
The default user is "elastic", its password can be obtained by running the following kubectl command. `kubectl get secret elastic-elasticsearch-es-elastic-user -o go-template='{{.data.elastic | base64decode}}' -n {namespace}`

### HashiCorp Vault Configuration

The description of configuring and using vault is in a separate document:
<https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/Using_Vault.md>

Please read this document before proceeding to install and configure other SIMPL-OPEN agents(namespaces).

### Redis Commander

Redis commander is a frontend allowing to visualisa the data stored in redis-master

![Redis_commander](images/RedisCommander.png)

The password for redis commander is stored in a HashiCopr Vault Secret in the vaut "common-redis secret".

Note!!! To log in, we use the password stored in the "rediscommander" variable, but as a username, we should enter "admin" and not "rediscommander"!

<img src="images/Redis01.png" alt="Redis012" width="400"><BR>
<img src="images/Redis02.png" alt="Redis02" width="400"><BR>

### Trouble shooting
