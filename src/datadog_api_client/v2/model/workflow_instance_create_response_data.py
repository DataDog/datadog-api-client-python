# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class WorkflowInstanceCreateResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
        }

    attribute_map = {
        "id": "id",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, **kwargs):
        """
        Data about the created workflow instance.

        :param id: The ID of the workflow execution. It can be used to fetch the execution status.
        :type id: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
