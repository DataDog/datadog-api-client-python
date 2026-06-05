# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsDeleteAnnotationsDataAttributesRequest(ModelNormal):
    validations = {
        "annotation_ids": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "annotation_ids": ([str],),
        }

    attribute_map = {
        "annotation_ids": "annotation_ids",
    }

    def __init__(self_, annotation_ids: List[str], **kwargs):
        """
        Attributes for deleting annotations.

        :param annotation_ids: IDs of the annotations to delete. Must contain at least one item.
        :type annotation_ids: [str]
        """
        super().__init__(kwargs)

        self_.annotation_ids = annotation_ids
