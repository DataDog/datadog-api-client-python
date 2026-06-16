# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_item_response import LLMObsAnnotationItemResponse
    from datadog_api_client.v2.model.llm_obs_annotation_error import LLMObsAnnotationError


class LLMObsAnnotationsDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_item_response import LLMObsAnnotationItemResponse
        from datadog_api_client.v2.model.llm_obs_annotation_error import LLMObsAnnotationError

        return {
            "annotations": ([LLMObsAnnotationItemResponse],),
            "errors": ([LLMObsAnnotationError],),
        }

    attribute_map = {
        "annotations": "annotations",
        "errors": "errors",
    }

    def __init__(
        self_,
        annotations: List[LLMObsAnnotationItemResponse],
        errors: Union[List[LLMObsAnnotationError], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the annotations response.

        :param annotations: Successfully created or updated annotations.
        :type annotations: [LLMObsAnnotationItemResponse]

        :param errors: Partial errors for annotations that could not be processed.
        :type errors: [LLMObsAnnotationError], optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        super().__init__(kwargs)

        self_.annotations = annotations
