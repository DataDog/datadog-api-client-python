# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
    from datadog_api_client.v1_20270101.model.hostmap_scalar_formula_request import HostmapScalarFormulaRequest
    from datadog_api_client.v1_20270101.model.hostmap_group_by import HostmapGroupBy
    from datadog_api_client.v1_20270101.model.hostmap_node_type import HostmapNodeType
    from datadog_api_client.v1_20270101.model.hostmap_infrastructure_request_request_type import (
        HostmapInfrastructureRequestRequestType,
    )
    from datadog_api_client.v1_20270101.model.hostmap_style import HostmapStyle


class HostmapInfrastructureRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.threshold_formatting_rule import ThresholdFormattingRule
        from datadog_api_client.v1_20270101.model.hostmap_scalar_formula_request import HostmapScalarFormulaRequest
        from datadog_api_client.v1_20270101.model.hostmap_group_by import HostmapGroupBy
        from datadog_api_client.v1_20270101.model.hostmap_node_type import HostmapNodeType
        from datadog_api_client.v1_20270101.model.hostmap_infrastructure_request_request_type import (
            HostmapInfrastructureRequestRequestType,
        )
        from datadog_api_client.v1_20270101.model.hostmap_style import HostmapStyle

        return {
            "child": (HostmapInfrastructureRequest,),
            "conditional_formats": ([ThresholdFormattingRule],),
            "enrichments": ([HostmapScalarFormulaRequest],),
            "filter": (str,),
            "group_by": ([HostmapGroupBy],),
            "no_group_hosts": (bool,),
            "no_metric_hosts": (bool,),
            "node_type": (HostmapNodeType,),
            "request_type": (HostmapInfrastructureRequestRequestType,),
            "style": (HostmapStyle,),
        }

    attribute_map = {
        "child": "child",
        "conditional_formats": "conditional_formats",
        "enrichments": "enrichments",
        "filter": "filter",
        "group_by": "group_by",
        "no_group_hosts": "no_group_hosts",
        "no_metric_hosts": "no_metric_hosts",
        "node_type": "node_type",
        "request_type": "request_type",
        "style": "style",
    }

    def __init__(
        self_,
        enrichments: List[HostmapScalarFormulaRequest],
        node_type: HostmapNodeType,
        request_type: HostmapInfrastructureRequestRequestType,
        child: Union[HostmapInfrastructureRequest, UnsetType] = unset,
        conditional_formats: Union[List[ThresholdFormattingRule], UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        group_by: Union[List[HostmapGroupBy], UnsetType] = unset,
        no_group_hosts: Union[bool, UnsetType] = unset,
        no_metric_hosts: Union[bool, UnsetType] = unset,
        style: Union[HostmapStyle, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

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
        """
        if child is not unset:
            kwargs["child"] = child
        if conditional_formats is not unset:
            kwargs["conditional_formats"] = conditional_formats
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if no_group_hosts is not unset:
            kwargs["no_group_hosts"] = no_group_hosts
        if no_metric_hosts is not unset:
            kwargs["no_metric_hosts"] = no_metric_hosts
        if style is not unset:
            kwargs["style"] = style
        super().__init__(kwargs)

        self_.enrichments = enrichments
        self_.node_type = node_type
        self_.request_type = request_type
