# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterMetaEditionMode(ModelSimple):
    """
    Which attributes of the retention filter can be edited. `complete`: all attributes can be edited. `limited`: only the sample rates can be edited; the name, event type, and query are fixed and the filter cannot be reordered (for example, default filters). `unknown`: the edition mode is not set.

    :param value: Must be one of ["unknown", "complete", "limited"].
    :type value: str
    """

    allowed_values = {
        "unknown",
        "complete",
        "limited",
    }
    UNKNOWN: ClassVar["RumRetentionFilterMetaEditionMode"]
    COMPLETE: ClassVar["RumRetentionFilterMetaEditionMode"]
    LIMITED: ClassVar["RumRetentionFilterMetaEditionMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterMetaEditionMode.UNKNOWN = RumRetentionFilterMetaEditionMode("unknown")
RumRetentionFilterMetaEditionMode.COMPLETE = RumRetentionFilterMetaEditionMode("complete")
RumRetentionFilterMetaEditionMode.LIMITED = RumRetentionFilterMetaEditionMode("limited")
