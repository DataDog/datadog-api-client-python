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


class LLMObsDatasetRecordUpdateItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.any_value import AnyValue

        return {
            "expected_output": (AnyValue,),
            "id": (str,),
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
        "id": "id",
        "input": "input",
        "metadata": "metadata",
    }

    def __init__(
        self_,
        id: str,
        expected_output: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
            UnsetType,
        ] = unset,
        input: Union[
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
        A record update payload for an LLM Observability dataset.

        :param expected_output: Represents any valid JSON value.
        :type expected_output: AnyValue, none_type, optional

        :param id: Unique identifier of the record to update.
        :type id: str

        :param input: Represents any valid JSON value.
        :type input: AnyValue, none_type, optional

        :param metadata: Updated metadata associated with the record.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional
        """
        if expected_output is not unset:
            kwargs["expected_output"] = expected_output
        if input is not unset:
            kwargs["input"] = input
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.id = id
