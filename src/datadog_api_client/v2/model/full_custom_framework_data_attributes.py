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
            "created_at": (int,),
            "created_by": (str,),
            "description": (str,),
            "handle": (str,),
            "icon_url": (str,),
            "id": (str,),
            "modified_at": (int,),
            "name": (str,),
            "org_id": (int,),
            "requirements": ([CustomFrameworkRequirement],),
            "version": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "handle": "handle",
        "icon_url": "icon_url",
        "id": "id",
        "modified_at": "modified_at",
        "name": "name",
        "org_id": "org_id",
        "requirements": "requirements",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: int,
        created_by: str,
        description: str,
        handle: str,
        icon_url: str,
        id: str,
        modified_at: int,
        name: str,
        org_id: int,
        requirements: List[CustomFrameworkRequirement],
        version: str,
        **kwargs,
    ):
        """
        Full Framework Data Attributes.

        :param created_at: Creation Timestamp
        :type created_at: int

        :param created_by: Creator
        :type created_by: str

        :param description: Framework Description
        :type description: str

        :param handle: Framework Handle
        :type handle: str

        :param icon_url: Framework Icon URL
        :type icon_url: str

        :param id: Framework ID
        :type id: str

        :param modified_at: Modification Timestamp
        :type modified_at: int

        :param name: Framework Name
        :type name: str

        :param org_id: Organization ID
        :type org_id: int

        :param requirements: Framework Requirements
        :type requirements: [CustomFrameworkRequirement]

        :param version: Framework Version
        :type version: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.handle = handle
        self_.icon_url = icon_url
        self_.id = id
        self_.modified_at = modified_at
        self_.name = name
        self_.org_id = org_id
        self_.requirements = requirements
        self_.version = version
