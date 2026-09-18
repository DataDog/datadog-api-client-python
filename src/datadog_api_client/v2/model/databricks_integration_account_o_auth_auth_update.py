# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
        DatabricksIntegrationAccountOAuthAuthType,
    )


class DatabricksIntegrationAccountOAuthAuthUpdate(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.databricks_integration_account_o_auth_auth_type import (
            DatabricksIntegrationAccountOAuthAuthType,
        )

        return {
            "auth_type": (DatabricksIntegrationAccountOAuthAuthType,),
            "azure_tenant_id": (str, none_type),
            "client_id": (str,),
            "client_secret": (str,),
        }

    attribute_map = {
        "auth_type": "auth_type",
        "azure_tenant_id": "azure_tenant_id",
        "client_id": "client_id",
        "client_secret": "client_secret",
    }

    def __init__(
        self_,
        auth_type: DatabricksIntegrationAccountOAuthAuthType,
        azure_tenant_id: Union[str, none_type, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        client_secret: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Databricks OAuth machine-to-machine authentication using a service principal. Only the fields provided are changed; omit ``client_secret`` to keep the stored one.

        :param auth_type: The authentication method type.
        :type auth_type: DatabricksIntegrationAccountOAuthAuthType

        :param azure_tenant_id: Microsoft Entra ID tenant of the service principal, for Azure Databricks workspaces. Omit it to keep the stored tenant, send ``null`` or an empty string to remove it, or send a value to replace it.
        :type azure_tenant_id: str, none_type, optional

        :param client_id: Client ID of the Databricks service principal.
        :type client_id: str, optional

        :param client_secret: Secret of the Databricks service principal. Generate it under User management > Service principals > Credentials & secrets in Databricks.
        :type client_secret: str, optional
        """
        if azure_tenant_id is not unset:
            kwargs["azure_tenant_id"] = azure_tenant_id
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if client_secret is not unset:
            kwargs["client_secret"] = client_secret
        super().__init__(kwargs)

        self_.auth_type = auth_type
