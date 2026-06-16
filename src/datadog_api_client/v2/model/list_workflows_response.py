# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_list_item import WorkflowListItem
    from datadog_api_client.v2.model.list_workflows_response_meta import ListWorkflowsResponseMeta


class ListWorkflowsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_list_item import WorkflowListItem
        from datadog_api_client.v2.model.list_workflows_response_meta import ListWorkflowsResponseMeta

        return {
            "data": ([WorkflowListItem],),
            "meta": (ListWorkflowsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[WorkflowListItem], UnsetType] = unset,
        meta: Union[ListWorkflowsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        The response object for a listing workflows request.

        :param data: A list of workflows.
        :type data: [WorkflowListItem], optional

        :param meta: Metadata for a List Workflows response.
        :type meta: ListWorkflowsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
