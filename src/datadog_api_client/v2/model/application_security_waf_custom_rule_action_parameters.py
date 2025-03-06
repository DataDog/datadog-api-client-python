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


class ApplicationSecurityWafCustomRuleActionParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "location": (str,),
            "status_code": (int,),
        }

    attribute_map = {
        "location": "location",
        "status_code": "status_code",
    }

    def __init__(self_, location: Union[str, UnsetType] = unset, status_code: Union[int, UnsetType] = unset, **kwargs):
        """
        The definition of ``ApplicationSecurityWafCustomRuleActionParameters`` object.

        :param location: The location to redirect to when the WAF custom rule triggers.
        :type location: str, optional

        :param status_code: The status code to return when the WAF custom rule triggers.
        :type status_code: int, optional
        """
        if location is not unset:
            kwargs["location"] = location
        if status_code is not unset:
            kwargs["status_code"] = status_code
        super().__init__(kwargs)
