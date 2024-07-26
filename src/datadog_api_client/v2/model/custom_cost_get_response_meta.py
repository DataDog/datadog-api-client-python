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


class CustomCostGetResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "version": (str,),
        }

    attribute_map = {
        "version": "version",
    }

    def __init__(self_, version: Union[str, UnsetType] = unset, **kwargs):
        """
        Meta for the response from the Get Custom Costs endpoints.

        :param version: Version of Custom Costs file
        :type version: str, optional
        """
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
