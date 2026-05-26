# Common Components — Helm CLI Deployment

## Document Information

| | |
|---|---|
| **Scope** | Instructions for deploying the SIMPL-Open Middleware Common Components from the command line using Helm and kubectl. |
| **Audience** | Platform engineers and DevOps engineers with shell access to a host configured with Helm and kubectl. |

---

> For deployment through the ArgoCD graphical interface, see [ARGOCD_DEPLOYMENT.md](ARGOCD_DEPLOYMENT.md).

## Prerequisites

Before proceeding, ensure the following requirements are met:

- **Helm 3.x** is installed. See <https://helm.sh/>.
- **kubectl** is installed and configured to communicate with the target Kubernetes cluster. See <https://kubernetes.io/docs/reference/kubectl/>.
- The target Kubernetes cluster meets the version and tooling requirements listed in the [main deployment guide](README.md#tools).
- **ArgoCD** is installed. See <https://argo-cd.readthedocs.io/en/stable/>.

> **ArgoCD** is still required, because the manual deployment only bypasses adding the Deployer app through ArgoCD UI. ArgoCD is still necessary for deployment. The chart used in this repo still is an ArgoCD App-of-Apps generator, not a standalone Helm chart.

## Deployment Procedure

### Step 1 — Prepare the values file

Unpack the released Helm chart package to a local directory on a host where `kubectl` and `helm` are available and configured.

The primary file to modify is `values.yaml`. Replace the placeholder values listed in the table below with values specific to your environment; other fields can remain at their defaults.

> **WARNING — All values below are example placeholders.**
> They **MUST** be replaced with values specific to your environment before deploying. Deploying with the example values as-is will fail or produce an incorrect configuration.

> **Important:** Agent names in the `agentList` value list **cannot** contain the `-` (hyphen) character.

### Values that must be replaced

| Value in example | Field(s) | What to set |
|---|---|---|
| `<common-namespace>` | `namespaceTag`, `argocd.appname`, `cluster.namespace` | Your chosen namespace identifier for common components |
| `<authority-namespace>`, `<consumer-namespace>`, `<dataprovider-namespace>` | `agentList` entries | The actual namespace identifiers of each agent to be deployed |
| `<your-domain>` | `domainSuffix` | Your actual domain name |
| `default` | `project` | The ArgoCD project to which this deployment belongs |
| `v3.1.2` | `values.branch` | The Git branch corresponding to your release version |
| `example` | `secrets.secretEngine` | The name of the KV secret engine configured in your OpenBao |
| `example-role` | `secrets.role` | The name of the role configured in your OpenBao |
| `dev-prod` | `cluster.issuer` | Your certificate issuer name |
| `dev-selfsigned` | `cluster.internalIssuer` | Your internal/self-signed certificate issuer name |
| `kube-prometheus-stack-kube-state-metrics.devsecopstools.svc.cluster.local:8080` | `cluster.kubeStateHost` | The service address of kube-state-metrics in your cluster |

### Example values.yaml

```yaml
values:
  branch: v3.1.2                               # branch of repo with values
resourcePreset: default                        # set to "low" to disable requests of resources
agentList:                                     # list of all the agents to be deployed
  authorities:
    - <authority-namespace>
  consumers:
    - <consumer-namespace>
  providers:
    - <dataprovider-namespace>
project: default                               # project to which the namespace is attached
namespaceTag: <common-namespace>               # identifier of deployment and part of fqdn
domainSuffix: <your-domain>                    # last part of fqdn
argocd:
  appname: <common-namespace>                  # name of generated argocd app
  namespace: argocd                            # namespace of your argocd
cluster:
  address: https://kubernetes.default.svc
  namespace: <common-namespace>                # where the app will be deployed
  issuer: dev-prod                             # issuer of certificate
  internalIssuer: dev-selfsigned               # issuer of self-signed certificates
  kubeStateHost: kube-prometheus-stack-kube-state-metrics.devsecopstools.svc.cluster.local:8080
secrets:
  secretEngine: example                        # name of the kv secret engine that will be created in OpenBao
  role: example-role                           # name of the role that will be created in OpenBao
kafka:
  ha: true                                     # true creates 3 replicas of each component, false creates 1 of each
  topic:
    autocreate: true                           # set to true if kafka should automatically create topics
mailpit:
  enabled: true                                # set to true to enable the Mailpit app deployment as mock SMTP server
monitoring:
  enabled: true                                # set to true to enable the monitoring features
pg_admin:
  enabled: true                                # set to true to enable the Postgres Admin app deployment
pg_cluster:
  ha: true                                     # set to false to have one replica of Postgres to save resources
openbao:
  ha: true                                     # set to false to have one replica of OpenBao to save resources
```

To limit the resource usage you can switch the following keys to those values:

| Field | What to set | Description |
|---|---|---|
| `resourcePreset` | `low` | Disables requests for CPU and MEM |
| `kafka.ha` | `false` | Switches from 3 replicas of Kafka to 1 | 
| `pg_cluster.ha` | `false` | Switches from 3 replicas of Postgres to 1 |
| `openbao.ha` | `false` | Switches from 3 replicas of OpenBao to 1 |

Also, additionally to what is described in the snippet above, all of the following apps deployment can be disabled, but it will affect out-of-the-box functionality. 
To do so, add the following keys to with value "false" in spec.source.helm.values:

| Field | Description |
|---|---|
| `openbao.enabled` | Disable OpenBao |
| `openbao_init.enabled` | Disable OpenBao unseal scripts |
| `openbao_config.enabled` | Disable OpenBao config scripts |
| `vault_webhook.enabled` | Disable webhook pulling passwords from OpenBao |
| `confluent_operator.enabled` | Disable Kafka operator |
| `kafka.enabled` | Disable Kafka |
| `pg_operator.enabled` | Disable Postgres Operator |
| `pg_cluster.enabled` | Disable Postgres Cluster |
| `infrastructure_consumption_monitoring_service.enabled` | Disable Infrastructure Consumption Monitoring Service |

### Step 2 — Run the Helm install command

Navigate to the directory containing the `Chart.yaml` file and execute:

```bash
helm install common .
```

> **Important:** The trailing `.` is required — it tells Helm to use the chart definition in the current directory.

After starting the deployment, the expected namespace will be created and resources will begin synchronising. Depending on your cluster configuration, this step can take **more than 30 minutes**.

## Verification

After the deployment has completed, verify that all resources are healthy:

1. Confirm the Helm release is deployed:
   ```bash
   helm list -n <common-namespace>
   ```

2. Verify that all pods are running:
   ```bash
   kubectl get pods -n <common-namespace>
   ```
   All pods should report a `Running` or `Completed` status. Investigate any pods in `CrashLoopBackOff`, `Error`, or `Pending` states.

3. Review pod logs for any pod that is not healthy:
   ```bash
   kubectl logs <pod-name> -n <common-namespace>
   ```

## See Also

- [Common Components Deployment Overview](README.md)
- [ArgoCD UI Deployment Guide](ARGOCD_DEPLOYMENT.md)
