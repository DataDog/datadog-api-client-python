# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteProjectsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "project_ids": ([str],),
        }

    attribute_map = {
        "project_ids": "project_ids",
    }

    def __init__(self_, project_ids: List[str], **kwargs):
        """
        Attributes for deleting LLM Observability projects.

        :param project_ids: List of project IDs to delete.
        :type project_ids: [str]
        """
        super().__init__(kwargs)

        self_.project_ids = project_ids
