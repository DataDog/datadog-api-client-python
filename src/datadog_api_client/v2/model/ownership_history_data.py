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
    from datadog_api_client.v2.model.ownership_history_attributes import OwnershipHistoryAttributes
    from datadog_api_client.v2.model.ownership_history_type import OwnershipHistoryType


class OwnershipHistoryData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_history_attributes import OwnershipHistoryAttributes
        from datadog_api_client.v2.model.ownership_history_type import OwnershipHistoryType

        return {
            "attributes": (OwnershipHistoryAttributes,),
            "id": (str,),
            "type": (OwnershipHistoryType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipHistoryAttributes, id: str, type: OwnershipHistoryType, **kwargs):
        """
        The data wrapper for an ownership history response.

        :param attributes: The attributes of an ownership history response.
        :type attributes: OwnershipHistoryAttributes

        :param id: The resource identifier for which history is returned.
        :type id: str

        :param type: The type of the ownership history resource. The value should always be ``ownership_history``.
        :type type: OwnershipHistoryType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
