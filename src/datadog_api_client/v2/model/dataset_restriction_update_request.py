# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_restriction_update_request_data import DatasetRestrictionUpdateRequestData


class DatasetRestrictionUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_restriction_update_request_data import (
            DatasetRestrictionUpdateRequestData,
        )

        return {
            "data": (DatasetRestrictionUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DatasetRestrictionUpdateRequestData, **kwargs):
        """
        Payload for updating a dataset restriction configuration.

        :param data: Data object for a dataset restriction update.
        :type data: DatasetRestrictionUpdateRequestData
        """
        super().__init__(kwargs)

        self_.data = data
