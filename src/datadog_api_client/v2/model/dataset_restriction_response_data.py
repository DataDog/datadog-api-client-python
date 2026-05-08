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
    from datadog_api_client.v2.model.dataset_restriction_response_attributes import DatasetRestrictionResponseAttributes
    from datadog_api_client.v2.model.dataset_restrictions_type import DatasetRestrictionsType


class DatasetRestrictionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_restriction_response_attributes import (
            DatasetRestrictionResponseAttributes,
        )
        from datadog_api_client.v2.model.dataset_restrictions_type import DatasetRestrictionsType

        return {
            "attributes": (DatasetRestrictionResponseAttributes,),
            "id": (str,),
            "type": (DatasetRestrictionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: DatasetRestrictionResponseAttributes, id: str, type: DatasetRestrictionsType, **kwargs
    ):
        """
        A single dataset restriction configuration for one product type.

        :param attributes: The current configuration of a dataset restriction, including restriction mode,
            ownership mode, and exempt principals.
        :type attributes: DatasetRestrictionResponseAttributes

        :param id: The Datadog product type this restriction applies to (for example, ``rum`` , ``apm`` , or ``logs`` ).
        :type id: str

        :param type: JSON:API resource type for dataset restrictions.
        :type type: DatasetRestrictionsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
