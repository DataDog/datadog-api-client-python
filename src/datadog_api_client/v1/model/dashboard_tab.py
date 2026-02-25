# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class DashboardTab(ModelNormal):
    validations = {
        "name": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "name": (str,),
            "widget_ids": ([int],),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "widget_ids": "widget_ids",
    }

    def __init__(self_, id: UUID, name: str, widget_ids: List[int], **kwargs):
        """
        Dashboard tab for organizing widgets.

        :param id: UUID of the tab.
        :type id: UUID

        :param name: Name of the tab.
        :type name: str

        :param widget_ids: List of widget IDs belonging to this tab. The backend also accepts positional references in @N format (1-indexed) as a convenience for Terraform and other declarative tools.
        :type widget_ids: [int]
        """
        super().__init__(kwargs)

        self_.id = id
        self_.name = name
        self_.widget_ids = widget_ids
