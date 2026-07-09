# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringAzureAppRegistration(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_id": (str,),
            "error_count": (int,),
            "resource_collection_enabled": (bool,),
            "subscription_count": (int,),
            "tenant_id": (str,),
        }

    attribute_map = {
        "client_id": "client_id",
        "error_count": "error_count",
        "resource_collection_enabled": "resource_collection_enabled",
        "subscription_count": "subscription_count",
        "tenant_id": "tenant_id",
    }

    def __init__(
        self_,
        client_id: str,
        error_count: int,
        resource_collection_enabled: bool,
        subscription_count: int,
        tenant_id: str,
        **kwargs,
    ):
        """
        An Azure App Registration discovered for the organization.

        :param client_id: The client ID of the App Registration.
        :type client_id: str

        :param error_count: The number of errors encountered while crawling resources for this App Registration.
        :type error_count: int

        :param resource_collection_enabled: Whether resource collection is enabled for this App Registration.
        :type resource_collection_enabled: bool

        :param subscription_count: The number of Azure subscriptions associated with this App Registration.
        :type subscription_count: int

        :param tenant_id: The Azure tenant ID of the App Registration.
        :type tenant_id: str
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.error_count = error_count
        self_.resource_collection_enabled = resource_collection_enabled
        self_.subscription_count = subscription_count
        self_.tenant_id = tenant_id
