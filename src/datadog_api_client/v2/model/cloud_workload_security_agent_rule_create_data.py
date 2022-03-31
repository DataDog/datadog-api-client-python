# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_create_attributes import (
        CloudWorkloadSecurityAgentRuleCreateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

    globals()["CloudWorkloadSecurityAgentRuleCreateAttributes"] = CloudWorkloadSecurityAgentRuleCreateAttributes
    globals()["CloudWorkloadSecurityAgentRuleType"] = CloudWorkloadSecurityAgentRuleType


class CloudWorkloadSecurityAgentRuleCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "attributes": (CloudWorkloadSecurityAgentRuleCreateAttributes,),
            "type": (CloudWorkloadSecurityAgentRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self, attributes, type, *args, **kwargs):
        """
        Object for a single Agent rule.

        :param attributes: Create a new Cloud Workload Security Agent rule.
        :type attributes: CloudWorkloadSecurityAgentRuleCreateAttributes

        :param type: The type of the resource. The value should always be `agent_rule`.
        :type type: CloudWorkloadSecurityAgentRuleType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CloudWorkloadSecurityAgentRuleCreateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.type = type
        return self
