# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dataset_response import DatasetResponse


class DatasetResponseSingle(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_response import DatasetResponse

        return {
            "data": (DatasetResponse,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[DatasetResponse, UnsetType] = unset, **kwargs):
        """
        Response containing a single dataset object.

        :param data: **Datasets Object Constraints**

            *
              **Tag Limit per Dataset** :

              * Each restricted dataset supports a maximum of 10 key:value pairs per product.

            *
              **Tag Key Rules per Telemetry Type** :

              * Only one tag key or attribute may be used to define access within a single telemetry type.
              * The same or different tag key may be used across different telemetry types.

            *
              **Tag Value Uniqueness** :

              * Tag values must be unique within a single dataset.
              * A tag value used in one dataset cannot be reused in another dataset of the same telemetry type.
        :type data: DatasetResponse, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
