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
    from datadog_api_client.v2.model.workflow_instance_create_meta import WorkflowInstanceCreateMeta


class WorkflowInstanceCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.workflow_instance_create_meta import WorkflowInstanceCreateMeta

        return {
            "meta": (WorkflowInstanceCreateMeta,),
        }

    attribute_map = {
        "meta": "meta",
    }

    def __init__(self_, meta: Union[WorkflowInstanceCreateMeta, UnsetType] = unset, **kwargs):
        """
        Request used to create a workflow instance.

        :param meta: Additional information for creating a workflow instance.
        :type meta: WorkflowInstanceCreateMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
