# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_instance_summary_data import WorkflowInstanceSummaryData


class ListWorkflowInstancesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_instance_summary_data import WorkflowInstanceSummaryData

        return {
            "data": ([WorkflowInstanceSummaryData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[WorkflowInstanceSummaryData], **kwargs):
        """
        Response containing a list of workflow instance summaries.

        :param data: List of workflow instance summaries.
        :type data: [WorkflowInstanceSummaryData]
        """
        super().__init__(kwargs)

        self_.data = data
