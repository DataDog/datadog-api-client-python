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
    from datadog_api_client.v2.model.pruned_trace_attributes import PrunedTraceAttributes
    from datadog_api_client.v2.model.pruned_trace_type import PrunedTraceType


class PrunedTraceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.pruned_trace_attributes import PrunedTraceAttributes
        from datadog_api_client.v2.model.pruned_trace_type import PrunedTraceType

        return {
            "attributes": (PrunedTraceAttributes,),
            "id": (str,),
            "type": (PrunedTraceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: PrunedTraceAttributes, id: str, type: PrunedTraceType, **kwargs):
        """
        A pruned trace resource document.

        :param attributes: The attributes of a pruned trace returned by the Get pruned trace by ID endpoint.
        :type attributes: PrunedTraceAttributes

        :param id: The full 128-bit trace ID, encoded as a 32-character hexadecimal string.
        :type id: str

        :param type: The type of the pruned trace resource. The value is always ``pruned_trace``.
        :type type: PrunedTraceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
