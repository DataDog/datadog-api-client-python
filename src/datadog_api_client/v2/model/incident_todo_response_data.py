# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_attributes import IncidentTodoAttributes
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType


@dataclass
class IncidentTodoResponseDataJSON:
    id: str
    assignees: Union[IncidentTodoAssigneeArray, UnsetType] = unset
    completed: Union[str, none_type, UnsetType] = unset
    content: Union[str, UnsetType] = unset
    due_date: Union[str, none_type, UnsetType] = unset
    incident_id: Union[str, UnsetType] = unset


class IncidentTodoResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_todo_type import IncidentTodoType

        return {
            "attributes": (IncidentTodoAttributes,),
            "id": (str,),
            "type": (IncidentTodoType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = IncidentTodoResponseDataJSON

    def __init__(
        self_, id: str, type: IncidentTodoType, attributes: Union[IncidentTodoAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Incident todo response data.

        :param attributes: Incident todo's attributes.
        :type attributes: IncidentTodoAttributes, optional

        :param id: The incident todo's ID.
        :type id: str

        :param type: Todo resource type.
        :type type: IncidentTodoType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
