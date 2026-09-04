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
    from datadog_api_client.v2.model.dem_batch_get_journeys_attributes import DemBatchGetJourneysAttributes
    from datadog_api_client.v2.model.dem_batch_get_journeys_request_type import DemBatchGetJourneysRequestType


class DemBatchGetJourneysData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_batch_get_journeys_attributes import DemBatchGetJourneysAttributes
        from datadog_api_client.v2.model.dem_batch_get_journeys_request_type import DemBatchGetJourneysRequestType

        return {
            "attributes": (DemBatchGetJourneysAttributes,),
            "type": (DemBatchGetJourneysRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DemBatchGetJourneysAttributes, type: DemBatchGetJourneysRequestType, **kwargs):
        """
        Data object for a batch get journeys request.

        :param attributes: Attributes for a batch get journeys request.
        :type attributes: DemBatchGetJourneysAttributes

        :param type: The resource type for a request to retrieve DEM journeys by test suite IDs.
        :type type: DemBatchGetJourneysRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
