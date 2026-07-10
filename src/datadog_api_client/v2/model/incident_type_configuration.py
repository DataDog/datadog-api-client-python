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
    from datadog_api_client.v2.model.incident_type_slug_source import IncidentTypeSlugSource


class IncidentTypeConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_type_slug_source import IncidentTypeSlugSource

        return {
            "allow_incident_deletion": (bool,),
            "allow_workflows": (bool,),
            "create_message": (str,),
            "editable_timestamps": (bool,),
            "private_incidents": (bool,),
            "private_incidents_by_default": (bool,),
            "slug_source": (IncidentTypeSlugSource,),
            "test_incidents": (bool,),
        }

    attribute_map = {
        "allow_incident_deletion": "allow_incident_deletion",
        "allow_workflows": "allow_workflows",
        "create_message": "create_message",
        "editable_timestamps": "editable_timestamps",
        "private_incidents": "private_incidents",
        "private_incidents_by_default": "private_incidents_by_default",
        "slug_source": "slug_source",
        "test_incidents": "test_incidents",
    }

    def __init__(
        self_,
        allow_incident_deletion: Union[bool, UnsetType] = unset,
        allow_workflows: Union[bool, UnsetType] = unset,
        create_message: Union[str, UnsetType] = unset,
        editable_timestamps: Union[bool, UnsetType] = unset,
        private_incidents: Union[bool, UnsetType] = unset,
        private_incidents_by_default: Union[bool, UnsetType] = unset,
        slug_source: Union[IncidentTypeSlugSource, UnsetType] = unset,
        test_incidents: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The incident-type-scoped behavior settings. All fields are optional on update. Any field omitted from a PATCH request keeps its current value. This object is read-only on the incident type resource itself and is only mutated through the update (PATCH) endpoint.

        :param allow_incident_deletion: Whether incidents of this type can be deleted.
        :type allow_incident_deletion: bool, optional

        :param allow_workflows: Whether automation workflows can be triggered for incidents of this type.
        :type allow_workflows: bool, optional

        :param create_message: An optional message shown to users when they declare an incident of this type.
        :type create_message: str, optional

        :param editable_timestamps: Whether responders can edit incident timestamps for incidents of this type.
        :type editable_timestamps: bool, optional

        :param private_incidents: Whether responders can create private incidents of this type. This is an opt-in setting, distinct from ``private_incidents_by_default`` , which controls whether incidents are created private automatically.
        :type private_incidents: bool, optional

        :param private_incidents_by_default: Whether incidents of this type are created as private by default.
        :type private_incidents_by_default: bool, optional

        :param slug_source: When set to ``servicenow`` , incidents will display the ServiceNow record ID instead of the public ID. If no ServiceNow integration exists, the public ID will be displayed.
        :type slug_source: IncidentTypeSlugSource, optional

        :param test_incidents: Whether incidents of this type are treated as test incidents.
        :type test_incidents: bool, optional
        """
        if allow_incident_deletion is not unset:
            kwargs["allow_incident_deletion"] = allow_incident_deletion
        if allow_workflows is not unset:
            kwargs["allow_workflows"] = allow_workflows
        if create_message is not unset:
            kwargs["create_message"] = create_message
        if editable_timestamps is not unset:
            kwargs["editable_timestamps"] = editable_timestamps
        if private_incidents is not unset:
            kwargs["private_incidents"] = private_incidents
        if private_incidents_by_default is not unset:
            kwargs["private_incidents_by_default"] = private_incidents_by_default
        if slug_source is not unset:
            kwargs["slug_source"] = slug_source
        if test_incidents is not unset:
            kwargs["test_incidents"] = test_incidents
        super().__init__(kwargs)
