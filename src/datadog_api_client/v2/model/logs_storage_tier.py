# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class LogsStorageTier(StringEnum):
    """
    Specifies storage type as indexes or online-archives

    :param value: If omitted defaults to "indexes". Must be one of ["indexes", "online-archives"].
    :type value: str
    """

    allowed_values = {
        "indexes",
        "online-archives",
    }
    INDEXES: ClassVar["LogsStorageTier"]
    ONLINE_ARCHIVES: ClassVar["LogsStorageTier"]


LogsStorageTier.INDEXES = LogsStorageTier("indexes")
LogsStorageTier.ONLINE_ARCHIVES = LogsStorageTier("online-archives")
