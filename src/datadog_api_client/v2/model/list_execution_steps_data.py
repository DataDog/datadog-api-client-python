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
    from datadog_api_client.v2.model.list_execution_steps_attributes import ListExecutionStepsAttributes
    from datadog_api_client.v2.model.list_execution_steps_data_type import ListExecutionStepsDataType


class ListExecutionStepsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_execution_steps_attributes import ListExecutionStepsAttributes
        from datadog_api_client.v2.model.list_execution_steps_data_type import ListExecutionStepsDataType

        return {
            "attributes": (ListExecutionStepsAttributes,),
            "id": (UUID,),
            "type": (ListExecutionStepsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ListExecutionStepsAttributes, id: UUID, type: ListExecutionStepsDataType, **kwargs):
        """
        Data for execution steps response.

        :param attributes: Attributes of an execution steps response.
        :type attributes: ListExecutionStepsAttributes

        :param id: The unique identifier of the workflow execution.
        :type id: UUID

        :param type: The resource type for workflow execution steps.
        :type type: ListExecutionStepsDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
