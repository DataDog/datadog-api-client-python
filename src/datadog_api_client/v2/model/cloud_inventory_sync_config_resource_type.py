# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudInventorySyncConfigResourceType(ModelSimple):
    """
    JSON:API type for sync configuration resources.

    :param value: If omitted defaults to "sync_configs". Must be one of ["sync_configs"].
    :type value: str
    """

    allowed_values = {
        "sync_configs",
    }
    SYNC_CONFIGS: ClassVar["CloudInventorySyncConfigResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudInventorySyncConfigResourceType.SYNC_CONFIGS = CloudInventorySyncConfigResourceType("sync_configs")
