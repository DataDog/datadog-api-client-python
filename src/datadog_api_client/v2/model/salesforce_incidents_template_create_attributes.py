# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.salesforce_incidents_template_priority import SalesforceIncidentsTemplatePriority


class SalesforceIncidentsTemplateCreateAttributes(ModelNormal):
    validations = {
        "description": {
            "max_length": 2048,
            "min_length": 1,
        },
        "name": {
            "max_length": 100,
            "min_length": 1,
        },
        "owner_id": {
            "max_length": 255,
            "min_length": 1,
        },
        "subject": {
            "max_length": 255,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.salesforce_incidents_template_priority import (
            SalesforceIncidentsTemplatePriority,
        )

        return {
            "description": (str,),
            "name": (str,),
            "owner_id": (str,),
            "priority": (SalesforceIncidentsTemplatePriority,),
            "salesforce_org_id": (UUID,),
            "subject": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "owner_id": "owner_id",
        "priority": "priority",
        "salesforce_org_id": "salesforce_org_id",
        "subject": "subject",
    }

    def __init__(
        self_,
        description: str,
        name: str,
        owner_id: str,
        priority: SalesforceIncidentsTemplatePriority,
        salesforce_org_id: UUID,
        subject: str,
        **kwargs,
    ):
        """
        Salesforce incident template attributes for a create request.

        :param description: Long-form description body for Salesforce incidents created from this template.
        :type description: str

        :param name: Human-readable name for this incident template. Must be unique within your organization.
        :type name: str

        :param owner_id: The Salesforce user ID that owns incidents created from this template.
        :type owner_id: str

        :param priority: Priority of the Salesforce incident created from this template.
        :type priority: SalesforceIncidentsTemplatePriority

        :param salesforce_org_id: The Datadog-assigned ID of the Salesforce organization this template belongs to.
        :type salesforce_org_id: UUID

        :param subject: Subject line for Salesforce incidents created from this template.
        :type subject: str
        """
        super().__init__(kwargs)

        self_.description = description
        self_.name = name
        self_.owner_id = owner_id
        self_.priority = priority
        self_.salesforce_org_id = salesforce_org_id
        self_.subject = subject
