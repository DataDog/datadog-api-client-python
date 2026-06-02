# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy


class IncidentUserDefinedRoleDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy

        return {
            "created": (datetime,),
            "description": (str, none_type),
            "modified": (datetime,),
            "name": (str,),
            "policy": (IncidentUserDefinedRolePolicy,),
        }

    attribute_map = {
        "created": "created",
        "description": "description",
        "modified": "modified",
        "name": "name",
        "policy": "policy",
    }

    def __init__(
        self_,
        created: datetime,
        modified: datetime,
        name: str,
        policy: IncidentUserDefinedRolePolicy,
        description: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident user-defined role.

        :param created: Timestamp when the role was created.
        :type created: datetime

        :param description: A description of the user-defined role.
        :type description: str, none_type, optional

        :param modified: Timestamp when the role was last modified.
        :type modified: datetime

        :param name: The name of the user-defined role.
        :type name: str

        :param policy: Policy configuration for a user-defined role.
        :type policy: IncidentUserDefinedRolePolicy
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.created = created
        self_.modified = modified
        self_.name = name
        self_.policy = policy
