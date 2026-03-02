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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.any_value import AnyValue
    from datadog_api_client.v2.model.any_value_object import AnyValueObject
    from datadog_api_client.v2.model.any_value_item import AnyValueItem


class LLMObsDatasetRecordDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.any_value import AnyValue

        return {
            "created_at": (datetime,),
            "dataset_id": (str,),
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
                none_type,
            ),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "dataset_id": "dataset_id",
        "expected_output": "expected_output",
        "id": "id",
        "input": "input",
        "metadata": "metadata",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        dataset_id: str,
        expected_output: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
        ],
        id: str,
        input: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
        ],
        metadata: Union[Dict[str, Any], none_type],
        updated_at: datetime,
        **kwargs,
    ):
        """
        A single LLM Observability dataset record.

        :param created_at: Timestamp when the record was created.
        :type created_at: datetime

        :param dataset_id: Identifier of the dataset this record belongs to.
        :type dataset_id: str

        :param expected_output: Represents any valid JSON value.
        :type expected_output: AnyValue, none_type

        :param id: Unique identifier of the record.
        :type id: str

        :param input: Represents any valid JSON value.
        :type input: AnyValue, none_type

        :param metadata: Arbitrary metadata associated with the record.
        :type metadata: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type

        :param updated_at: Timestamp when the record was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.dataset_id = dataset_id
        self_.expected_output = expected_output
        self_.id = id
        self_.input = input
        self_.metadata = metadata
        self_.updated_at = updated_at
