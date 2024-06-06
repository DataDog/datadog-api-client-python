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
    from datadog_api_client.v2.model.awsx_ray_services_list import AWSXRayServicesList


class AWSTraces(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.awsx_ray_services_list import AWSXRayServicesList

        return {
            "xray_services": (AWSXRayServicesList,),
        }

    attribute_map = {
        "xray_services": "xray_services",
    }

    def __init__(self_, xray_services: Union[AWSXRayServicesList, UnsetType] = unset, **kwargs):
        """
        AWS Traces config

        :param xray_services: AWS X-Ray services to collect traces from
        :type xray_services: AWSXRayServicesList, optional
        """
        if xray_services is not unset:
            kwargs["xray_services"] = xray_services
        super().__init__(kwargs)
