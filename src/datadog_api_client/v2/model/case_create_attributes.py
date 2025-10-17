# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.case_priority import CasePriority


class CaseCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_priority import CasePriority

        return {
            "description": (str,),
            "priority": (CasePriority,),
            "title": (str,),
            "type_id": (str,),
        }

    attribute_map = {
        "description": "description",
        "priority": "priority",
        "title": "title",
        "type_id": "type_id",
    }

    def __init__(
        self_,
        title: str,
        type_id: str,
        description: Union[str, UnsetType] = unset,
        priority: Union[CasePriority, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case creation attributes

        :param description: Description
        :type description: str, optional

        :param priority: Case priority
        :type priority: CasePriority, optional

        :param title: Title
        :type title: str

        :param type_id: Case type UUID
        :type type_id: str
        """
        if description is not unset:
            kwargs["description"] = description
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.title = title
        self_.type_id = type_id
