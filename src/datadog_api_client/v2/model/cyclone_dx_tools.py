# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cyclone_dx_tool_component import CycloneDXToolComponent


class CycloneDXTools(ModelNormal):
    validations = {
        "components": {
            "max_items": 1,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cyclone_dx_tool_component import CycloneDXToolComponent

        return {
            "components": ([CycloneDXToolComponent],),
        }

    attribute_map = {
        "components": "components",
    }

    def __init__(self_, components: List[CycloneDXToolComponent], **kwargs):
        """
        Tools used to generate the BOM.

        :param components: List of tool components. Only one tool is supported.
        :type components: [CycloneDXToolComponent]
        """
        super().__init__(kwargs)

        self_.components = components
