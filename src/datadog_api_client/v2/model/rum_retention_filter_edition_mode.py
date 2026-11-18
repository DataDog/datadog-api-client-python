# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterEditionMode(ModelSimple):
    """
    The types of changes the retention filter accepts. `complete` filters can be updated and deleted.
        `limited` filters are default retention filters that can't be deleted.

    :param value: Must be one of ["unknown", "complete", "limited"].
    :type value: str
    """

    allowed_values = {
        "unknown",
        "complete",
        "limited",
    }
    UNKNOWN: ClassVar["RumRetentionFilterEditionMode"]
    COMPLETE: ClassVar["RumRetentionFilterEditionMode"]
    LIMITED: ClassVar["RumRetentionFilterEditionMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterEditionMode.UNKNOWN = RumRetentionFilterEditionMode("unknown")
RumRetentionFilterEditionMode.COMPLETE = RumRetentionFilterEditionMode("complete")
RumRetentionFilterEditionMode.LIMITED = RumRetentionFilterEditionMode("limited")
