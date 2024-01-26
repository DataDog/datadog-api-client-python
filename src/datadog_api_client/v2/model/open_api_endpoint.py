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


class OpenAPIEndpoint(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "method": (str,),
            "path": (str,),
        }

    attribute_map = {
        "method": "method",
        "path": "path",
    }

    def __init__(self_, method: Union[str, UnsetType] = unset, path: Union[str, UnsetType] = unset, **kwargs):
        """
        Endpoint info extracted from an ``OpenAPI`` specification.

        :param method: The endpoint method.
        :type method: str, optional

        :param path: The endpoint path.
        :type path: str, optional
        """
        if method is not unset:
            kwargs["method"] = method
        if path is not unset:
            kwargs["path"] = path
        super().__init__(kwargs)
