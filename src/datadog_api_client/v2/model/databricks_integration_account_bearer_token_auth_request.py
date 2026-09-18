# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_type import (
        DatabricksIntegrationAccountBearerTokenAuthType,
    )


class DatabricksIntegrationAccountBearerTokenAuthRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_type import (
            DatabricksIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountBearerTokenAuthType,),
            "token": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "token": "token",
    }

    def __init__(self_, auth_type: DatabricksIntegrationAccountBearerTokenAuthType, token: str, **kwargs):
        """
        Bearer token authentication. The method is deprecated and the API rejects it on creation: Databricks accepts it only on accounts that already use it. It is present in the create union so that the method keeps the same shape across create, update and read; sending it on creation always fails. Use ``databricks_oauth`` or ``private_action_runner`` instead.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with Databricks.
        :type token: str
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.token = token
