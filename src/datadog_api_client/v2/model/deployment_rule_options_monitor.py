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


class DeploymentRuleOptionsMonitor(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "duration": (int,),
            "query": (str,),
        }

    attribute_map = {
        "duration": "duration",
        "query": "query",
    }

    def __init__(self_, query: str, duration: Union[int, UnsetType] = unset, **kwargs):
        """
        Monitor options for deployment rules.

        :param duration: Seconds the monitor needs to stay in OK status for the rule to pass.
        :type duration: int, optional

        :param query: Monitors that match this query are evaluated.
        :type query: str
        """
        if duration is not unset:
            kwargs["duration"] = duration
        super().__init__(kwargs)

        self_.query = query
