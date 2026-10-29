# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TopologyMapInlineNodeStringColumnId(ModelSimple):
    """
    Node field the column fills. `title` is bold text at the top of the node; `subtitle` is smaller text below it.

    :param value: Must be one of ["title", "subtitle"].
    :type value: str
    """

    allowed_values = {
        "title",
        "subtitle",
    }
    TITLE: ClassVar["TopologyMapInlineNodeStringColumnId"]
    SUBTITLE: ClassVar["TopologyMapInlineNodeStringColumnId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TopologyMapInlineNodeStringColumnId.TITLE = TopologyMapInlineNodeStringColumnId("title")
TopologyMapInlineNodeStringColumnId.SUBTITLE = TopologyMapInlineNodeStringColumnId("subtitle")
