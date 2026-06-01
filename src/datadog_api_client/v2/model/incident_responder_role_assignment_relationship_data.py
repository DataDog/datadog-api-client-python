# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class IncidentResponderRoleAssignmentRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (UUID,),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: UUID, type: str, **kwargs):
        """
        A single role assignment relationship data object.

        :param id: The role assignment identifier.
        :type id: UUID

        :param type: The role assignment resource type.
        :type type: str
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
