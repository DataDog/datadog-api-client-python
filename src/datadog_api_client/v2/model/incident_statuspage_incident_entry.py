# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentStatuspageIncidentEntry(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "incident_id": (str,),
            "page_id": (str,),
            "redirect_url": (str,),
        }

    attribute_map = {
        "incident_id": "incident_id",
        "page_id": "page_id",
        "redirect_url": "redirect_url",
    }

    def __init__(self_, incident_id: str, page_id: str, redirect_url: Union[str, UnsetType] = unset, **kwargs):
        """
        A Statuspage incident entry.

        :param incident_id: The Datadog incident identifier.
        :type incident_id: str

        :param page_id: The Statuspage page identifier.
        :type page_id: str

        :param redirect_url: The URL of the Statuspage incident.
        :type redirect_url: str, optional
        """
        if redirect_url is not unset:
            kwargs["redirect_url"] = redirect_url
        super().__init__(kwargs)

        self_.incident_id = incident_id
        self_.page_id = page_id
