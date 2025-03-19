# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_user_relationship_type import WorkflowUserRelationshipType


class WorkflowUserRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_user_relationship_type import WorkflowUserRelationshipType

        return {
            "id": (str,),
            "type": (WorkflowUserRelationshipType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: WorkflowUserRelationshipType, **kwargs):
        """
        The definition of ``WorkflowUserRelationshipData`` object.

        :param id: The user identifier
        :type id: str

        :param type: The definition of ``WorkflowUserRelationshipType`` object.
        :type type: WorkflowUserRelationshipType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
