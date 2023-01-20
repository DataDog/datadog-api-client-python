# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.fastly_service_response import FastlyServiceResponse


class FastlyServicesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_service_response import FastlyServiceResponse

        return {
            "data": ([FastlyServiceResponse],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[FastlyServiceResponse], UnsetType] = unset, **kwargs):
        """
        The expected response schema when getting Fastly services.

        :param data: The JSON:API data schema.
        :type data: [FastlyServiceResponse], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
