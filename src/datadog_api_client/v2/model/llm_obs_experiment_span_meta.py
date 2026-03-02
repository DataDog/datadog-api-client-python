# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experiment_span_error import LLMObsExperimentSpanError
    from datadog_api_client.v2.model.any_value import AnyValue
    from datadog_api_client.v2.model.any_value_object import AnyValueObject
    from datadog_api_client.v2.model.any_value_item import AnyValueItem


class LLMObsExperimentSpanMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_span_error import LLMObsExperimentSpanError
        from datadog_api_client.v2.model.any_value import AnyValue

        return {
            "error": (LLMObsExperimentSpanError,),
            "expected_output": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "input": (AnyValue,),
            "output": (AnyValue,),
        }

    attribute_map = {
        "error": "error",
        "expected_output": "expected_output",
        "input": "input",
        "output": "output",
    }

    def __init__(
        self_,
        error: Union[LLMObsExperimentSpanError, UnsetType] = unset,
        expected_output: Union[Dict[str, Any], UnsetType] = unset,
        input: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
            UnsetType,
        ] = unset,
        output: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """
        Metadata associated with an experiment span.

        :param error: Error details for an experiment span.
        :type error: LLMObsExperimentSpanError, optional

        :param expected_output: Expected output for the span, used for evaluation.
        :type expected_output: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param input: Represents any valid JSON value.
        :type input: AnyValue, none_type, optional

        :param output: Represents any valid JSON value.
        :type output: AnyValue, none_type, optional
        """
        if error is not unset:
            kwargs["error"] = error
        if expected_output is not unset:
            kwargs["expected_output"] = expected_output
        if input is not unset:
            kwargs["input"] = input
        if output is not unset:
            kwargs["output"] = output
        super().__init__(kwargs)
