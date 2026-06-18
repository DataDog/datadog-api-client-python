# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_wif_persona_mapping_data import AwsWifPersonaMappingData


class AwsWifPersonaMappingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_wif_persona_mapping_data import AwsWifPersonaMappingData

        return {
            "data": ([AwsWifPersonaMappingData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[AwsWifPersonaMappingData], **kwargs):
        """
        Response containing a list of AWS WIF persona mappings.

        :param data:
        :type data: [AwsWifPersonaMappingData]
        """
        super().__init__(kwargs)

        self_.data = data
