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
    from datadog_api_client.v2.model.stream_event_v1 import StreamEventV1


class WorkflowScaffoldAgenticStreamResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stream_event_v1 import StreamEventV1

        return {
            "event": (StreamEventV1,),
            "id": (str,),
        }

    attribute_map = {
        "event": "event",
        "id": "id",
    }

    def __init__(self_, event: StreamEventV1, id: str, **kwargs):
        """


        :param event:
        :type event: StreamEventV1

        :param id: The generation ID.
        :type id: str
        """
        super().__init__(kwargs)

        self_.event = event
        self_.id = id
