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
    from datadog_api_client.v2.model.update_variant_data import UpdateVariantData


class UpdateVariantRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_variant_data import UpdateVariantData

        return {
            "data": (UpdateVariantData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpdateVariantData, **kwargs):
        """
        Request to update an existing variant's name and value.

        :param data: Data for updating a variant.
        :type data: UpdateVariantData
        """
        super().__init__(kwargs)

        self_.data = data
