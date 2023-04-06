# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ServiceDefinitionV2Dot1Contact(ModelComposed):
    def __init__(self, **kwargs):
        """
        Service owner's contacts information.

        :param contact: Contact value.
        :type contact: str

        :param name: Contact email.
        :type name: str, optional

        :param type: Contact type.
        :type type: ServiceDefinitionV2Dot1EmailType
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
        from datadog_api_client.v2.model.service_definition_v2_dot1_email import ServiceDefinitionV2Dot1Email
        from datadog_api_client.v2.model.service_definition_v2_dot1_slack import ServiceDefinitionV2Dot1Slack

        return {
            "oneOf": [
                ServiceDefinitionV2Dot1Email,
                ServiceDefinitionV2Dot1Slack,
            ],
        }
