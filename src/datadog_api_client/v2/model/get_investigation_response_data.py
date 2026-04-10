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
    from datadog_api_client.v2.model.get_investigation_response_data_attributes import (
        GetInvestigationResponseDataAttributes,
    )
    from datadog_api_client.v2.model.investigation_type import InvestigationType


class GetInvestigationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_investigation_response_data_attributes import (
            GetInvestigationResponseDataAttributes,
        )
        from datadog_api_client.v2.model.investigation_type import InvestigationType

        return {
            "attributes": (GetInvestigationResponseDataAttributes,),
            "id": (str,),
            "type": (InvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: GetInvestigationResponseDataAttributes, id: str, type: InvestigationType, **kwargs):
        """
        Data for the get investigation response.

        :param attributes: Attributes of the investigation.
        :type attributes: GetInvestigationResponseDataAttributes

        :param id: The unique identifier of the investigation.
        :type id: str

        :param type: The resource type for investigations.
        :type type: InvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
