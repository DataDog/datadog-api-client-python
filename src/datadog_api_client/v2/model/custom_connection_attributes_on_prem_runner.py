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


class CustomConnectionAttributesOnPremRunner(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "url": (str,),
        }

    attribute_map = {
        "id": "id",
        "url": "url",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, url: Union[str, UnsetType] = unset, **kwargs):
        """
        Information about the Private Action Runner used by the custom connection, if the custom connection is associated with a Private Action Runner.

        :param id: The Private Action Runner ID.
        :type id: str, optional

        :param url: The URL of the Private Action Runner.
        :type url: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
