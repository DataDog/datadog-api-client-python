# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudInventorySyncConfigAzureRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_id": (str,),
            "container": (str,),
            "resource_group": (str,),
            "storage_account": (str,),
            "subscription_id": (str,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "client_id": "client_id",
        "container": "container",
        "resource_group": "resource_group",
        "storage_account": "storage_account",
        "subscription_id": "subscription_id",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        client_id: str,
        container: str,
        resource_group: str,
        storage_account: str,
        subscription_id: str,
        tenant_id: str,
        **kwargs,
    ):
        """
        Azure settings for the storage account and container with inventory data.

        :param client_id: Azure AD application (client) ID used for access.
        :type client_id: str

        :param container: Blob container name.
        :type container: str

        :param resource_group: Resource group containing the storage account.
        :type resource_group: str

        :param storage_account: Storage account name.
        :type storage_account: str

        :param subscription_id: Azure subscription ID.
        :type subscription_id: str

        :param tenant_id: Azure AD tenant ID.
        :type tenant_id: str
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.container = container
        self_.resource_group = resource_group
        self_.storage_account = storage_account
        self_.subscription_id = subscription_id
        self_.tenant_id = tenant_id
