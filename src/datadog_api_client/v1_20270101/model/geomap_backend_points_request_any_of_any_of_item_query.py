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
    from datadog_api_client.v1_20270101.model.network_devices_data_source_name import NetworkDevicesDataSourceName


class GeomapBackendPointsRequestAnyOfAnyOfItemQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.network_devices_data_source_name import NetworkDevicesDataSourceName

        return {
            "data_source": (NetworkDevicesDataSourceName,),
            "query_string": (str,),
        }

    attribute_map = {
        "data_source": "data_source",
        "query_string": "query_string",
    }

    def __init__(self_, data_source: NetworkDevicesDataSourceName, query_string: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: NetworkDevicesDataSourceName

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
