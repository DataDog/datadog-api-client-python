# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.opsgenie_service_response_data import OpsgenieServiceResponseData
    from datadog_api_client.v2.model.opsgenie_service_region_type import OpsgenieServiceRegionType


@dataclass
class OpsgenieServicesResponseJSON:
    id: str
    custom_url: Union[str, none_type, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    region: Union[OpsgenieServiceRegionType, UnsetType] = unset


class OpsgenieServicesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_service_response_data import OpsgenieServiceResponseData

        return {
            "data": ([OpsgenieServiceResponseData],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = OpsgenieServicesResponseJSON

    def __init__(self_, data: List[OpsgenieServiceResponseData], **kwargs):
        """
        Response with a list of Opsgenie services.

        :param data: An array of Opsgenie services.
        :type data: [OpsgenieServiceResponseData]
        """
        super().__init__(kwargs)

        self_.data = data
