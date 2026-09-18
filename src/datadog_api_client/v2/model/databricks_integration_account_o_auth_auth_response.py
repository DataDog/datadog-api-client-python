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
    from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
        DatabricksIntegrationAccountOAuthAuthType,
    )


class DatabricksIntegrationAccountOAuthAuthResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
            DatabricksIntegrationAccountOAuthAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountOAuthAuthType,),
            "azure_tenant_id": (str,),
            "client_id": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "azure_tenant_id": "azure_tenant_id",
        "client_id": "client_id",
    }

    def __init__(
        self_,
        auth_type: DatabricksIntegrationAccountOAuthAuthType,
        client_id: str,
        azure_tenant_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Databricks OAuth authentication method and service principal configured on the account.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountOAuthAuthType

        :param azure_tenant_id: Microsoft Entra ID tenant of the service principal, for Azure Databricks workspaces.
        :type azure_tenant_id: str, optional

        :param client_id: Client ID of the Databricks service principal.
        :type client_id: str
        """
        if azure_tenant_id is not unset:
            kwargs["azure_tenant_id"] = azure_tenant_id
        super().__init__(kwargs)

        self_.auth_type = auth_type
        self_.client_id = client_id
