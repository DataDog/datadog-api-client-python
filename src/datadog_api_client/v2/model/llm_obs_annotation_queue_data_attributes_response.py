# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema


class LLMObsAnnotationQueueDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema

        return {
            "annotation_schema": (LLMObsAnnotationSchema,),
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "modified_at": (datetime,),
            "modified_by": (str,),
            "name": (str,),
            "owned_by": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "annotation_schema": "annotation_schema",
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "owned_by": "owned_by",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        description: str,
        modified_at: datetime,
        modified_by: str,
        name: str,
        owned_by: str,
        project_id: str,
        annotation_schema: Union[LLMObsAnnotationSchema, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an LLM Observability annotation queue.

        :param annotation_schema: Schema defining the labels for an annotation queue.
        :type annotation_schema: LLMObsAnnotationSchema, optional

        :param created_at: Timestamp when the queue was created.
        :type created_at: datetime

        :param created_by: Identifier of the user who created the queue.
        :type created_by: str

        :param description: Description of the annotation queue.
        :type description: str

        :param modified_at: Timestamp when the queue was last modified.
        :type modified_at: datetime

        :param modified_by: Identifier of the user who last modified the queue.
        :type modified_by: str

        :param name: Name of the annotation queue.
        :type name: str

        :param owned_by: Identifier of the user who owns the queue.
        :type owned_by: str

        :param project_id: Identifier of the project this queue belongs to.
        :type project_id: str
        """
        if annotation_schema is not unset:
            kwargs["annotation_schema"] = annotation_schema
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.name = name
        self_.owned_by = owned_by
        self_.project_id = project_id
