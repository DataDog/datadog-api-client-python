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
    from datadog_api_client.v2.model.open_api_endpoint import OpenAPIEndpoint


class UpdateOpenAPIResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_api_endpoint import OpenAPIEndpoint

        return {
            "failed_endpoints": ([OpenAPIEndpoint],),
        }

    attribute_map = {
        "failed_endpoints": "failed_endpoints",
    }

    def __init__(self_, failed_endpoints: Union[List[OpenAPIEndpoint], UnsetType] = unset, **kwargs):
        """
        Attributes for ``UpdateOpenAPI``.

        :param failed_endpoints: List of endpoints which couldn't be parsed.
        :type failed_endpoints: [OpenAPIEndpoint], optional
        """
        if failed_endpoints is not unset:
            kwargs["failed_endpoints"] = failed_endpoints
        super().__init__(kwargs)
