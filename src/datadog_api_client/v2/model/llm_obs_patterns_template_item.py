# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class LLMObsPatternsTemplateItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "clustering_instructions": (str,),
            "created_at": (datetime,),
            "description": (str,),
            "evp_query_prefix": (str,),
            "id": (str,),
            "name": (str,),
            "scope": (str,),
            "template": (str,),
            "time_frame_duration_ms": (int,),
        }

    attribute_map = {
        "clustering_instructions": "clustering_instructions",
        "created_at": "created_at",
        "description": "description",
        "evp_query_prefix": "evp_query_prefix",
        "id": "id",
        "name": "name",
        "scope": "scope",
        "template": "template",
        "time_frame_duration_ms": "time_frame_duration_ms",
    }

    def __init__(
        self_,
        clustering_instructions: str,
        created_at: datetime,
        description: str,
        evp_query_prefix: str,
        id: str,
        name: str,
        scope: str,
        template: str,
        time_frame_duration_ms: int,
        **kwargs,
    ):
        """
        A single Agent Observability patterns template in a list response.

        :param clustering_instructions: Instructions guiding how topics are clustered for configurations linked to this template.
        :type clustering_instructions: str

        :param created_at: Timestamp when the template was created.
        :type created_at: datetime

        :param description: Human-readable description of what the template is for.
        :type description: str

        :param evp_query_prefix: Prefix merged into the query that selects spans for configurations linked to this template.
        :type evp_query_prefix: str

        :param id: Unique identifier of the template.
        :type id: str

        :param name: Name of the template.
        :type name: str

        :param scope: Scope the template applies to.
        :type scope: str

        :param template: Template used to guide topic generation for configurations linked to this template.
        :type template: str

        :param time_frame_duration_ms: Default lookback window, in milliseconds, for configurations linked to this template.
        :type time_frame_duration_ms: int
        """
        super().__init__(kwargs)

        self_.clustering_instructions = clustering_instructions
        self_.created_at = created_at
        self_.description = description
        self_.evp_query_prefix = evp_query_prefix
        self_.id = id
        self_.name = name
        self_.scope = scope
        self_.template = template
        self_.time_frame_duration_ms = time_frame_duration_ms
