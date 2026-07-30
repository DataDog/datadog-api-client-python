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
    from datadog_api_client.v2.model.stix_ingest_response_attributes import STIXIngestResponseAttributes
    from datadog_api_client.v2.model.stix_ingest_response_type import STIXIngestResponseType


class STIXIngestResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.stix_ingest_response_attributes import STIXIngestResponseAttributes
        from datadog_api_client.v2.model.stix_ingest_response_type import STIXIngestResponseType

        return {
            "attributes": (STIXIngestResponseAttributes,),
            "id": (str,),
            "type": (STIXIngestResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: STIXIngestResponseAttributes, id: str, type: STIXIngestResponseType, **kwargs):
        """
        The JSON:API resource describing the completed STIX ingestion request.

        :param attributes: Counters describing the result of the STIX ingestion request.
        :type attributes: STIXIngestResponseAttributes

        :param id: The normalized vendor identifier.
        :type id: str

        :param type: The STIX ingestion resource type.
        :type type: STIXIngestResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
