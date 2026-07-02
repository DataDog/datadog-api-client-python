# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateSnapshotTTL(ModelSimple):
    """
    The time-to-live for the snapshot. This value corresponds to storage lifecycle policies that automatically delete the snapshot after the specified period.

    :param value: Must be one of ["30d", "60d", "90d", "1y", "2y", "inf"].
    :type value: str
    """

    allowed_values = {
        "30d",
        "60d",
        "90d",
        "1y",
        "2y",
        "inf",
    }
    THIRTY_DAYS: ClassVar["CreateSnapshotTTL"]
    SIXTY_DAYS: ClassVar["CreateSnapshotTTL"]
    NINETY_DAYS: ClassVar["CreateSnapshotTTL"]
    ONE_YEAR: ClassVar["CreateSnapshotTTL"]
    TWO_YEARS: ClassVar["CreateSnapshotTTL"]
    INFINITE: ClassVar["CreateSnapshotTTL"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateSnapshotTTL.THIRTY_DAYS = CreateSnapshotTTL("30d")
CreateSnapshotTTL.SIXTY_DAYS = CreateSnapshotTTL("60d")
CreateSnapshotTTL.NINETY_DAYS = CreateSnapshotTTL("90d")
CreateSnapshotTTL.ONE_YEAR = CreateSnapshotTTL("1y")
CreateSnapshotTTL.TWO_YEARS = CreateSnapshotTTL("2y")
CreateSnapshotTTL.INFINITE = CreateSnapshotTTL("inf")
