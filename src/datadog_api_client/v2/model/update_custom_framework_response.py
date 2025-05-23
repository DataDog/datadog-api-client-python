# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.framework_handle_and_version_response_data import (
        FrameworkHandleAndVersionResponseData,
    )


class UpdateCustomFrameworkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.framework_handle_and_version_response_data import (
            FrameworkHandleAndVersionResponseData,
        )

        return {
            "data": (FrameworkHandleAndVersionResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: FrameworkHandleAndVersionResponseData, **kwargs):
        """
        Response object to update a custom framework.

        :param data: Contains type and attributes for custom frameworks.
        :type data: FrameworkHandleAndVersionResponseData
        """
        super().__init__(kwargs)

        self_.data = data
