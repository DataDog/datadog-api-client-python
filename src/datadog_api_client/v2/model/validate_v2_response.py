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
    from datadog_api_client.v2.model.validate_v2_data import ValidateV2Data


class ValidateV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.validate_v2_data import ValidateV2Data

        return {
            "data": (ValidateV2Data,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ValidateV2Data, **kwargs):
        """
        Response for the API key validation endpoint.

        :param data: Data object containing the API key validation result.
        :type data: ValidateV2Data
        """
        super().__init__(kwargs)

        self_.data = data
