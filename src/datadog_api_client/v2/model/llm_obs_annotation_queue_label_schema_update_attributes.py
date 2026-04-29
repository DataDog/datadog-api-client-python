# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema


class LLMObsAnnotationQueueLabelSchemaUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema

        return {
            "annotation_schema": (LLMObsAnnotationSchema,),
        }

    attribute_map = {
        "annotation_schema": "annotation_schema",
    }

    def __init__(self_, annotation_schema: LLMObsAnnotationSchema, **kwargs):
        """
        Attributes for updating an annotation queue label schema.

        :param annotation_schema: Schema defining the labels for an annotation queue.
        :type annotation_schema: LLMObsAnnotationSchema
        """
        super().__init__(kwargs)

        self_.annotation_schema = annotation_schema
