# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DatabricksIntegrationAccountAuthenticationUpdate(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication for updating the Databricks integration account. Exactly one method is set. Choosing ``private_action_runner`` leaves the ``databricks-model-serving-metrics`` dataflow unable to collect data. ``bearer_token`` is deprecated on Databricks: it is accepted only on accounts that already use it and never on creation, so it cannot move an account onto token authentication. Migrate those accounts to ``databricks_oauth`` or ``private_action_runner``.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountOAuthAuthType

        :param azure_tenant_id: Microsoft Entra ID tenant of the service principal, for Azure Databricks workspaces. Omit it to keep the stored tenant, send `null` or an empty string to remove it, or send a value to replace it.
        :type azure_tenant_id: str, none_type, optional

        :param client_id: Client ID of the Databricks service principal.
        :type client_id: str, optional

        :param client_secret: Secret of the Databricks service principal. Generate it under User management > Service principals > Credentials & secrets in Databricks.
        :type client_secret: str, optional

        :param connection_id: Unique identifier of the Private Action Runner connection holding the credentials.
        :type connection_id: UUID, optional

        :param secret_path: Path of the credential inside the secret backend configured on the runner. Omit it to keep the stored path, send `null` or an empty string to remove it, or send a value to replace it.
        :type secret_path: str, none_type, optional

        :param user_uuid: Unique identifier of the user the Private Action Runner connection belongs to.
        :type user_uuid: UUID, optional

        :param token: Secret token used to authenticate with Databricks.
        :type token: str, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_update import (
            DatabricksIntegrationAccountOAuthAuthUpdate,
        )
        from datadog_api_client.v2.model.databricks_integration_account_private_action_runner_auth_update import (
            DatabricksIntegrationAccountPrivateActionRunnerAuthUpdate,
        )
        from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_update import (
            DatabricksIntegrationAccountBearerTokenAuthUpdate,
        )

        return {
            "oneOf": [
                DatabricksIntegrationAccountOAuthAuthUpdate,
                DatabricksIntegrationAccountPrivateActionRunnerAuthUpdate,
                DatabricksIntegrationAccountBearerTokenAuthUpdate,
            ],
        }
