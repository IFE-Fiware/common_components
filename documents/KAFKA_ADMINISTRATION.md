# Kafka administration

### Overview

Common Components repo includes three components that are used as Kafka stack. Those are:
* Confluent Operator, provided by a chart *confluent-for-kubernetes* from https://packages.confluent.io/helm
* Kafka stack, from repository https://code.europa.eu/simpl/simpl-open/development/common-components/kafka
* Redpanda Console, an open source UI, provided by a chart *console* from https://charts.redpanda.com

Redpanda console serves as an UI to administer the Kafka stack. 

### Kafka configuration

There are a couple options you can set in Kafka deployment. Below you can find a table explaining them:

| Variable name              | Default value | Description     |
| ----------------------     | :-----:       | --------------- |
| kafka.replicas             | 3             | Count of Kafka replicas |
| kafka.topic.replicas       | 2             | Number of requested topic replicas |
| kafka.topic.insyncreplicas | 1             | Number of topic replicas for topic to be shown as in sync |
| kraftController.replicas   | 3             | Count of Kraft Controller replicas |
| kafka.auth.enabled         | true          | Should kafka SASL PLAIN authentication be enabled |
| kafka.topic.autocreate     | false         | Should topics be automatically created if they don't exist |

If kafka.auth.enabled is set as true, you need to have the Secret created in Vault. Secret creation is described in "Secret for Kafka" section in the README.md file. 

### Redpanda Console

#### Console access

You can access the console by going to https url redpanda.*namespaceTag*.*domainSuffix*

The *italic* values above are based on values.yaml file. Also in the values file, or by overwriting the values, you can set the username and password for accessing the console. Default is admin / admin. 

| Variable name                 |     Default value         | Description     |
| ----------------------        |     :-----:         | --------------- |
| redpanda.credentials.username | admin        | Username for Redpanda Console |
| redpanda.credentials.password | admin        | Password for Redpanda Console |

#### Console overview

After accessing the website above and entering the credentials set up with values, you will see the following screen.

![Init](images/RedpandaMain.png)

Using the menu on the right, you'll be able to see topics,

![Init](images/RedpandaTopics.png)

Consumer groups, etc. 

![Init](images/RedpandaConsumerGroups.png)