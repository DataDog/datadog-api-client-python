# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteDatasetsDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dataset_ids": ([str],),
        }

    attribute_map = {
        "dataset_ids": "dataset_ids",
    }

    def __init__(self_, dataset_ids: List[str], **kwargs):
        """
        Attributes for deleting LLM Observability datasets.

        :param dataset_ids: List of dataset IDs to delete.
        :type dataset_ids: [str]
        """
        super().__init__(kwargs)

        self_.dataset_ids = dataset_ids
