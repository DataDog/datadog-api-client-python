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
    from datadog_api_client.v2.model.custom_framework_metadata import CustomFrameworkMetadata


class DeleteCustomFrameworkResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_framework_metadata import CustomFrameworkMetadata

        return {
            "data": (CustomFrameworkMetadata,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CustomFrameworkMetadata, **kwargs):
        """
        Response object to delete a custom framework.

        :param data: Metadata for custom frameworks.
        :type data: CustomFrameworkMetadata
        """
        super().__init__(kwargs)

        self_.data = data
