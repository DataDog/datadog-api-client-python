# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class StorageType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["live", "hot", "online_archives", "driveline", "flex_tier", "case_insensitive", "cloud_prem"].
    :type value: str
    """

    allowed_values = {
        "live",
        "hot",
        "online_archives",
        "driveline",
        "flex_tier",
        "case_insensitive",
        "cloud_prem",
    }
    LIVE: ClassVar["StorageType"]
    HOT: ClassVar["StorageType"]
    ONLINE_ARCHIVES: ClassVar["StorageType"]
    DRIVELINE: ClassVar["StorageType"]
    FLEX_TIER: ClassVar["StorageType"]
    CASE_INSENSITIVE: ClassVar["StorageType"]
    CLOUD_PREM: ClassVar["StorageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


StorageType.LIVE = StorageType("live")
StorageType.HOT = StorageType("hot")
StorageType.ONLINE_ARCHIVES = StorageType("online_archives")
StorageType.DRIVELINE = StorageType("driveline")
StorageType.FLEX_TIER = StorageType("flex_tier")
StorageType.CASE_INSENSITIVE = StorageType("case_insensitive")
StorageType.CLOUD_PREM = StorageType("cloud_prem")
