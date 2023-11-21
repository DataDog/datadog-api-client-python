# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SensitiveDataScannerStandardPatternAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "included_keywords": ([str],),
            "name": (str,),
            "pattern": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "included_keywords": "included_keywords",
        "name": "name",
        "pattern": "pattern",
        "tags": "tags",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        included_keywords: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the Sensitive Data Scanner standard pattern.

        :param description: Description of the standard pattern.
        :type description: str, optional

        :param included_keywords: List of included keywords.
        :type included_keywords: [str], optional

        :param name: Name of the standard pattern.
        :type name: str, optional

        :param pattern: Regex to match.
        :type pattern: str, optional

        :param tags: List of tags.
        :type tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if included_keywords is not unset:
            kwargs["included_keywords"] = included_keywords
        if name is not unset:
            kwargs["name"] = name
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
