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


class DatabricksIntegrationAccountBearerTokenAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_type import (
            DatabricksIntegrationAccountBearerTokenAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountBearerTokenAuthType,),
        }

    attribute_map = {
        "auth_type": "auth_type",
    }

    def __init__(self_, auth_type: DatabricksIntegrationAccountBearerTokenAuthType, **kwargs):
        """
        The bearer token authentication method configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountBearerTokenAuthType
        """
        super().__init__(kwargs)

        self_.auth_type = auth_type
