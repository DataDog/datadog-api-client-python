# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudInventoryCloudProviderRequestType(ModelSimple):
    """
    JSON:API type for upsert sync configuration requests.

    :param value: If omitted defaults to "cloud_provider". Must be one of ["cloud_provider"].
    :type value: str
    """

    allowed_values = {
        "cloud_provider",
    }
    CLOUD_PROVIDER: ClassVar["CloudInventoryCloudProviderRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudInventoryCloudProviderRequestType.CLOUD_PROVIDER = CloudInventoryCloudProviderRequestType("cloud_provider")
