# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AgentHealthRemediationStep(ModelNormal):
    validations = {
        "order": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "order": (int,),
            "text": (str,),
        }

    attribute_map = {
        "order": "order",
        "text": "text",
    }

    def __init__(self_, order: int, text: str, **kwargs):
        """
        A step to remediate the issue.

        :param order: The order in which to perform the step.
        :type order: int

        :param text: The instructions for the step.
        :type text: str
        """
        super().__init__(kwargs)

        self_.order = order
        self_.text = text
