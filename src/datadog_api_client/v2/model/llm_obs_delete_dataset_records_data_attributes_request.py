# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteDatasetRecordsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "record_ids": ([str],),
        }

    attribute_map = {
        "record_ids": "record_ids",
    }

    def __init__(self_, record_ids: List[str], **kwargs):
        """
        Attributes for deleting records from an LLM Observability dataset.

        :param record_ids: List of record IDs to delete.
        :type record_ids: [str]
        """
        super().__init__(kwargs)

        self_.record_ids = record_ids
