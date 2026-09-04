# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class DatabricksIntegrationAccountAuthenticationRequest(ModelComposed):
    def __init__(self, **kwargs):
        """
        Authentication for creating the Databricks integration account. Exactly one method is set. Choosing ``private-action-runner`` leaves the ``databricks-model-serving-metrics`` dataflow unable to collect data.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountOAuthAuthType

        :param azure_tenant_id: Microsoft Entra ID tenant of the service principal, for Azure Databricks workspaces.
        :type azure_tenant_id: str, optional

        :param client_id: Client ID of the Databricks service principal.
        :type client_id: str

        :param client_secret: Secret of the Databricks service principal.
        :type client_secret: str

        :param connection_id: Unique identifier of the Private Action Runner connection holding the credentials.
        :type connection_id: str

        :param secret_path: Path of the credential inside the secret backend configured on the runner.
        :type secret_path: str, optional

        :param user_uuid: Unique identifier of the user the Private Action Runner connection belongs to.
        :type user_uuid: str
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
        from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_request import (
            DatabricksIntegrationAccountOAuthAuthRequest,
        )
        from datadog_api_client.v2.model.integration_account_private_action_runner_auth_request import (
            IntegrationAccountPrivateActionRunnerAuthRequest,
        )

        return {
            "oneOf": [
                DatabricksIntegrationAccountOAuthAuthRequest,
                IntegrationAccountPrivateActionRunnerAuthRequest,
            ],
        }
