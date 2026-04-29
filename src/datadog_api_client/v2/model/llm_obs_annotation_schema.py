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
    from datadog_api_client.v2.model.llm_obs_label_schema import LLMObsLabelSchema


class LLMObsAnnotationSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_label_schema import LLMObsLabelSchema

        return {
            "label_schemas": ([LLMObsLabelSchema],),
        }

    attribute_map = {
        "label_schemas": "label_schemas",
    }

    def __init__(self_, label_schemas: List[LLMObsLabelSchema], **kwargs):
        """
        Schema defining the labels for an annotation queue.

        :param label_schemas: List of label schema definitions.
        :type label_schemas: [LLMObsLabelSchema]
        """
        super().__init__(kwargs)

        self_.label_schemas = label_schemas
