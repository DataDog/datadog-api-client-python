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
    from datadog_api_client.v2.model.salesforce_incidents_organization_response_attributes import (
        SalesforceIncidentsOrganizationResponseAttributes,
    )
    from datadog_api_client.v2.model.salesforce_incidents_organization_type import SalesforceIncidentsOrganizationType


class SalesforceIncidentsOrganizationResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.salesforce_incidents_organization_response_attributes import (
            SalesforceIncidentsOrganizationResponseAttributes,
        )
        from datadog_api_client.v2.model.salesforce_incidents_organization_type import (
            SalesforceIncidentsOrganizationType,
        )

        return {
            "attributes": (SalesforceIncidentsOrganizationResponseAttributes,),
            "id": (str,),
            "type": (SalesforceIncidentsOrganizationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SalesforceIncidentsOrganizationResponseAttributes,
        id: str,
        type: SalesforceIncidentsOrganizationType,
        **kwargs,
    ):
        """
        Salesforce organization data from a response.

        :param attributes: Attributes of a Salesforce organization connected to the Datadog Salesforce integration.
        :type attributes: SalesforceIncidentsOrganizationResponseAttributes

        :param id: The Datadog-assigned ID of the connected Salesforce organization.
        :type id: str

        :param type: Salesforce organization resource type.
        :type type: SalesforceIncidentsOrganizationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
