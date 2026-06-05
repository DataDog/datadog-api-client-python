# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_delete_annotation_error import LLMObsDeleteAnnotationError


class LLMObsDeleteAnnotationsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_annotation_error import LLMObsDeleteAnnotationError

        return {
            "annotation_ids": ([str],),
            "errors": ([LLMObsDeleteAnnotationError],),
        }

    attribute_map = {
        "annotation_ids": "annotation_ids",
        "errors": "errors",
    }

    def __init__(self_, annotation_ids: List[str], errors: List[LLMObsDeleteAnnotationError], **kwargs):
        """
        Attributes of the annotation deletion response.

        :param annotation_ids: IDs of the successfully deleted annotations.
        :type annotation_ids: [str]

        :param errors: Errors for annotations that could not be deleted.
        :type errors: [LLMObsDeleteAnnotationError]
        """
        super().__init__(kwargs)

        self_.annotation_ids = annotation_ids
        self_.errors = errors
