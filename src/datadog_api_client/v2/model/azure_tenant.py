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
    from datadog_api_client.v2.model.azure_tenant_type import AzureTenantType


class AzureTenant(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.azure_tenant_type import AzureTenantType

        return {
            "app_client_id": (str,),
            "client_secret": (str,),
            "custom_scopes": (str,),
            "tenant_id": (str,),
            "type": (AzureTenantType,),
        }

    attribute_map = {
        "app_client_id": "app_client_id",
        "client_secret": "client_secret",
        "custom_scopes": "custom_scopes",
        "tenant_id": "tenant_id",
        "type": "type",
    }

    def __init__(
        self_,
        app_client_id: str,
        client_secret: str,
        tenant_id: str,
        type: AzureTenantType,
        custom_scopes: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``AzureTenant`` object.

        :param app_client_id: The Client ID, also known as the Application ID in Azure, is a unique identifier for an application. It's used to identify the application during the authentication process. Your Application (client) ID is listed in the application's overview page. You can navigate to your application via the Azure Directory.
        :type app_client_id: str

        :param client_secret: The Client Secret is a confidential piece of information known only to the application and Azure AD. It's used to prove the application's identity. Your Client Secret is available from the application’s secrets page. You can navigate to your application via the Azure Directory.
        :type client_secret: str

        :param custom_scopes: If provided, the custom scope to be requested from Microsoft when acquiring an OAuth 2 access token. This custom scope is used only in conjunction with the HTTP action. A resource's scope is constructed by using the identifier URI for the resource and .default, separated by a forward slash (/) as follows:{identifierURI}/.default.
        :type custom_scopes: str, optional

        :param tenant_id: The Tenant ID, also known as the Directory ID in Azure, is a unique identifier that represents an Azure AD instance. Your Tenant ID (Directory ID) is listed in your Active Directory overview page under the 'Tenant information' section.
        :type tenant_id: str

        :param type: The definition of the ``AzureTenant`` object.
        :type type: AzureTenantType
        """
        if custom_scopes is not unset:
            kwargs["custom_scopes"] = custom_scopes
        super().__init__(kwargs)

        self_.app_client_id = app_client_id
        self_.client_secret = client_secret
        self_.tenant_id = tenant_id
        self_.type = type
