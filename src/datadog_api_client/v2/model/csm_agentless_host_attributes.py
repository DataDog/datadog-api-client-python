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
    from datadog_api_client.v2.model.csm_cloud_provider import CsmCloudProvider
    from datadog_api_client.v2.model.csm_agentless_host_resource_type import CsmAgentlessHostResourceType


class CsmAgentlessHostAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.csm_cloud_provider import CsmCloudProvider
        from datadog_api_client.v2.model.csm_agentless_host_resource_type import CsmAgentlessHostResourceType

        return {
            "account_id": (str,),
            "cloud_provider": (CsmCloudProvider,),
            "has_posture_management": (bool,),
            "has_vulnerability_scanning": (bool,),
            "resource_type": (CsmAgentlessHostResourceType,),
        }

    attribute_map = {
        "account_id": "account_id",
        "cloud_provider": "cloud_provider",
        "has_posture_management": "has_posture_management",
        "has_vulnerability_scanning": "has_vulnerability_scanning",
        "resource_type": "resource_type",
    }

    def __init__(
        self_,
        account_id: str,
        cloud_provider: CsmCloudProvider,
        has_posture_management: bool,
        has_vulnerability_scanning: bool,
        resource_type: CsmAgentlessHostResourceType,
        **kwargs,
    ):
        """
        Attributes of an agentless host.

        :param account_id: The ID of the cloud account that the host belongs to.
        :type account_id: str

        :param cloud_provider: The cloud provider of a host resource.
        :type cloud_provider: CsmCloudProvider

        :param has_posture_management: Whether CSM Misconfigurations is enabled for this host. ``true`` if enabled; ``false`` if disabled.
        :type has_posture_management: bool

        :param has_vulnerability_scanning: Whether CSM Vulnerabilities is enabled for this host. ``true`` if enabled; ``false`` if disabled.
        :type has_vulnerability_scanning: bool

        :param resource_type: The type of cloud resource for an agentless host.
        :type resource_type: CsmAgentlessHostResourceType
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.cloud_provider = cloud_provider
        self_.has_posture_management = has_posture_management
        self_.has_vulnerability_scanning = has_vulnerability_scanning
        self_.resource_type = resource_type
