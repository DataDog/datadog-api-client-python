# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudWorkloadSecurityAgentRuleUpdateAttributes(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "description": (str,),
            "enabled": (bool,),
            "expression": (str,),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "expression": "expression",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Update an existing Cloud Workload Security Agent rule.

        :param description: The description of the Agent rule.
        :type description: str, optional

        :param enabled: Whether the Agent rule is enabled.
        :type enabled: bool, optional

        :param expression: The SECL expression of the Agent rule.
        :type expression: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(CloudWorkloadSecurityAgentRuleUpdateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
