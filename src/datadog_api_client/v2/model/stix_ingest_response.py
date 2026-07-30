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
    from datadog_api_client.v2.model.stix_ingest_response_data import STIXIngestResponseData


class STIXIngestResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stix_ingest_response_data import STIXIngestResponseData

        return {
            "data": (STIXIngestResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: STIXIngestResponseData, **kwargs):
        """
        The response from a completed STIX ingestion request.

        :param data: The JSON:API resource describing the completed STIX ingestion request.
        :type data: STIXIngestResponseData
        """
        super().__init__(kwargs)

        self_.data = data
