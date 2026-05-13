# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CancelWorkflowExecutionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "canceled_count": (int,),
        }

    attribute_map = {
        "canceled_count": "canceled_count",
    }

    def __init__(self_, canceled_count: int, **kwargs):
        """
        Data returned after canceling workflow executions.

        :param canceled_count: The number of running instances that were successfully canceled.
        :type canceled_count: int
        """
        super().__init__(kwargs)

        self_.canceled_count = canceled_count
