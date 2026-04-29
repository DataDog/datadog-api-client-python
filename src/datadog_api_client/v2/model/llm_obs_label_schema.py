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
    from datadog_api_client.v2.model.llm_obs_label_schema_type import LLMObsLabelSchemaType


class LLMObsLabelSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_label_schema_type import LLMObsLabelSchemaType

        return {
            "description": (str,),
            "has_assessment": (bool,),
            "has_reasoning": (bool,),
            "id": (str,),
            "is_assessment": (bool,),
            "is_integer": (bool,),
            "is_required": (bool,),
            "max": (float,),
            "min": (float,),
            "name": (str,),
            "type": (LLMObsLabelSchemaType,),
            "values": ([str],),
        }

    attribute_map = {
        "description": "description",
        "has_assessment": "has_assessment",
        "has_reasoning": "has_reasoning",
        "id": "id",
        "is_assessment": "is_assessment",
        "is_integer": "is_integer",
        "is_required": "is_required",
        "max": "max",
        "min": "min",
        "name": "name",
        "type": "type",
        "values": "values",
    }

    def __init__(
        self_,
        name: str,
        type: LLMObsLabelSchemaType,
        description: Union[str, UnsetType] = unset,
        has_assessment: Union[bool, UnsetType] = unset,
        has_reasoning: Union[bool, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_assessment: Union[bool, UnsetType] = unset,
        is_integer: Union[bool, UnsetType] = unset,
        is_required: Union[bool, UnsetType] = unset,
        max: Union[float, UnsetType] = unset,
        min: Union[float, UnsetType] = unset,
        values: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema definition for a single label in an annotation queue.

        :param description: Description of the label.
        :type description: str, optional

        :param has_assessment: Whether this label includes an assessment field.
        :type has_assessment: bool, optional

        :param has_reasoning: Whether this label includes a reasoning field.
        :type has_reasoning: bool, optional

        :param id: Unique identifier of the label schema. Assigned by the server if not provided.
        :type id: str, optional

        :param is_assessment: Whether the boolean label represents an assessment. Requires ``has_assessment`` to be true.
        :type is_assessment: bool, optional

        :param is_integer: Whether score values must be integers. Applicable to score-type labels.
        :type is_integer: bool, optional

        :param is_required: Whether this label is required for an annotation.
        :type is_required: bool, optional

        :param max: Maximum value for score-type labels.
        :type max: float, optional

        :param min: Minimum value for score-type labels.
        :type min: float, optional

        :param name: Name of the label. Must match the pattern ``^[a-zA-Z0-9_-]+$`` and be unique within the queue.
        :type name: str

        :param type: Type of a label in an annotation queue label schema.
        :type type: LLMObsLabelSchemaType

        :param values: Allowed values for categorical-type labels. Must contain at least one non-empty, unique value.
        :type values: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if has_assessment is not unset:
            kwargs["has_assessment"] = has_assessment
        if has_reasoning is not unset:
            kwargs["has_reasoning"] = has_reasoning
        if id is not unset:
            kwargs["id"] = id
        if is_assessment is not unset:
            kwargs["is_assessment"] = is_assessment
        if is_integer is not unset:
            kwargs["is_integer"] = is_integer
        if is_required is not unset:
            kwargs["is_required"] = is_required
        if max is not unset:
            kwargs["max"] = max
        if min is not unset:
            kwargs["min"] = min
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
