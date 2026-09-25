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


class GeneralInvestigationAttributesWithoutTimeBounds(ModelNormal):
    validations = {
        "description": {
            "max_length": 4096,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "tags": "tags",
    }

    def __init__(self_, description: str, tags: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Attributes for a general investigation without an explicit time window.

        :param description: A free-form description of what to investigate, up to 4,096 characters.
        :type description: str

        :param tags: Tags that scope the investigation.
        :type tags: [str], optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.description = description
