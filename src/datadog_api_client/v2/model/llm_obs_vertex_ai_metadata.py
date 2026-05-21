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


class LLMObsVertexAIMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "location": (str,),
            "project": (str,),
            "project_ids": ([str],),
        }

    attribute_map = {
        "location": "location",
        "project": "project",
        "project_ids": "project_ids",
    }

    def __init__(
        self_,
        location: Union[str, UnsetType] = unset,
        project: Union[str, UnsetType] = unset,
        project_ids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Vertex AI-specific metadata for an integration account or inference request.

        :param location: The Vertex AI region.
        :type location: str, optional

        :param project: The Google Cloud project ID.
        :type project: str, optional

        :param project_ids: List of Google Cloud project IDs available to the service account.
        :type project_ids: [str], optional
        """
        if location is not unset:
            kwargs["location"] = location
        if project is not unset:
            kwargs["project"] = project
        if project_ids is not unset:
            kwargs["project_ids"] = project_ids
        super().__init__(kwargs)
