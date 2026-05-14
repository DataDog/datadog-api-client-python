# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class IncidentRoleAssignmentDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "role": (str, none_type),
        }

    attribute_map = {
        "role": "role",
    }

    def __init__(self_, role: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Attributes for creating a role assignment.

        :param role: The name of the role to assign.
        :type role: str, none_type, optional
        """
        if role is not unset:
            kwargs["role"] = role
        super().__init__(kwargs)
