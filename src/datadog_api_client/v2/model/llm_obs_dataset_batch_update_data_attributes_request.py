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
    from datadog_api_client.v2.model.llm_obs_dataset_batch_update_insert_record import (
        LLMObsDatasetBatchUpdateInsertRecord,
    )
    from datadog_api_client.v2.model.llm_obs_dataset_batch_update_update_record import (
        LLMObsDatasetBatchUpdateUpdateRecord,
    )


class LLMObsDatasetBatchUpdateDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_dataset_batch_update_insert_record import (
            LLMObsDatasetBatchUpdateInsertRecord,
        )
        from datadog_api_client.v2.model.llm_obs_dataset_batch_update_update_record import (
            LLMObsDatasetBatchUpdateUpdateRecord,
        )

        return {
            "create_new_version": (bool,),
            "delete_records": ([str],),
            "insert_records": ([LLMObsDatasetBatchUpdateInsertRecord],),
            "tags": ([str],),
            "update_records": ([LLMObsDatasetBatchUpdateUpdateRecord],),
        }

    attribute_map = {
        "create_new_version": "create_new_version",
        "delete_records": "delete_records",
        "insert_records": "insert_records",
        "tags": "tags",
        "update_records": "update_records",
    }

    def __init__(
        self_,
        create_new_version: Union[bool, UnsetType] = unset,
        delete_records: Union[List[str], UnsetType] = unset,
        insert_records: Union[List[LLMObsDatasetBatchUpdateInsertRecord], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        update_records: Union[List[LLMObsDatasetBatchUpdateUpdateRecord], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for batch-updating records in an LLM Observability dataset.

        :param create_new_version: Whether to create a new dataset version when applying the batch update. Defaults to ``true``.
        :type create_new_version: bool, optional

        :param delete_records: Record IDs to delete.
        :type delete_records: [str], optional

        :param insert_records: Records to insert.
        :type insert_records: [LLMObsDatasetBatchUpdateInsertRecord], optional

        :param tags: List of tag strings.
        :type tags: [str], optional

        :param update_records: Records to update by ID.
        :type update_records: [LLMObsDatasetBatchUpdateUpdateRecord], optional
        """
        if create_new_version is not unset:
            kwargs["create_new_version"] = create_new_version
        if delete_records is not unset:
            kwargs["delete_records"] = delete_records
        if insert_records is not unset:
            kwargs["insert_records"] = insert_records
        if tags is not unset:
            kwargs["tags"] = tags
        if update_records is not unset:
            kwargs["update_records"] = update_records
        super().__init__(kwargs)
