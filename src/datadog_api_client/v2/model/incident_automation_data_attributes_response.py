# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


class IncidentAutomationDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "incident_id": (UUID,),
            "key": (str,),
            "updated_at": (datetime,),
            "value": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "incident_id": "incident_id",
        "key": "key",
        "updated_at": "updated_at",
        "value": "value",
    }

    def __init__(self_, created_at: datetime, incident_id: UUID, key: str, updated_at: datetime, value: str, **kwargs):
        """
        Attributes of incident automation data.

        :param created_at: Timestamp when the data was created.
        :type created_at: datetime

        :param incident_id: The incident identifier.
        :type incident_id: UUID

        :param key: The automation data key.
        :type key: str

        :param updated_at: Timestamp when the data was last updated.
        :type updated_at: datetime

        :param value: The automation data value.
        :type value: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.incident_id = incident_id
        self_.key = key
        self_.updated_at = updated_at
        self_.value = value
