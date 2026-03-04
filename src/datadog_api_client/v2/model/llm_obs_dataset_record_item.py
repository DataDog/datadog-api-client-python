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
    from datadog_api_client.v2.model.any_value import AnyValue
    from datadog_api_client.v2.model.any_value_object import AnyValueObject
    from datadog_api_client.v2.model.any_value_item import AnyValueItem


class LLMObsDatasetRecordItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.any_value import AnyValue

        return {
            "expected_output": (AnyValue,),
            "input": (AnyValue,),
            "metadata": (
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
        }

    attribute_map = {
        "expected_output": "expected_output",
        "input": "input",
        "metadata": "metadata",
    }

    def __init__(
        self_,
        input: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
        ],
        expected_output: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
            UnsetType,
        ] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        A single record to append to an LLM Observability dataset.

        :param expected_output: Represents any valid JSON value.
        :type expected_output: AnyValue, none_type, optional

        :param input: Represents any valid JSON value.
        :type input: AnyValue, none_type

        :param metadata: Arbitrary metadata associated with the record.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if expected_output is not unset:
            kwargs["expected_output"] = expected_output
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.input = input
