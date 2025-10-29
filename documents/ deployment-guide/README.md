# Common Components Agent

<!-- TOC -->
- [Common Components Agent](#common-components-agent)
  - [Description](#description)
  - [Prerequisites](#prerequisites)
    - [Tools](#tools)
    - [DNS entries](#dns-entries)  
  - [Deployment](#deployment)
    - [Deployment using ArgoCD](#deployment-using-argocd)
    - [Manual deployment](#manual-deployment)
      - [Files preparation](#files-preparation)
      - [Deployment](#deployment-1)
  - [Additional steps and remarks](#additional-steps-and-remarks)
    - [Init-bao job issues](#init-bao-job-issues)
    - [Failing pod restart](#failing-pod-restart)
    - [Monitoring](#monitoring)
    - [Vault Configuration](#vault-configuration)
  - [Troubleshooting](#troubleshooting)
<!-- TOC -->

## Description
This project contains the configuration files required for deploying an application using Helm and ArgoCD. 
- the deployment will be done by master helm chart allowing to deploy **Common components** using a single command.
- templates of values.yaml files used inside *Integration* environment under `app-values` folder

## Prerequisites

Ensure you have the following tools installed before starting the deployment process:
- Git
- Helm
- Kubectl

Additionally, ensure you have access to a Kubernetes cluster where ArgoCD is installed.

### Tools

The following versions of the elements will be used in the process:

| Pre-Requisites         |     Version     | Description                                                                                                                                     |
| ---------------------- |     :-----:     | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| DNS sub-domain name    |       N/A       | This domain will be used to address all services of the agent. <br/> example: `*.common01.example.com` | 
| external-dns    | bitnami/external-dns:0.16.1 | Currently version docker.io/bitnami/external-dns:0.16.1-debian-12-r should be used as externaldns. Unfortunately, using a newer version caused DNS to work incorrectly. |  
| Kubernetes Cluster     | 1.29.x or newer | Other version *might* work but tests were performed using 1.29.x version                                                                        |
| nginx-ingress          | 1.10.x or newer | Used as ingress controller. <br/> Other version *might* work but tests were performed using 1.10.x version. <br/> Image used: `registry.k8s.io/ingress-nginx/controller:v1.10.0`  |
| argocd                 | 2.11.x or newer | Used as GitOps tool . App of apps concept. <br/> Other version *might* work but tests were performed using 2.11.x version. <br/> Image used: `quay.io/argoproj/argocd:v2.11.3` |
| kube-state-metrics  | 2.13.x or newer | Used for monitoring, Metricbeat statuses in Kibana dashboard    |
| cert-manager           | 1.15.x or newer | Used for automatic cert management. <br/> Other version *might* work but tests were performed using 1.15.x version. <br/> Image used: `quay.io/jetstack/cert-manager-controller:v1.15.3` |
| cluster issuer for selfsigned certificates |       N/A       | A cluster issuer needs to be created to create self-signed certificates. It's used for monitoring only. Name should be supplied in cluster.internalIssuer variable |

### DNS entries 

| Entry Name | Entries |
| ------------- | --------------------------------------------------------------------------------------------------- |
| elastic-apm-server | apm.(namespace).(domainSuffix) |
| elastic-elasticsearch-http| elastic-elasticsearch-es-http.(namespace).svc
| elastic-elasticsearch-http-public	 | elasticsearch.(namespace).(domainSuffix) |
| elastic-kibana-dashboard | kibana.(namespace).(domainSuffix) | 
| elastic-otel-collector | collector.(namespace).(domainSuffix) |
| logstash-api-beats | logstash.beats.(namespace).(domainSuffix) |
| mailpit-(namespace)	 | mailpit.(namespace).(domainSuffix) |
| pg-admin-(namespace)		 | pgadmin.(namespace).(domainSuffix) |
| redpanda	 | redpanda.(namespace).(domainSuffix) |
| vault	 | vault.(namespace).(domainSuffix) |

## Deployment

### Deployment using ArgoCD

You can easily deploy the agent using ArgoCD. All the values mentioned in the sections below you can input in ArgoCD deployment. The repoURL gets the package directly from code.europa.eu.
"targetRevision" is the package version. 

In the example below, please replace the marked versions with the ones applicable to your environment.

Please pay special attention to the namespace names: common01, authority01, consumer01 and dataprovider01, and also to replace the domain name example.com and the occurrence of the example value itself.

```YAML
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: 'common01-deployer'                          # name of the deploying app in argocd
spec:
  project: default
  source:
    repoURL: 'https://code.europa.eu/api/v4/projects/951/packages/helm/stable'
    path: '""'
    targetRevision: 2.3.1                          # version of package
    helm:
      values: |
        values:
          branch: v2.3.1                            # branch of repo with values
        resourcePreset: default                     # set to "low" to disable requests of resources
        agentList:                                  # list of all the agents to be deployed
          authorities:
            - authority01
          consumers:
            - consumer01
          providers:
            - dataprovider01
        project: default                            # Project to which the namespace is attached
        namespaceTag: common01                      # identifier of deployment and part of fqdn
        domainSuffix: example.com                   # last part of fqdn
        argocd:
          appname: common01                         # name of generated argocd app 
          namespace: argocd                         # namespace of your argocd
        cluster:
          address: https://kubernetes.default.svc
          namespace: common01                       # where the app will be deployed
          issuer: dev-prod                          # issuer of certificate
          internalIssuer: dev-selfsigned            # issuer for self-signed certificates, for monitoring stack
          kubeStateHost: kube-prometheus-stack-kube-state-metrics.devsecopstools.svc.cluster.local:8080    # link to kube-state-metrics svc
        secrets:
          secretEngine: example                     # name of the kv secret engine that will be created in vault
          role: example-role                        # name of the role that will be created in vault
        kafka:
          ha: true                                  # true creates 3 replicas of each component, false creates 1 of each
          topic:
            autocreate: true                        # set to true if kafka should automatically create topics
        mailpit:
          enabled: true                             # set to true if mailpit should be deployed as mock smtp for notification service
        monitoring:
          enabled: true                             # should monitoring be enabled
    chart: common_components                        # chart name
  destination:
    server: 'https://kubernetes.default.svc'
    namespace: common01                             # where the package will be deployed

```

### Manual deployment

#### Files preparation

Another way for deployment, is to unpack the released package to a folder on a host where you have kubectl and helm available and configured. 

There is basically one file that you need to modify - values.yaml. 
There are a couple of variables you need to replace - described below. The rest you don't need to change.

```YAML
values:
  branch: v2.3.1                            # branch of repo with values
resourcePreset: default                     # set to "low" to disable requests of resources
agentList:                                  # list of all the agents to be deployed
  authorities:
    - authority01
  consumers:
    - consumer01
  providers:
    - dataprovider01
project: default                            # Project to which the namespace is attached
namespaceTag: common01                      # identifier of deployment and part of fqdn
domainSuffix: example.com                   # last part of fqdn
argocd:
  appname: common01                         # name of generated argocd app 
  namespace: argocd                         # namespace of your argocd
cluster:
  address: https://kubernetes.default.svc
  namespace: common01                       # where the app will be deployed
  issuer: dev-prod                          # issuer of certificate
  internalIssuer: dev-selfsigned            # issuer for self-signed certificates, for monitoring stack
  kubeStateHost: kube-prometheus-stack-kube-state-metrics.devsecopstools.svc.cluster.local:8080    # link to kube-state-metrics svc
secrets:
  secretEngine: example                     # name of the kv secret engine that will be created in vault
  role: example-role                        # name of the role that will be created in vault
kafka:
  ha: true                                  # true creates 3 replicas of each component, false creates 1 of each
  topic:
    autocreate: true                        # set to true if kafka should automatically create topics
mailpit:
  enabled: true                             # set to true if mailpit should be deployed as mock smtp for notification service
monitoring:
  enabled: true                             # should monitoring be enabled
```

#### Deployment

After you have prepared the values file, you can start the deployment. 
Use the command prompt. Proceed to the folder where you have the Chart.yaml file and execute the following command. The dot at the end is crucial - it points to current folder to look for the chart. 

Now you can deploy the agent:

`helm install common . `


After starting the deployment synchronization process, the expected namespace will be created.


Initially, the status observed e.g. in ArgoCD will indicate the creation of new pods:

<img src="../images/ArgoCD_01.png" alt="ArgoCD_01" width="600"><BR>

Be patient!... Depending on the configuration, this step can take up to 30 minutes!

At the end, all pods should be created correctly:

<img src="../images/ArgoCD_02.png" alt="ArgoCD_02" width="600"><BR>

## Additional steps and remarks

### Init-bao job issues

Ocassionaly, the init-bao job might go ahead with creating secrets, despite open-bao secret engine not being available. This creates empty secrets, which might cause components to fail.

<img src="../images/Initbao.png" alt="Initbao" width="400"><BR>

in case this happens, the secrets must be deleted and then the job has to be restarted if it has ran out of tries. 

These secrets have to be deleted:

secrets-root-token<BR>
secrets-unseal-keys

### Failing pod restart

If failing. these two pods need to be restarted after OpenBao is up. They rely on information from OpenBao and may be up before it is up. 

<img src="../images/Podstodelete.png" alt="Podstodelete" width="400"><BR>

Although it's rare, it might happen more than once so retry the following steps if init-bao is failing again.

### Monitoring

ELK stack for monitoring is added with this release.  
Its deployment can be disabled by switch the value monitoring.enabled to false.  
When it's enabled, after the stack is deployed, you can access the ELK stack UI by <https://kibana.**namespacetag**.**domainSuffix**>
Default user is "elastic", its password can be extracted by kubectl command. `kubectl get secret elastic-elasticsearch-es-elastic-user -o go-template='{{.data.elastic | base64decode}}' -n {namespace}`

### Vault Configuration

The description of configuring and using vault is in a separate document:
https://code.europa.eu/simpl/simpl-open/development/agents/common_components/-/blob/main/documents/Using_Vault.md

Please read this document before proceeding to install and configure other agents (namespaces).

## Troubleshooting

If you encounter issues during deployment, check the following:

- Ensure that ArgoCD is properly set up and running.
- Verify that the namespace exists in your Kubernetes cluster.
- Check the ArgoCD application logs and Helm error messages for specific issues.
