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
    from datadog_api_client.v2.model.hamr_org_connection_attributes_response import HamrOrgConnectionAttributesResponse
    from datadog_api_client.v2.model.hamr_org_connection_type import HamrOrgConnectionType


class HamrOrgConnectionDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.hamr_org_connection_attributes_response import (
            HamrOrgConnectionAttributesResponse,
        )
        from datadog_api_client.v2.model.hamr_org_connection_type import HamrOrgConnectionType

        return {
            "attributes": (HamrOrgConnectionAttributesResponse,),
            "id": (str,),
            "type": (HamrOrgConnectionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: HamrOrgConnectionAttributesResponse, id: str, type: HamrOrgConnectionType, **kwargs
    ):
        """


        :param attributes:
        :type attributes: HamrOrgConnectionAttributesResponse

        :param id: The organization UUID for this HAMR connection.
        :type id: str

        :param type: Type of the HAMR organization connection resource.
        :type type: HamrOrgConnectionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
