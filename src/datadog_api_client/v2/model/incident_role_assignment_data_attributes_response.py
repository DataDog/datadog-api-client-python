# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IncidentRoleAssignmentDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created": (datetime,),
            "deleted": (datetime,),
            "modified": (datetime,),
            "responder_type": (str,),
            "role": (str,),
        }

    attribute_map = {
        "created": "created",
        "deleted": "deleted",
        "modified": "modified",
        "responder_type": "responder_type",
        "role": "role",
    }

    def __init__(
        self_,
        created: datetime,
        modified: datetime,
        responder_type: str,
        role: str,
        deleted: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident role assignment.

        :param created: Timestamp when the role assignment was created.
        :type created: datetime

        :param deleted: Timestamp when the role assignment was deleted, or the zero timestamp if it has not been deleted.
        :type deleted: datetime, optional

        :param modified: Timestamp when the role assignment was last modified.
        :type modified: datetime

        :param responder_type: The type of the responder.
        :type responder_type: str

        :param role: The name of the assigned role.
        :type role: str
        """
        if deleted is not unset:
            kwargs["deleted"] = deleted
        super().__init__(kwargs)

        self_.created = created
        self_.modified = modified
        self_.responder_type = responder_type
        self_.role = role
