# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ConnectionGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "connection_group_id": (str,),
            "label": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "connection_group_id": "connectionGroupId",
        "label": "label",
        "tags": "tags",
    }

    def __init__(self_, connection_group_id: str, label: str, tags: List[str], **kwargs):
        """
        The definition of ``ConnectionGroup`` object.

        :param connection_group_id: The ``ConnectionGroup`` ``connectionGroupId``.
        :type connection_group_id: str

        :param label: The ``ConnectionGroup`` ``label``.
        :type label: str

        :param tags: The ``ConnectionGroup`` ``tags``.
        :type tags: [str]
        """
        super().__init__(kwargs)

        self_.connection_group_id = connection_group_id
        self_.label = label
        self_.tags = tags
