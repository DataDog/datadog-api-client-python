# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.databricks_integration_account_bearer_token_auth_type import (
        DatabricksIntegrationAccountBearerTokenAuthType,
    )


class DatabricksIntegrationAccountBearerTokenAuthUpdate(ModelNormal):
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

    def __init__(
        self_,
        auth_type: DatabricksIntegrationAccountBearerTokenAuthType,
        token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Bearer token authentication. The credential is a single opaque secret, a Databricks personal access token, with no accompanying non-secret identifier. The method is deprecated: Databricks accepts it only on accounts that already use it, and never on creation. Only the fields provided are changed; omit ``token`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountBearerTokenAuthType

        :param token: Secret token used to authenticate with Databricks.
        :type token: str, optional
        """
        if token is not unset:
            kwargs["token"] = token
        super().__init__(kwargs)

        self_.auth_type = auth_type
