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
    from datadog_api_client.v2.model.dataset_attributes import DatasetAttributes


class Dataset(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_attributes import DatasetAttributes

        return {
            "attributes": (DatasetAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DatasetAttributes, type: str, id: Union[str, UnsetType] = unset, **kwargs):
        """
        Dataset object.

        :param attributes: Dataset metadata and configuration(s).
        :type attributes: DatasetAttributes

        :param id: Unique identifier for the dataset.
        :type id: str, optional

        :param type: Resource type, always "dataset".
        :type type: str
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
