# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudWorkloadSecurityAgentRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_data import (
            CloudWorkloadSecurityAgentRuleCreateData,
        )

        return {
            "data": (CloudWorkloadSecurityAgentRuleCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, data, *args, **kwargs):
        """
        Request object that includes the Agent rule to create.

        :param data: Object for a single Agent rule.
        :type data: CloudWorkloadSecurityAgentRuleCreateData
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CloudWorkloadSecurityAgentRuleCreateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
