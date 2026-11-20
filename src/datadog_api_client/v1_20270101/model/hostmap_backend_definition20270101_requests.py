# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class HostmapBackendDefinition20270101Requests(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param fill: Test-only generated schema for the dashboard versioning proof of concept.
        :type fill: HostmapTileDefFillRequest, optional

        :param size: Test-only generated schema for the dashboard versioning proof of concept.
        :type size: HostmapTileDefSizeRequest, optional

        :param child: Test-only generated schema for the dashboard versioning proof of concept.
        :type child: HostmapInfrastructureRequest, optional

        :param conditional_formats: Test-only generated schema for the dashboard versioning proof of concept.
        :type conditional_formats: [ThresholdFormattingRule], optional

        :param enrichments: Test-only generated schema for the dashboard versioning proof of concept.
        :type enrichments: [HostmapScalarFormulaRequest]

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [HostmapGroupBy], optional

        :param no_group_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_group_hosts: bool, optional

        :param no_metric_hosts: Test-only generated schema for the dashboard versioning proof of concept.
        :type no_metric_hosts: bool, optional

        :param node_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type node_type: HostmapNodeType

        :param request_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type request_type: HostmapInfrastructureRequestRequestType

        :param style: Test-only generated schema for the dashboard versioning proof of concept.
        :type style: HostmapStyle, optional

        :param limit: Test-only generated schema for the dashboard versioning proof of concept.
        :type limit: float, optional

        :param projection: Test-only generated schema for the dashboard versioning proof of concept.
        :type projection: HostmapProjection

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: DatasetListQuery
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.metric_hostmap_requests import MetricHostmapRequests
        from datadog_api_client.v1_20270101.model.hostmap_infrastructure_request import HostmapInfrastructureRequest
        from datadog_api_client.v1_20270101.model.hostmap_data_projection_request import HostmapDataProjectionRequest

        return {
            "oneOf": [
                MetricHostmapRequests,
                HostmapInfrastructureRequest,
                HostmapDataProjectionRequest,
            ],
        }
