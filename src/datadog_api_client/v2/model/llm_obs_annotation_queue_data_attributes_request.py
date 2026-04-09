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


class LLMObsAnnotationQueueDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "project_id": "project_id",
    }

    def __init__(self_, name: str, project_id: str, description: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes for creating an LLM Observability annotation queue.

        :param description: Description of the annotation queue.
        :type description: str, optional

        :param name: Name of the annotation queue.
        :type name: str

        :param project_id: Identifier of the project this queue belongs to.
        :type project_id: str
        """
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.name = name
        self_.project_id = project_id
