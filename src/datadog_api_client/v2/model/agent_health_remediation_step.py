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


class AgentHealthRemediationStep(ModelNormal):
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

    def __init__(self_, order: Union[int, UnsetType] = unset, text: Union[str, UnsetType] = unset, **kwargs):
        """
        A step to remediate the issue.

        :param order: The order in which to perform the step.
        :type order: int, optional

        :param text: The instructions for the step.
        :type text: str, optional
        """
        if order is not unset:
            kwargs["order"] = order
        if text is not unset:
            kwargs["text"] = text
        super().__init__(kwargs)
