# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ExecutionLimit(ModelNormal):
    validations = {
        "count": {
            "inclusive_maximum": 9999,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
        }

    attribute_map = {
        "count": "count",
    }

    def __init__(self_, count: int, **kwargs):
        """
        The maximum number of times to execute a workflow for an incident.

        :param count: The maximum number of workflow executions.
        :type count: int
        """
        super().__init__(kwargs)

        self_.count = count
