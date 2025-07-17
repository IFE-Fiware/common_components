### Using Vault

In our project, we use Vault to increase security in different namespaces. Vault is a powerful tool for managing secrets, such as passwords, tokens, and encryption keys.
Additionally, our environment has been enriched with the vault-secrets-webhook module, which facilitates integration between Vault and our application.

Applications retrieve all necessary passwords, keys, and tokens from Vault based on the appropriate definitions contained in the application.yaml file.


**_IMPORTANT_**: **dataprovider_namespace**-gitea secret is not in use as Gitea credential yet.

Example entries in Vaults look like this:

![Vault view](images/vault1.png)

**_As an update from previous version, most of the Vault configuration is now applied automatically.
You just need to create a key for Signer and update a couple of values, which is mentioned in other agents readmes._**

**_All the credentials (for Keycloak and other components) are also now automatically stored in Vault - review the secrets for credentials if needed._**

You can access vault on https://vault.**namespacetag**.**domainsuffix**

we can always check the actual address in rancher:

<img src="images/Rancher03.png" alt="Rancher03" width="600"><BR>

Root token can be found in secret vault-unseal-keys, in key vault-root. 

<img src="images/Rancher01.png" alt="Rancher01" width="600"><BR>
<img src="images/Rancher02.png" alt="Rancher02" width="600"><BR>
<img src="images/Vault_02.png" alt="Vault_02" width="400"><BR>

The application retrieves them according to the following configuration:

![kafka-credentials view](images/kafka-credentials1.png)

The above configuration ensures that passwords and other secrets are generated securely and managed efficiently, reducing the risk of security breaches and simplifying the management of secrets across namespaces.


