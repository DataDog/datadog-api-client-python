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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.opsgenie_service_update_data import OpsgenieServiceUpdateData
    from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType


@dataclass
class OpsgenieServiceUpdateRequestJSON:
    id: str
    custom_url: Union[str, none_type, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    opsgenie_api_key: Union[str, UnsetType] = unset
    region: Union[OpsgenieServiceRegionType, UnsetType] = unset


class OpsgenieServiceUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_update_data import OpsgenieServiceUpdateData

        return {
            "data": (OpsgenieServiceUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = OpsgenieServiceUpdateRequestJSON

    def __init__(self_, data: OpsgenieServiceUpdateData, **kwargs):
        """
        Update request for an Opsgenie service.

        :param data: Opsgenie service for an update request.
        :type data: OpsgenieServiceUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
