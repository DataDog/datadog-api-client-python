# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteAnnotationQueueInteractionsDataAttributesRequest(ModelNormal):
    validations = {
        "interaction_ids": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "interaction_ids": ([str],),
        }

    attribute_map = {
        "interaction_ids": "interaction_ids",
    }

    def __init__(self_, interaction_ids: List[str], **kwargs):
        """
        Attributes for deleting interactions from an annotation queue.

        :param interaction_ids: List of interaction IDs to delete. Must contain at least one item.
        :type interaction_ids: [str]
        """
        super().__init__(kwargs)

        self_.interaction_ids = interaction_ids
