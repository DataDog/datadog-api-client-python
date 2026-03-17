# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamSyncSelectionStateOperation(ModelSimple):
    """
    The operation to perform on the selected hierarchy.
        When set to `include`, synchronization covers the
        referenced teams or organizations.

    :param value: If omitted defaults to "include". Must be one of ["include"].
    :type value: str
    """

    allowed_values = {
        "include",
    }
    INCLUDE: ClassVar["TeamSyncSelectionStateOperation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamSyncSelectionStateOperation.INCLUDE = TeamSyncSelectionStateOperation("include")
