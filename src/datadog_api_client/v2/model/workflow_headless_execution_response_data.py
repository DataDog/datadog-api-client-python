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
    from datadog_api_client.v2.model.workflow_headless_execution_response_attributes import (
        WorkflowHeadlessExecutionResponseAttributes,
    )
    from datadog_api_client.v2.model.workflow_headless_execution_response_type import (
        WorkflowHeadlessExecutionResponseType,
    )


class WorkflowHeadlessExecutionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_headless_execution_response_attributes import (
            WorkflowHeadlessExecutionResponseAttributes,
        )
        from datadog_api_client.v2.model.workflow_headless_execution_response_type import (
            WorkflowHeadlessExecutionResponseType,
        )

        return {
            "attributes": (WorkflowHeadlessExecutionResponseAttributes,),
            "id": (str,),
            "type": (WorkflowHeadlessExecutionResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: WorkflowHeadlessExecutionResponseAttributes,
        id: str,
        type: WorkflowHeadlessExecutionResponseType,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: WorkflowHeadlessExecutionResponseAttributes

        :param id: The ID of the parent workflow
        :type id: str

        :param type: The type for workflow headless execution response
        :type type: WorkflowHeadlessExecutionResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
