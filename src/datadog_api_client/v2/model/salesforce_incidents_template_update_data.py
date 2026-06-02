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
    from datadog_api_client.v2.model.salesforce_incidents_template_update_attributes import (
        SalesforceIncidentsTemplateUpdateAttributes,
    )
    from datadog_api_client.v2.model.salesforce_incidents_template_type import SalesforceIncidentsTemplateType


class SalesforceIncidentsTemplateUpdateData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.salesforce_incidents_template_update_attributes import (
            SalesforceIncidentsTemplateUpdateAttributes,
        )
        from datadog_api_client.v2.model.salesforce_incidents_template_type import SalesforceIncidentsTemplateType

        return {
            "attributes": (SalesforceIncidentsTemplateUpdateAttributes,),
            "id": (str,),
            "type": (SalesforceIncidentsTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SalesforceIncidentsTemplateUpdateAttributes,
        id: str,
        type: SalesforceIncidentsTemplateType,
        **kwargs,
    ):
        """
        Salesforce incident template data for an update request.

        :param attributes: Salesforce incident template attributes for an update request.
        :type attributes: SalesforceIncidentsTemplateUpdateAttributes

        :param id: The ID of the Salesforce incident template being updated. Must match the path parameter.
        :type id: str

        :param type: Salesforce incident template resource type.
        :type type: SalesforceIncidentsTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
