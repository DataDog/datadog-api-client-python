# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema


class LLMObsAnnotationQueueDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema

        return {
            "annotation_schema": (LLMObsAnnotationSchema,),
            "description": (str,),
            "name": (str,),
            "project_id": (str,),
        }

    attribute_map = {
        "annotation_schema": "annotation_schema",
        "description": "description",
        "name": "name",
        "project_id": "project_id",
    }

    def __init__(
        self_,
        name: str,
        project_id: str,
        annotation_schema: Union[LLMObsAnnotationSchema, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an LLM Observability annotation queue.

        :param annotation_schema: Schema defining the labels for an annotation queue.
        :type annotation_schema: LLMObsAnnotationSchema, optional

        :param description: Description of the annotation queue.
        :type description: str, optional

        :param name: Name of the annotation queue.
        :type name: str

        :param project_id: Identifier of the project this queue belongs to.
        :type project_id: str
        """
        if annotation_schema is not unset:
            kwargs["annotation_schema"] = annotation_schema
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.name = name
        self_.project_id = project_id
