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
    from datadog_api_client.v2.model.llm_obs_dataset_record_tag_operations import LLMObsDatasetRecordTagOperations
    from datadog_api_client.v2.model.any_value_object import AnyValueObject
    from datadog_api_client.v2.model.any_value_item import AnyValueItem


class LLMObsDatasetBatchUpdateInsertRecord(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.any_value import AnyValue
        from datadog_api_client.v2.model.llm_obs_dataset_record_tag_operations import LLMObsDatasetRecordTagOperations

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
            "tag_operations": (LLMObsDatasetRecordTagOperations,),
            "tags": ([str],),
        }

    attribute_map = {
        "expected_output": "expected_output",
        "id": "id",
        "input": "input",
        "metadata": "metadata",
        "tag_operations": "tag_operations",
        "tags": "tags",
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
        id: Union[str, UnsetType] = unset,
        metadata: Union[Dict[str, Any], UnsetType] = unset,
        tag_operations: Union[LLMObsDatasetRecordTagOperations, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A record to insert as part of a batch update on an LLM Observability dataset.

        :param expected_output: Represents any valid JSON value.
        :type expected_output: AnyValue, none_type, optional

        :param id: Optional user-provided identifier for the record. If omitted, the server generates an identifier.
        :type id: str, optional

        :param input: Represents any valid JSON value.
        :type input: AnyValue, none_type

        :param metadata: Arbitrary metadata associated with the record.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param tag_operations: Explicit tag operations for updating records. Operations are applied in order, Remove then Add then Set. ``set`` is the final override; if specified, the result of ``remove`` and ``add`` is discarded.
        :type tag_operations: LLMObsDatasetRecordTagOperations, optional

        :param tags: List of tag strings.
        :type tags: [str], optional
        """
        if expected_output is not unset:
            kwargs["expected_output"] = expected_output
        if id is not unset:
            kwargs["id"] = id
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if tag_operations is not unset:
            kwargs["tag_operations"] = tag_operations
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.input = input
