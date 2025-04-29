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
    from datadog_api_client.v2.model.custom_framework_control import CustomFrameworkControl


class CustomFrameworkRequirement(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_framework_control import CustomFrameworkControl

        return {
            "controls": ([CustomFrameworkControl],),
            "name": (str,),
        }

    attribute_map = {
        "controls": "controls",
        "name": "name",
    }

    def __init__(self_, controls: List[CustomFrameworkControl], name: str, **kwargs):
        """
        Framework Requirement.

        :param controls: Requirement Controls.
        :type controls: [CustomFrameworkControl]

        :param name: Requirement Name.
        :type name: str
        """
        super().__init__(kwargs)

        self_.controls = controls
        self_.name = name
