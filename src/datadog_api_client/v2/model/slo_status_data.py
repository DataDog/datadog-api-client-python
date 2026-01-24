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
    from datadog_api_client.v2.model.slo_status_data_attributes import SloStatusDataAttributes
    from datadog_api_client.v2.model.slo_status_type import SloStatusType


class SloStatusData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.slo_status_data_attributes import SloStatusDataAttributes
        from datadog_api_client.v2.model.slo_status_type import SloStatusType

        return {
            "attributes": (SloStatusDataAttributes,),
            "id": (str,),
            "type": (SloStatusType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: SloStatusDataAttributes, id: str, type: SloStatusType, **kwargs):
        """
        The data portion of the SLO status response.

        :param attributes: The attributes of the SLO status.
        :type attributes: SloStatusDataAttributes

        :param id: The ID of the SLO.
        :type id: str

        :param type: The type of the SLO status resource.
        :type type: SloStatusType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
