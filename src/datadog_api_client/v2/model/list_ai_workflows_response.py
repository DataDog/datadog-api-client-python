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
    from datadog_api_client.v2.model.ai_workflow_data import AIWorkflowData
    from datadog_api_client.v2.model.ai_workflow_list_meta import AIWorkflowListMeta


class ListAIWorkflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_workflow_data import AIWorkflowData
        from datadog_api_client.v2.model.ai_workflow_list_meta import AIWorkflowListMeta

        return {
            "data": ([AIWorkflowData],),
            "meta": (AIWorkflowListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[AIWorkflowData], meta: AIWorkflowListMeta, **kwargs):
        """
        Response containing a list of AI workflows.

        :param data: List of AI workflow resources.
        :type data: [AIWorkflowData]

        :param meta: Metadata for the list AI workflows response.
        :type meta: AIWorkflowListMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
