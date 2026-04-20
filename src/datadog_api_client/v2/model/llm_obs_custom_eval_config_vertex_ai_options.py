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


class LLMObsCustomEvalConfigVertexAIOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "location": (str,),
            "project": (str,),
        }

    attribute_map = {
        "location": "location",
        "project": "project",
    }

    def __init__(self_, location: Union[str, UnsetType] = unset, project: Union[str, UnsetType] = unset, **kwargs):
        """
        Google Vertex AI-specific options for LLM provider configuration.

        :param location: Google Cloud region.
        :type location: str, optional

        :param project: Google Cloud project ID.
        :type project: str, optional
        """
        if location is not unset:
            kwargs["location"] = location
        if project is not unset:
            kwargs["project"] = project
        super().__init__(kwargs)
