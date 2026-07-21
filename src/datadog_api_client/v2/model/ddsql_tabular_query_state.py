# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DdsqlTabularQueryState(ModelSimple):
    """
    Lifecycle state of a DDSQL tabular query response.
        `running` means the query is still executing and the client should poll
        the fetch endpoint with the returned `query_id`. `completed` means the
        result set is inlined in `columns` and no further polling is required.

    :param value: Must be one of ["running", "completed"].
    :type value: str
    """

    allowed_values = {
        "running",
        "completed",
    }
    RUNNING: ClassVar["DdsqlTabularQueryState"]
    COMPLETED: ClassVar["DdsqlTabularQueryState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DdsqlTabularQueryState.RUNNING = DdsqlTabularQueryState("running")
DdsqlTabularQueryState.COMPLETED = DdsqlTabularQueryState("completed")
