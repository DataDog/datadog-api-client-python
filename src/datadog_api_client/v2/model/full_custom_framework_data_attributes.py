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
    from datadog_api_client.v2.model.custom_framework_requirement import CustomFrameworkRequirement


class FullCustomFrameworkDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_framework_requirement import CustomFrameworkRequirement

        return {
            "description": (str,),
            "handle": (str,),
            "icon_url": (str,),
            "name": (str,),
            "requirements": ([CustomFrameworkRequirement],),
            "version": (str,),
        }

    attribute_map = {
        "description": "description",
        "handle": "handle",
        "icon_url": "icon_url",
        "name": "name",
        "requirements": "requirements",
        "version": "version",
    }

    def __init__(
        self_,
        description: str,
        handle: str,
        icon_url: str,
        name: str,
        requirements: List[CustomFrameworkRequirement],
        version: str,
        **kwargs,
    ):
        """
        Full Framework Data Attributes.

        :param description: Framework Description
        :type description: str

        :param handle: Framework Handle
        :type handle: str

        :param icon_url: Framework Icon URL
        :type icon_url: str

        :param name: Framework Name
        :type name: str

        :param requirements: Framework Requirements
        :type requirements: [CustomFrameworkRequirement]

        :param version: Framework Version
        :type version: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.handle = handle
        self_.icon_url = icon_url
        self_.name = name
        self_.requirements = requirements
        self_.version = version
