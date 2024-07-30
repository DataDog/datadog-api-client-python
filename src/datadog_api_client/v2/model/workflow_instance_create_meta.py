# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class WorkflowInstanceCreateMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "payload": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
        }

    attribute_map = {
        "payload": "payload",
    }

    def __init__(self_, payload: Union[Dict[str, Any], UnsetType] = unset, **kwargs):
        """
        Additional information for creating a workflow instance.

        :param payload: The input parameters to the workflow.
        :type payload: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if payload is not unset:
            kwargs["payload"] = payload
        super().__init__(kwargs)
