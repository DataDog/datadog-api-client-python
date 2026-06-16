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
    from datadog_api_client.v2.model.llm_obs_annotation_label_value import LLMObsAnnotationLabelValue


class LLMObsUpsertAnnotationItem(ModelNormal):
    validations = {
        "label_values": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_label_value import LLMObsAnnotationLabelValue

        return {
            "interaction_id": (str,),
            "label_values": ([LLMObsAnnotationLabelValue],),
        }

    attribute_map = {
        "interaction_id": "interaction_id",
        "label_values": "label_values",
    }

    def __init__(self_, interaction_id: str, label_values: List[LLMObsAnnotationLabelValue], **kwargs):
        """
        A single annotation to create or update. The annotation is matched by
        ``interaction_id`` and the requesting user's identity.

        :param interaction_id: ID of the interaction to annotate.
        :type interaction_id: str

        :param label_values: Label values for this annotation. Each entry references a label schema by ID
            and provides the corresponding value validated against the schema type constraints.
        :type label_values: [LLMObsAnnotationLabelValue]
        """
        super().__init__(kwargs)

        self_.interaction_id = interaction_id
        self_.label_values = label_values
