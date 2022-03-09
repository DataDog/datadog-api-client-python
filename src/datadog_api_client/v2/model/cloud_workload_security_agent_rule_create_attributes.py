# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudWorkloadSecurityAgentRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "enabled": (bool,),
            "expression": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "expression": "expression",
        "name": "name",
    }

    def __init__(self, expression, name, *args, **kwargs):
        """
        Create a new Cloud Workload Security Agent rule.

        :param description: The description of the Agent rule.
        :type description: str, optional

        :param enabled: Whether the Agent rule is enabled.
        :type enabled: bool, optional

        :param expression: The SECL expression of the Agent rule.
        :type expression: str

        :param name: The name of the Agent rule.
        :type name: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.expression = expression
        self.name = name

    @classmethod
    def _from_openapi_data(cls, expression, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CloudWorkloadSecurityAgentRuleCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.expression = expression
        self.name = name
        return self
