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
    from datadog_api_client.v2.model.workflow_execution_attributes import WorkflowExecutionAttributes
    from datadog_api_client.v2.model.workflow_execution_data_type import WorkflowExecutionDataType


class WorkflowExecutionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_execution_attributes import WorkflowExecutionAttributes
        from datadog_api_client.v2.model.workflow_execution_data_type import WorkflowExecutionDataType

        return {
            "attributes": (WorkflowExecutionAttributes,),
            "id": (UUID,),
            "type": (WorkflowExecutionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: WorkflowExecutionAttributes, id: UUID, type: WorkflowExecutionDataType, **kwargs):
        """
        A single workflow execution resource.

        :param attributes: Attributes of a workflow execution.
        :type attributes: WorkflowExecutionAttributes

        :param id: The unique identifier of the workflow execution.
        :type id: UUID

        :param type: The resource type for workflow executions.
        :type type: WorkflowExecutionDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
