# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class IncidentResponderDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created": (datetime,),
            "external_id": (str, none_type),
            "external_source": (str, none_type),
            "is_billable": (bool,),
            "last_active": (datetime, none_type),
            "meta": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
                none_type,
            ),
            "modified": (datetime,),
        }

    attribute_map = {
        "created": "created",
        "external_id": "external_id",
        "external_source": "external_source",
        "is_billable": "is_billable",
        "last_active": "last_active",
        "meta": "meta",
        "modified": "modified",
    }

    def __init__(
        self_,
        created: datetime,
        is_billable: bool,
        modified: datetime,
        external_id: Union[str, none_type, UnsetType] = unset,
        external_source: Union[str, none_type, UnsetType] = unset,
        last_active: Union[datetime, none_type, UnsetType] = unset,
        meta: Union[Dict[str, Any], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an incident responder in a response.

        :param created: Timestamp when the responder was created.
        :type created: datetime

        :param external_id: The external ID of the responder.
        :type external_id: str, none_type, optional

        :param external_source: The external source of the responder.
        :type external_source: str, none_type, optional

        :param is_billable: Whether this responder counts toward billing.
        :type is_billable: bool

        :param last_active: Timestamp when the responder was last active.
        :type last_active: datetime, none_type, optional

        :param meta: Additional metadata for the responder.
        :type meta: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, none_type, optional

        :param modified: Timestamp when the responder was last modified.
        :type modified: datetime
        """
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if external_source is not unset:
            kwargs["external_source"] = external_source
        if last_active is not unset:
            kwargs["last_active"] = last_active
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.created = created
        self_.is_billable = is_billable
        self_.modified = modified
