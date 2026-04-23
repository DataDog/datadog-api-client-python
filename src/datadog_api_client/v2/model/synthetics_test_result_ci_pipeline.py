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


class SyntheticsTestResultCIPipeline(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "number": (int,),
            "url": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "number": "number",
        "url": "url",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        number: Union[int, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the CI pipeline.

        :param id: Pipeline identifier.
        :type id: str, optional

        :param name: Pipeline name.
        :type name: str, optional

        :param number: Pipeline number.
        :type number: int, optional

        :param url: Pipeline URL.
        :type url: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if number is not unset:
            kwargs["number"] = number
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
