# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GuidedTableStorageType(ModelSimple):
    """
    Storage tier to target for an events-platform query in a guided table.

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
    LIVE: ClassVar["GuidedTableStorageType"]
    HOT: ClassVar["GuidedTableStorageType"]
    ONLINE_ARCHIVES: ClassVar["GuidedTableStorageType"]
    DRIVELINE: ClassVar["GuidedTableStorageType"]
    FLEX_TIER: ClassVar["GuidedTableStorageType"]
    CASE_INSENSITIVE: ClassVar["GuidedTableStorageType"]
    CLOUD_PREM: ClassVar["GuidedTableStorageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GuidedTableStorageType.LIVE = GuidedTableStorageType("live")
GuidedTableStorageType.HOT = GuidedTableStorageType("hot")
GuidedTableStorageType.ONLINE_ARCHIVES = GuidedTableStorageType("online_archives")
GuidedTableStorageType.DRIVELINE = GuidedTableStorageType("driveline")
GuidedTableStorageType.FLEX_TIER = GuidedTableStorageType("flex_tier")
GuidedTableStorageType.CASE_INSENSITIVE = GuidedTableStorageType("case_insensitive")
GuidedTableStorageType.CLOUD_PREM = GuidedTableStorageType("cloud_prem")
