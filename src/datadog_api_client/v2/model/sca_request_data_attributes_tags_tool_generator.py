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


class ScaRequestDataAttributesTagsToolGenerator(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "name": "name",
        "version": "version",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, version: Union[str, UnsetType] = unset, **kwargs):
        """
        Metadata about the tool that generated the SCA tags.

        :param name: The name of the tag generator.
        :type name: str, optional

        :param version: The version of the tag generator.
        :type version: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
