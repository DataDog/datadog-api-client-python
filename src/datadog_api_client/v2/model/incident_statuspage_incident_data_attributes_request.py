# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class IncidentStatuspageIncidentDataAttributesRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "body": (str, none_type),
            "components": ({str: (str,)},),
            "deliver_notifications": (bool, none_type),
            "impact": (str, none_type),
            "name": (str, none_type),
            "page_id": (str,),
            "status": (str, none_type),
        }

    attribute_map = {
        "body": "body",
        "components": "components",
        "deliver_notifications": "deliver_notifications",
        "impact": "impact",
        "name": "name",
        "page_id": "page_id",
        "status": "status",
    }

    def __init__(
        self_,
        body: Union[str, none_type, UnsetType] = unset,
        components: Union[Dict[str, str], UnsetType] = unset,
        deliver_notifications: Union[bool, none_type, UnsetType] = unset,
        impact: Union[str, none_type, UnsetType] = unset,
        name: Union[str, none_type, UnsetType] = unset,
        page_id: Union[str, UnsetType] = unset,
        status: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a Statuspage incident.

        :param body: The body text of the Statuspage incident.
        :type body: str, none_type, optional

        :param components: Map of component identifiers to their status.
        :type components: {str: (str,)}, optional

        :param deliver_notifications: Whether to deliver notifications.
        :type deliver_notifications: bool, none_type, optional

        :param impact: The impact level of the incident.
        :type impact: str, none_type, optional

        :param name: The name of the Statuspage incident.
        :type name: str, none_type, optional

        :param page_id: The Statuspage page identifier.
        :type page_id: str, optional

        :param status: The status of the Statuspage incident.
        :type status: str, none_type, optional
        """
        if body is not unset:
            kwargs["body"] = body
        if components is not unset:
            kwargs["components"] = components
        if deliver_notifications is not unset:
            kwargs["deliver_notifications"] = deliver_notifications
        if impact is not unset:
            kwargs["impact"] = impact
        if name is not unset:
            kwargs["name"] = name
        if page_id is not unset:
            kwargs["page_id"] = page_id
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
