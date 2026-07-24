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
    from datadog_api_client.v2.model.incident_impact_patch_attributes import IncidentImpactPatchAttributes
    from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType


class IncidentImpactPatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_impact_patch_attributes import IncidentImpactPatchAttributes
        from datadog_api_client.v2.model.incident_impact_type import IncidentImpactType

        return {
            "attributes": (IncidentImpactPatchAttributes,),
            "type": (IncidentImpactType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, type: IncidentImpactType, attributes: Union[IncidentImpactPatchAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Incident impact data for a patch request.

        :param attributes: The incident impact's attributes for a patch request. All fields are optional.
        :type attributes: IncidentImpactPatchAttributes, optional

        :param type: Incident impact resource type.
        :type type: IncidentImpactType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
