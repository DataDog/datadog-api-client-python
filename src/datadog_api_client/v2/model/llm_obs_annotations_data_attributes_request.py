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
    from datadog_api_client.v2.model.llm_obs_upsert_annotation_item import LLMObsUpsertAnnotationItem


class LLMObsAnnotationsDataAttributesRequest(ModelNormal):
    validations = {
        "annotations": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_upsert_annotation_item import LLMObsUpsertAnnotationItem

        return {
            "annotations": ([LLMObsUpsertAnnotationItem],),
        }

    attribute_map = {
        "annotations": "annotations",
    }

    def __init__(self_, annotations: List[LLMObsUpsertAnnotationItem], **kwargs):
        """
        Attributes for creating or updating annotations.

        :param annotations: List of annotations to create or update. Must contain at least one item.
        :type annotations: [LLMObsUpsertAnnotationItem]
        """
        super().__init__(kwargs)

        self_.annotations = annotations
