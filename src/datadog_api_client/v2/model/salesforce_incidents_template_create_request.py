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
    from datadog_api_client.v2.model.salesforce_incidents_template_create_data import (
        SalesforceIncidentsTemplateCreateData,
    )


class SalesforceIncidentsTemplateCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.salesforce_incidents_template_create_data import (
            SalesforceIncidentsTemplateCreateData,
        )

        return {
            "data": (SalesforceIncidentsTemplateCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: SalesforceIncidentsTemplateCreateData, **kwargs):
        """
        Create request for a Salesforce incident template.

        :param data: Salesforce incident template data for a create request.
        :type data: SalesforceIncidentsTemplateCreateData
        """
        super().__init__(kwargs)

        self_.data = data
