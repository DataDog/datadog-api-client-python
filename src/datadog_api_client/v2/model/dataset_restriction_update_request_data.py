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
    from datadog_api_client.v2.model.dataset_restriction_update_request_attributes import (
        DatasetRestrictionUpdateRequestAttributes,
    )
    from datadog_api_client.v2.model.dataset_restrictions_type import DatasetRestrictionsType


class DatasetRestrictionUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dataset_restriction_update_request_attributes import (
            DatasetRestrictionUpdateRequestAttributes,
        )
        from datadog_api_client.v2.model.dataset_restrictions_type import DatasetRestrictionsType

        return {
            "attributes": (DatasetRestrictionUpdateRequestAttributes,),
            "type": (DatasetRestrictionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DatasetRestrictionUpdateRequestAttributes, type: DatasetRestrictionsType, **kwargs):
        """
        Data object for a dataset restriction update.

        :param attributes: Editable attributes of a dataset restriction. Only ``restriction_mode`` is required;
            omitted optional fields retain their current values.
        :type attributes: DatasetRestrictionUpdateRequestAttributes

        :param type: JSON:API resource type for dataset restrictions.
        :type type: DatasetRestrictionsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
