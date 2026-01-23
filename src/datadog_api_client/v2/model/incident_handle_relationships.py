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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_handle_relationship import IncidentHandleRelationship


class IncidentHandleRelationships(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_handle_relationship import IncidentHandleRelationship

        return {
            "commander_user": (IncidentHandleRelationship,),
            "created_by_user": (IncidentHandleRelationship,),
            "incident_type": (IncidentHandleRelationship,),
            "last_modified_by_user": (IncidentHandleRelationship,),
        }

    attribute_map = {
        "commander_user": "commander_user",
        "created_by_user": "created_by_user",
        "incident_type": "incident_type",
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_,
        created_by_user: IncidentHandleRelationship,
        incident_type: IncidentHandleRelationship,
        last_modified_by_user: IncidentHandleRelationship,
        commander_user: Union[IncidentHandleRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param commander_user:
        :type commander_user: IncidentHandleRelationship, optional

        :param created_by_user:
        :type created_by_user: IncidentHandleRelationship

        :param incident_type:
        :type incident_type: IncidentHandleRelationship

        :param last_modified_by_user:
        :type last_modified_by_user: IncidentHandleRelationship
        """
        if commander_user is not unset:
            kwargs["commander_user"] = commander_user
        super().__init__(kwargs)

        self_.created_by_user = created_by_user
        self_.incident_type = incident_type
        self_.last_modified_by_user = last_modified_by_user
