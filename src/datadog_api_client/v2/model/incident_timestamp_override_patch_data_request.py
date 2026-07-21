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
    from datadog_api_client.v2.model.incident_timestamp_override_patch_data_attributes_request import (
        IncidentTimestampOverridePatchDataAttributesRequest,
    )
    from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType


class IncidentTimestampOverridePatchDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_timestamp_override_patch_data_attributes_request import (
            IncidentTimestampOverridePatchDataAttributesRequest,
        )
        from datadog_api_client.v2.model.incident_timestamp_override_type import IncidentTimestampOverrideType

        return {
            "attributes": (IncidentTimestampOverridePatchDataAttributesRequest,),
            "id": (UUID,),
            "type": (IncidentTimestampOverrideType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: UUID,
        type: IncidentTimestampOverrideType,
        attributes: Union[IncidentTimestampOverridePatchDataAttributesRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Timestamp override data in a patch request.

        :param attributes: Attributes for patching a timestamp override.
        :type attributes: IncidentTimestampOverridePatchDataAttributesRequest, optional

        :param id: The timestamp override identifier.
        :type id: UUID

        :param type: Incident timestamp override resource type.
        :type type: IncidentTimestampOverrideType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
