# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.trace_attributes import TraceAttributes
    from datadog_api_client.v2.model.trace_type import TraceType


class TraceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.trace_attributes import TraceAttributes
        from datadog_api_client.v2.model.trace_type import TraceType

        return {
            "attributes": (TraceAttributes,),
            "id": (str,),
            "type": (TraceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: TraceAttributes, id: str, type: TraceType, **kwargs):
        """
        A trace resource document.

        :param attributes: The attributes of a trace returned by the Get trace by ID endpoint.
        :type attributes: TraceAttributes

        :param id: The full 128-bit trace ID, encoded as a 32-character hexadecimal string.
        :type id: str

        :param type: The type of the trace resource. The value is always ``trace``.
        :type type: TraceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
