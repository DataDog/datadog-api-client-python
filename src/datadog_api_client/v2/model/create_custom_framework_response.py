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
    from datadog_api_client.v2.model.partial_custom_framework_data import PartialCustomFrameworkData


class CreateCustomFrameworkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.partial_custom_framework_data import PartialCustomFrameworkData

        return {
            "data": (PartialCustomFrameworkData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PartialCustomFrameworkData, **kwargs):
        """
        Response object to create a custom framework.

        :param data: Contains type and attributes for custom frameworks.
        :type data: PartialCustomFrameworkData
        """
        super().__init__(kwargs)

        self_.data = data
