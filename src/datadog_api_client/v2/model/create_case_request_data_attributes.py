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


class CreateCaseRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_priority import CasePriority

        return {
            "assignee_id": (str,),
            "description": (str,),
            "priority": (CasePriority,),
            "title": (str,),
        }

    attribute_map = {
        "assignee_id": "assignee_id",
        "description": "description",
        "priority": "priority",
        "title": "title",
    }

    def __init__(
        self_,
        assignee_id: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        priority: Union[CasePriority, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the case to create.

        :param assignee_id: Unique identifier of the user assigned to the case.
        :type assignee_id: str, optional

        :param description: Description of the case. If not provided, the description will be automatically generated.
        :type description: str, optional

        :param priority: Case priority
        :type priority: CasePriority, optional

        :param title: Title of the case. If not provided, the title will be automatically generated.
        :type title: str, optional
        """
        if assignee_id is not unset:
            kwargs["assignee_id"] = assignee_id
        if description is not unset:
            kwargs["description"] = description
        if priority is not unset:
            kwargs["priority"] = priority
        if title is not unset:
            kwargs["title"] = title
        super().__init__(kwargs)
