# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.workflow_instance_create_response_data import WorkflowInstanceCreateResponseData


class WorkflowInstanceCreateResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_instance_create_response_data import (
            WorkflowInstanceCreateResponseData,
        )

        return {
            "data": (WorkflowInstanceCreateResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[WorkflowInstanceCreateResponseData, UnsetType] = unset, **kwargs):
        """
        Response returned upon successful workflow instance creation.

        :param data: Data about the created workflow instance.
        :type data: WorkflowInstanceCreateResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
