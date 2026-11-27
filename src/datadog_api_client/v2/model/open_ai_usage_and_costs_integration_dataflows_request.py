# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_request import (
        OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest,
    )


class OpenAIUsageAndCostsIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.open_ai_usage_and_costs_cloud_cost_data_integration_dataflow_request import (
            OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest,
        )

        return {
            "openai_cloud_cost_data": (OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest,),
        }

    attribute_map = {
        "openai_cloud_cost_data": "openai-cloud-cost-data",
    }

    def __init__(
        self_,
        openai_cloud_cost_data: Union[OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from OpenAI Usage and Costs, keyed by dataflow ID. Datadog always collects organization usage metrics. Each dataflow in this object adds another type of collection. Set ``enabled`` to start or stop a dataflow. The default for each dataflow applies when the account is created. On update, omitted fields keep their current values.

        :param openai_cloud_cost_data: OpenAI organization costs, which you can analyze in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. See `collected data <https://docs.datadoghq.com/cloud_cost_management/saas_costs/?tab=openai#data-collected>`_ for what is included. Cost data appears in Cloud Cost Management within 24 hours after you enable this dataflow.
        :type openai_cloud_cost_data: OpenAIUsageAndCostsCloudCostDataIntegrationDataflowRequest, optional
        """
        if openai_cloud_cost_data is not unset:
            kwargs["openai_cloud_cost_data"] = openai_cloud_cost_data
        super().__init__(kwargs)
