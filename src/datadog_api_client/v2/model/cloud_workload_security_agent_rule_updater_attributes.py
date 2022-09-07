# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CloudWorkloadSecurityAgentRuleUpdaterAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "handle": "handle",
        "name": "name",
    }

    def __init__(self_, *args, **kwargs):
        """
        The attributes of the user who last updated the Agent rule.

        :param handle: The handle of the user.
        :type handle: str, optional

        :param name: The name of the user.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
