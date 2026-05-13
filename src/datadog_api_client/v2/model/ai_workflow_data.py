# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_workflow_attributes import AIWorkflowAttributes
    from datadog_api_client.v2.model.ai_workflow_data_type import AIWorkflowDataType


class AIWorkflowData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_workflow_attributes import AIWorkflowAttributes
        from datadog_api_client.v2.model.ai_workflow_data_type import AIWorkflowDataType

        return {
            "attributes": (AIWorkflowAttributes,),
            "id": (UUID,),
            "type": (AIWorkflowDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AIWorkflowAttributes, id: UUID, type: AIWorkflowDataType, **kwargs):
        """
        A single AI workflow resource.

        :param attributes: Attributes of an AI workflow.
        :type attributes: AIWorkflowAttributes

        :param id: The unique identifier of the AI workflow.
        :type id: UUID

        :param type: The resource type for AI workflows.
        :type type: AIWorkflowDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
