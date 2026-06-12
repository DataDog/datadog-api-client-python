# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SharedDashboardSelectableTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "allow_any_value": (bool,),
            "default_values": ([str],),
            "name": (str,),
            "prefix": (str,),
            "type": (str,),
            "visible_tags": ([str],),
        }

    attribute_map = {
        "allow_any_value": "allow_any_value",
        "default_values": "default_values",
        "name": "name",
        "prefix": "prefix",
        "type": "type",
        "visible_tags": "visible_tags",
    }

    def __init__(
        self_,
        allow_any_value: bool,
        default_values: List[str],
        name: str,
        prefix: str,
        type: str,
        visible_tags: List[str],
        **kwargs,
    ):
        """
        A template variable that viewers can modify on the shared dashboard.

        :param allow_any_value: Whether viewers can see all tag values for the template variable and specify any value.
        :type allow_any_value: bool

        :param default_values: Default selected values for the variable.
        :type default_values: [str]

        :param name: Name of the template variable.
        :type name: str

        :param prefix: Tag prefix for the variable.
        :type prefix: str

        :param type: Type of the template variable.
        :type type: str

        :param visible_tags: Restricts which tag values are visible to the viewer.
        :type visible_tags: [str]
        """
        super().__init__(kwargs)

        self_.allow_any_value = allow_any_value
        self_.default_values = default_values
        self_.name = name
        self_.prefix = prefix
        self_.type = type
        self_.visible_tags = visible_tags
