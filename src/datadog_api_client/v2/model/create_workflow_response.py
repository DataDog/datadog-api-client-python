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
    from datadog_api_client.v2.model.workflow_data import WorkflowData


class CreateWorkflowResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_data import WorkflowData

        return {
            "data": (WorkflowData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: WorkflowData, **kwargs):
        """
        The response object after creating a new workflow.

        :param data: Data related to the workflow.
        :type data: WorkflowData
        """
        super().__init__(kwargs)

        self_.data = data
