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
    from datadog_api_client.v2.model.llm_obs_dataset_record_item import LLMObsDatasetRecordItem


class LLMObsDatasetRecordsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_record_item import LLMObsDatasetRecordItem

        return {
            "deduplicate": (bool,),
            "records": ([LLMObsDatasetRecordItem],),
        }

    attribute_map = {
        "deduplicate": "deduplicate",
        "records": "records",
    }

    def __init__(self_, records: List[LLMObsDatasetRecordItem], deduplicate: Union[bool, UnsetType] = unset, **kwargs):
        """
        Attributes for appending records to an LLM Observability dataset.

        :param deduplicate: Whether to deduplicate records before appending. Defaults to ``true``.
        :type deduplicate: bool, optional

        :param records: List of records to append to the dataset.
        :type records: [LLMObsDatasetRecordItem]
        """
        if deduplicate is not unset:
            kwargs["deduplicate"] = deduplicate
        super().__init__(kwargs)

        self_.records = records
