# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.salesforce_incidents_template_priority import SalesforceIncidentsTemplatePriority


class SalesforceIncidentsTemplateResponseAttributes(ModelNormal):
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
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        owner_id: Union[str, UnsetType] = unset,
        priority: Union[SalesforceIncidentsTemplatePriority, UnsetType] = unset,
        salesforce_org_id: Union[UUID, UnsetType] = unset,
        subject: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Salesforce incident template attributes returned by the API.

        :param description: Long-form description body for Salesforce incidents created from this template.
        :type description: str, optional

        :param name: Human-readable name for this incident template.
        :type name: str, optional

        :param owner_id: The Salesforce user ID that owns incidents created from this template.
        :type owner_id: str, optional

        :param priority: Priority of the Salesforce incident created from this template.
        :type priority: SalesforceIncidentsTemplatePriority, optional

        :param salesforce_org_id: The Datadog-assigned ID of the Salesforce organization this template belongs to.
        :type salesforce_org_id: UUID, optional

        :param subject: Subject line for Salesforce incidents created from this template.
        :type subject: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if owner_id is not unset:
            kwargs["owner_id"] = owner_id
        if priority is not unset:
            kwargs["priority"] = priority
        if salesforce_org_id is not unset:
            kwargs["salesforce_org_id"] = salesforce_org_id
        if subject is not unset:
            kwargs["subject"] = subject
        super().__init__(kwargs)
