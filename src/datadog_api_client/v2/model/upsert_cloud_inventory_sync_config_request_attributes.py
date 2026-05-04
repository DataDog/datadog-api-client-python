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
    from datadog_api_client.v2.model.cloud_inventory_sync_config_aws_request_attributes import (
        CloudInventorySyncConfigAWSRequestAttributes,
    )
    from datadog_api_client.v2.model.cloud_inventory_sync_config_azure_request_attributes import (
        CloudInventorySyncConfigAzureRequestAttributes,
    )
    from datadog_api_client.v2.model.cloud_inventory_sync_config_gcp_request_attributes import (
        CloudInventorySyncConfigGCPRequestAttributes,
    )


class UpsertCloudInventorySyncConfigRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_inventory_sync_config_aws_request_attributes import (
            CloudInventorySyncConfigAWSRequestAttributes,
        )
        from datadog_api_client.v2.model.cloud_inventory_sync_config_azure_request_attributes import (
            CloudInventorySyncConfigAzureRequestAttributes,
        )
        from datadog_api_client.v2.model.cloud_inventory_sync_config_gcp_request_attributes import (
            CloudInventorySyncConfigGCPRequestAttributes,
        )

        return {
            "aws": (CloudInventorySyncConfigAWSRequestAttributes,),
            "azure": (CloudInventorySyncConfigAzureRequestAttributes,),
            "gcp": (CloudInventorySyncConfigGCPRequestAttributes,),
        }

    attribute_map = {
        "aws": "aws",
        "azure": "azure",
        "gcp": "gcp",
    }

    def __init__(
        self_,
        aws: Union[CloudInventorySyncConfigAWSRequestAttributes, UnsetType] = unset,
        azure: Union[CloudInventorySyncConfigAzureRequestAttributes, UnsetType] = unset,
        gcp: Union[CloudInventorySyncConfigGCPRequestAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provider-specific configuration. Include the object that matches ``data.id`` ( ``aws`` , ``gcp`` , or ``azure`` ).

        :param aws: AWS settings for the customer bucket that stores inventory reports.
        :type aws: CloudInventorySyncConfigAWSRequestAttributes, optional

        :param azure: Azure settings for the storage account and container with inventory data.
        :type azure: CloudInventorySyncConfigAzureRequestAttributes, optional

        :param gcp: GCP settings for buckets involved in inventory reporting.
        :type gcp: CloudInventorySyncConfigGCPRequestAttributes, optional
        """
        if aws is not unset:
            kwargs["aws"] = aws
        if azure is not unset:
            kwargs["azure"] = azure
        if gcp is not unset:
            kwargs["gcp"] = gcp
        super().__init__(kwargs)
