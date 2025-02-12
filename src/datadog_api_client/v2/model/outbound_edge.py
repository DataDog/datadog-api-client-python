# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OutboundEdge(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "branch_name": (str,),
            "next_step_name": (str,),
        }

    attribute_map = {
        "branch_name": "branchName",
        "next_step_name": "nextStepName",
    }

    def __init__(self_, branch_name: str, next_step_name: str, **kwargs):
        """
        The definition of ``OutboundEdge`` object.

        :param branch_name: The ``OutboundEdge`` ``branchName``.
        :type branch_name: str

        :param next_step_name: The ``OutboundEdge`` ``nextStepName``.
        :type next_step_name: str
        """
        super().__init__(kwargs)

        self_.branch_name = branch_name
        self_.next_step_name = next_step_name
