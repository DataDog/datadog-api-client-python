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
    from datadog_api_client.v2.model.chat_gpt_enterprise_agent_console_integration_dataflow_request import (
        ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest,
    )
    from datadog_api_client.v2.model.chat_gpt_enterprise_cloud_cost_data_integration_dataflow_request import (
        ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest,
    )


class ChatGPTEnterpriseIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_gpt_enterprise_agent_console_integration_dataflow_request import (
            ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest,
        )
        from datadog_api_client.v2.model.chat_gpt_enterprise_cloud_cost_data_integration_dataflow_request import (
            ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest,
        )

        return {
            "chatgpt_enterprise_agent_console": (ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest,),
            "chatgpt_enterprise_cloud_cost_data": (ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest,),
        }

    attribute_map = {
        "chatgpt_enterprise_agent_console": "chatgpt-enterprise-agent-console",
        "chatgpt_enterprise_cloud_cost_data": "chatgpt-enterprise-cloud-cost-data",
    }

    def __init__(
        self_,
        chatgpt_enterprise_agent_console: Union[
            ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest, UnsetType
        ] = unset,
        chatgpt_enterprise_cloud_cost_data: Union[
            ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest, UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from ChatGPT Enterprise, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Every dataflow requires a ChatGPT Enterprise workspace with access to the OpenAI Costs API; a dataflow enabled without it is stored but collects no data.

        :param chatgpt_enterprise_agent_console: Activity, token consumption, credits, and estimated usage costs across ChatGPT Chat, ChatGPT Work, and Codex, shown in Agent Console with breakdowns by product, model, and user where OpenAI provides them. Data already available from OpenAI appears within 1 hour of enabling this dataflow.
        :type chatgpt_enterprise_agent_console: ChatGPTEnterpriseAgentConsoleIntegrationDataflowRequest, optional

        :param chatgpt_enterprise_cloud_cost_data: ChatGPT Enterprise costs from the OpenAI Costs API, so that ChatGPT Enterprise spend can be analyzed in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. These costs are excluded from Cloud Cost Management spend-monitored billing. Reported costs are estimates, not final invoice amounts.
        :type chatgpt_enterprise_cloud_cost_data: ChatGPTEnterpriseCloudCostDataIntegrationDataflowRequest, optional
        """
        if chatgpt_enterprise_agent_console is not unset:
            kwargs["chatgpt_enterprise_agent_console"] = chatgpt_enterprise_agent_console
        if chatgpt_enterprise_cloud_cost_data is not unset:
            kwargs["chatgpt_enterprise_cloud_cost_data"] = chatgpt_enterprise_cloud_cost_data
        super().__init__(kwargs)
