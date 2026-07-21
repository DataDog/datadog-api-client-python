# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy


class IncidentUserDefinedRoleDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_user_defined_role_policy import IncidentUserDefinedRolePolicy

        return {
            "description": (str, none_type),
            "name": (str,),
            "policy": (IncidentUserDefinedRolePolicy,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "policy": "policy",
    }

    def __init__(
        self_,
        name: str,
        description: Union[str, none_type, UnsetType] = unset,
        policy: Union[IncidentUserDefinedRolePolicy, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an incident user-defined role.

        :param description: A description of the user-defined role.
        :type description: str, none_type, optional

        :param name: The name of the user-defined role.
        :type name: str

        :param policy: Policy configuration for a user-defined role.
        :type policy: IncidentUserDefinedRolePolicy, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if policy is not unset:
            kwargs["policy"] = policy
        super().__init__(kwargs)

        self_.name = name
