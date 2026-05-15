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


class CreatePublishRequestRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "title": (str,),
        }

    attribute_map = {
        "description": "description",
        "title": "title",
    }

    def __init__(self_, title: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for creating a publish request.

        :param description: An optional description of the changes in this publish request.
        :type description: str, optional

        :param title: A short title for the publish request.
        :type title: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.title = title
