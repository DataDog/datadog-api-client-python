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
    from datadog_api_client.v2.model.custom_costs_file_update_attributes import CustomCostsFileUpdateAttributes
    from datadog_api_client.v2.model.custom_costs_file_update_type import CustomCostsFileUpdateType


class CustomCostsFileUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_costs_file_update_attributes import CustomCostsFileUpdateAttributes
        from datadog_api_client.v2.model.custom_costs_file_update_type import CustomCostsFileUpdateType

        return {
            "attributes": (CustomCostsFileUpdateAttributes,),
            "id": (str,),
            "type": (CustomCostsFileUpdateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: CustomCostsFileUpdateAttributes, id: str, type: CustomCostsFileUpdateType, **kwargs
    ):
        """
        Custom Costs file to update.

        :param attributes: Attributes of a Custom Costs file that can be updated.
        :type attributes: CustomCostsFileUpdateAttributes

        :param id: ID of the Custom Costs file.
        :type id: str

        :param type: Type of the Custom Costs file resource.
        :type type: CustomCostsFileUpdateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
