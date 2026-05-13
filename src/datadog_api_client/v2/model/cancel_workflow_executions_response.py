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
    from datadog_api_client.v2.model.cancel_workflow_executions_data import CancelWorkflowExecutionsData


class CancelWorkflowExecutionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cancel_workflow_executions_data import CancelWorkflowExecutionsData

        return {
            "data": (CancelWorkflowExecutionsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CancelWorkflowExecutionsData, **kwargs):
        """
        Response from canceling all running workflow execution instances.

        :param data: Data returned after canceling workflow executions.
        :type data: CancelWorkflowExecutionsData
        """
        super().__init__(kwargs)

        self_.data = data
