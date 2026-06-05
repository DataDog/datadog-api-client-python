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
    from datadog_api_client.v2.model.llm_obs_label_schema_type import LLMObsLabelSchemaType
    from datadog_api_client.v2.model.llm_obs_annotation_label_value_value import LLMObsAnnotationLabelValueValue


class LLMObsAnnotationLabelValueResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_assessment import LLMObsAnnotationAssessment
        from datadog_api_client.v2.model.llm_obs_label_schema_type import LLMObsLabelSchemaType
        from datadog_api_client.v2.model.llm_obs_annotation_label_value_value import LLMObsAnnotationLabelValueValue

        return {
            "assessment": (LLMObsAnnotationAssessment,),
            "label_schema_id": (str,),
            "name_when_saved": (str,),
            "reasoning": (str,),
            "type": (LLMObsLabelSchemaType,),
            "value": (LLMObsAnnotationLabelValueValue,),
        }

    attribute_map = {
        "assessment": "assessment",
        "label_schema_id": "label_schema_id",
        "name_when_saved": "name_when_saved",
        "reasoning": "reasoning",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        label_schema_id: str,
        value: Union[LLMObsAnnotationLabelValueValue, float, str, List[str], bool],
        assessment: Union[LLMObsAnnotationAssessment, UnsetType] = unset,
        name_when_saved: Union[str, UnsetType] = unset,
        reasoning: Union[str, UnsetType] = unset,
        type: Union[LLMObsLabelSchemaType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single label value entry in an annotation response.
        In addition to the submitted fields, the server populates ``type`` and
        ``name_when_saved`` to mirror the schema state at the time the annotation
        was created — these help clients display values correctly when the schema
        has since changed.

        :param assessment: Assessment result for a label value.
        :type assessment: LLMObsAnnotationAssessment, optional

        :param label_schema_id: ID of the label schema this value corresponds to.
        :type label_schema_id: str

        :param name_when_saved: Name of the label schema at the time the annotation was created.
        :type name_when_saved: str, optional

        :param reasoning: Free text reasoning for this label value.
        :type reasoning: str, optional

        :param type: Type of a label in an annotation queue label schema.
        :type type: LLMObsLabelSchemaType, optional

        :param value: The value for this label. Must comply with the label schema type constraints.
        :type value: LLMObsAnnotationLabelValueValue
        """
        if assessment is not unset:
            kwargs["assessment"] = assessment
        if name_when_saved is not unset:
            kwargs["name_when_saved"] = name_when_saved
        if reasoning is not unset:
            kwargs["reasoning"] = reasoning
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.label_schema_id = label_schema_id
        self_.value = value
