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


class DowntimeMonitorIncludedAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
        }

    attribute_map = {
        "name": "name",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of the monitor identified by the downtime.

        :param name: The name of the monitor identified by the downtime.
        :type name: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
