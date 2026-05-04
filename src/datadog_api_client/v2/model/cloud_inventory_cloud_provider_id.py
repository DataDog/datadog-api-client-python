# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudInventoryCloudProviderId(ModelSimple):
    """
    Cloud provider for this sync configuration (`aws`, `gcp`, or `azure`). For requests, must match the provider block supplied under `attributes`.

    :param value: Must be one of ["aws", "gcp", "azure"].
    :type value: str
    """

    allowed_values = {
        "aws",
        "gcp",
        "azure",
    }
    AWS: ClassVar["CloudInventoryCloudProviderId"]
    GCP: ClassVar["CloudInventoryCloudProviderId"]
    AZURE: ClassVar["CloudInventoryCloudProviderId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudInventoryCloudProviderId.AWS = CloudInventoryCloudProviderId("aws")
CloudInventoryCloudProviderId.GCP = CloudInventoryCloudProviderId("gcp")
CloudInventoryCloudProviderId.AZURE = CloudInventoryCloudProviderId("azure")
