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


class LLMObsAnnotationQueueUpdateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
    }

    def __init__(self_, description: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for updating an LLM Observability annotation queue. All fields are optional.

        :param description: Updated description of the annotation queue.
        :type description: str, optional

        :param name: Updated name of the annotation queue.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
