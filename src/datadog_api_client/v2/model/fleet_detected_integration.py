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


class FleetDetectedIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "escaped_name": (str,),
            "prefix": (str,),
        }

    attribute_map = {
        "escaped_name": "escaped_name",
        "prefix": "prefix",
    }

    def __init__(self_, escaped_name: Union[str, UnsetType] = unset, prefix: Union[str, UnsetType] = unset, **kwargs):
        """
        An integration detected on the agent but not necessarily configured.

        :param escaped_name: Escaped integration name.
        :type escaped_name: str, optional

        :param prefix: Integration prefix identifier.
        :type prefix: str, optional
        """
        if escaped_name is not unset:
            kwargs["escaped_name"] = escaped_name
        if prefix is not unset:
            kwargs["prefix"] = prefix
        super().__init__(kwargs)
