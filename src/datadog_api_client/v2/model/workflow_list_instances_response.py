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
    from datadog_api_client.v2.model.workflow_instance_list_item import WorkflowInstanceListItem
    from datadog_api_client.v2.model.workflow_list_instances_response_meta import WorkflowListInstancesResponseMeta


class WorkflowListInstancesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_instance_list_item import WorkflowInstanceListItem
        from datadog_api_client.v2.model.workflow_list_instances_response_meta import WorkflowListInstancesResponseMeta

        return {
            "data": ([WorkflowInstanceListItem],),
            "meta": (WorkflowListInstancesResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[WorkflowInstanceListItem], UnsetType] = unset,
        meta: Union[WorkflowListInstancesResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response returned when listing workflow instances.

        :param data: A list of workflow instances.
        :type data: [WorkflowInstanceListItem], optional

        :param meta: Metadata about the instances list
        :type meta: WorkflowListInstancesResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
