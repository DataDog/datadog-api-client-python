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
    from datadog_api_client.v2.model.dataset_request import DatasetRequest


class DatasetCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_request import DatasetRequest

        return {
            "data": (DatasetRequest,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DatasetRequest, **kwargs):
        """
        Create request for a dataset.

        :param data: **Datasets Object Constraints**

            *
              **Tag limit per dataset** :

              * Each restricted dataset supports a maximum of 10 key:value pairs per product.

            *
              **Tag key rules per telemetry type** :

              * Only one tag key or attribute may be used to define access within a single telemetry type.
              * The same or different tag key may be used across different telemetry types.

            *
              **Tag value uniqueness** :

              * Tag values must be unique within a single dataset.
              * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.
        :type data: DatasetRequest
        """
        super().__init__(kwargs)

        self_.data = data
