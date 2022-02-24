# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_attributes import (
        CloudWorkloadSecurityAgentRuleAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType

    globals()["CloudWorkloadSecurityAgentRuleAttributes"] = CloudWorkloadSecurityAgentRuleAttributes
    globals()["CloudWorkloadSecurityAgentRuleType"] = CloudWorkloadSecurityAgentRuleType


class CloudWorkloadSecurityAgentRuleData(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (CloudWorkloadSecurityAgentRuleAttributes,),
            "id": (str,),
            "type": (CloudWorkloadSecurityAgentRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Object for a single Agent rule.

        :param attributes: A Cloud Workload Security Agent rule returned by the API.
        :type attributes: CloudWorkloadSecurityAgentRuleAttributes, optional

        :param id: The ID of the Agent rule.
        :type id: str, optional

        :param type: The type of the resource. The value should always be `agent_rule`.
        :type type: CloudWorkloadSecurityAgentRuleType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CloudWorkloadSecurityAgentRuleData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
