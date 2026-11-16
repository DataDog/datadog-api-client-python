# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
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
            "annotator": (str, none_type),
            "interaction_id": (str,),
            "label_values": ([LLMObsAnnotationLabelValue],),
        }

    attribute_map = {
        "annotator": "annotator",
        "interaction_id": "interaction_id",
        "label_values": "label_values",
    }

    def __init__(
        self_,
        interaction_id: str,
        label_values: List[LLMObsAnnotationLabelValue],
        annotator: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single annotation to create or update. The annotation is matched by
        ``interaction_id`` and the requesting user's identity.

        :param annotator: Caller-supplied name or identifier for the external person or automated system that produced the labels.
            The value is an opaque string with no required format. Use a stable, recognizable value for the same
            producer across annotations.
            The value is stored and returned as provided. It is not a Datadog user ID or login, and it is not
            resolved against Datadog users.
            Omit this field or set it to ``null`` to preserve existing attribution. Set it to an empty string to clear
            attribution.
        :type annotator: str, none_type, optional

        :param interaction_id: ID of the interaction to annotate.
        :type interaction_id: str

        :param label_values: Label values for this annotation. Each entry references a label schema by ID
            and provides the corresponding value validated against the schema type constraints.
        :type label_values: [LLMObsAnnotationLabelValue]
        """
        if annotator is not unset:
            kwargs["annotator"] = annotator
        super().__init__(kwargs)

        self_.interaction_id = interaction_id
        self_.label_values = label_values
