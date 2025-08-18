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
    from datadog_api_client.v2.model.dataset_attributes_response import DatasetAttributesResponse
    from datadog_api_client.v2.model.dataset_type import DatasetType


class DatasetResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_attributes_response import DatasetAttributesResponse
        from datadog_api_client.v2.model.dataset_type import DatasetType

        return {
            "attributes": (DatasetAttributesResponse,),
            "id": (str,),
            "type": (DatasetType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[DatasetAttributesResponse, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[DatasetType, UnsetType] = unset,
        **kwargs,
    ):
        """
        **Datasets Object Constraints**

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

        :param attributes: Dataset metadata and configuration(s).
        :type attributes: DatasetAttributesResponse, optional

        :param id: Unique identifier for the dataset.
        :type id: str, optional

        :param type: Resource type, always set to ``dataset``.
        :type type: DatasetType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
