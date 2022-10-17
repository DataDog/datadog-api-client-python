# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType
from datadog_api_client.v2.model.opsgenie_service_update_attributes import OpsgenieServiceUpdateAttributes
from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType


@dataclass
class OpsgenieServiceUpdateDataJSON:
    id: str
    custom_url: Union[str, none_type, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    opsgenie_api_key: Union[str, UnsetType] = unset
    region: Union[OpsgenieServiceRegionType, UnsetType] = unset


class OpsgenieServiceUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_type import OpsgenieServiceType

        return {
            "attributes": (OpsgenieServiceUpdateAttributes,),
            "id": (str,),
            "type": (OpsgenieServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = OpsgenieServiceUpdateDataJSON

    def __init__(self_, attributes: OpsgenieServiceUpdateAttributes, id: str, type: OpsgenieServiceType, **kwargs):
        """
        Opsgenie service for an update request.

        :param attributes: The Opsgenie service attributes for an update request.
        :type attributes: OpsgenieServiceUpdateAttributes

        :param id: The ID of the Opsgenie service.
        :type id: str

        :param type: Opsgenie service resource type.
        :type type: OpsgenieServiceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
