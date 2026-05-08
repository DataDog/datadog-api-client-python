# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_restriction_response_data import DatasetRestrictionResponseData


class DatasetRestrictionsListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_restriction_response_data import DatasetRestrictionResponseData

        return {
            "data": ([DatasetRestrictionResponseData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[DatasetRestrictionResponseData], **kwargs):
        """
        Response containing the list of all dataset restriction configurations for the
        organization, one per product type.

        :param data: An array of dataset restriction objects, one for each configured product type.
        :type data: [DatasetRestrictionResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
