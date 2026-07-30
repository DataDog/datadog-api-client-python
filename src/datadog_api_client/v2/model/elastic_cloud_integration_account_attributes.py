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
    from datadog_api_client.v2.model.elastic_cloud_interface import ElasticCloudInterface
    from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions
    from datadog_api_client.v2.model.elastic_cloud_monitoring_interface import ElasticCloudMonitoringInterface
    from datadog_api_client.v2.model.elastic_cloud_ccm_interface import ElasticCloudCcmInterface


class ElasticCloudIntegrationAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_interface import ElasticCloudInterface
        from datadog_api_client.v2.model.integration_account_permissions import IntegrationAccountPermissions

        return {
            "interface": (ElasticCloudInterface,),
            "name": (str,),
            "permissions": (IntegrationAccountPermissions,),
        }

    attribute_map = {
        "interface": "interface",
        "name": "name",
        "permissions": "permissions",
    }
    read_only_vars = {
        "permissions",
    }

    def __init__(
        self_,
        interface: Union[ElasticCloudInterface, ElasticCloudMonitoringInterface, ElasticCloudCcmInterface],
        name: str,
        permissions: Union[IntegrationAccountPermissions, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an Elastic Cloud integration account.

        :param interface: Elastic Cloud interface (source-type). Exactly one interface variant is set, selected by its ``type``.
        :type interface: ElasticCloudInterface

        :param name: Human-readable name of the account.
        :type name: str

        :param permissions: Read-only permission information for the account, derived from its restriction policy.
        :type permissions: IntegrationAccountPermissions, optional
        """
        if permissions is not unset:
            kwargs["permissions"] = permissions
        super().__init__(kwargs)

        self_.interface = interface
        self_.name = name
