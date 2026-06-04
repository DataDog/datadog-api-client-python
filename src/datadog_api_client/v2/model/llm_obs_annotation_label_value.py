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
    from datadog_api_client.v2.model.llm_obs_annotation_assessment import LLMObsAnnotationAssessment
    from datadog_api_client.v2.model.llm_obs_annotation_label_value_value import LLMObsAnnotationLabelValueValue


class LLMObsAnnotationLabelValue(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_assessment import LLMObsAnnotationAssessment
        from datadog_api_client.v2.model.llm_obs_annotation_label_value_value import LLMObsAnnotationLabelValueValue

        return {
            "assessment": (LLMObsAnnotationAssessment,),
            "label_schema_id": (str,),
            "reasoning": (str,),
            "value": (LLMObsAnnotationLabelValueValue,),
        }

    attribute_map = {
        "assessment": "assessment",
        "label_schema_id": "label_schema_id",
        "reasoning": "reasoning",
        "value": "value",
    }

    def __init__(
        self_,
        label_schema_id: str,
        value: Union[LLMObsAnnotationLabelValueValue, float, str, List[str], bool],
        assessment: Union[LLMObsAnnotationAssessment, UnsetType] = unset,
        reasoning: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single label value entry in an annotation.
        The ``value`` type must match the label schema type:

        * ``score`` : a number within the schema ``min`` / ``max`` range (integer if ``is_integer`` is ``true`` ).
        * ``categorical`` : a string that is one of the schema ``values``.
        * ``boolean`` : ``true`` or ``false``.
        * ``text`` : any non-empty string.

        :param assessment: Assessment result for a label value.
        :type assessment: LLMObsAnnotationAssessment, optional

        :param label_schema_id: ID of the label schema this value corresponds to.
        :type label_schema_id: str

        :param reasoning: Free text reasoning for this label value.
        :type reasoning: str, optional

        :param value: The value for this label. Must comply with the label schema type constraints.
        :type value: LLMObsAnnotationLabelValueValue
        """
        if assessment is not unset:
            kwargs["assessment"] = assessment
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        super().__init__(kwargs)

        self_.label_schema_id = label_schema_id
        self_.value = value
