# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_basic_auth_instance import ServiceNowBasicAuthInstance
    from datadog_api_client.v2.model.service_now_basic_auth_password import ServiceNowBasicAuthPassword
    from datadog_api_client.v2.model.service_now_basic_auth_type import ServiceNowBasicAuthType
    from datadog_api_client.v2.model.service_now_basic_auth_username import ServiceNowBasicAuthUsername
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class ServiceNowBasicAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_basic_auth_instance import ServiceNowBasicAuthInstance
        from datadog_api_client.v2.model.service_now_basic_auth_password import ServiceNowBasicAuthPassword
        from datadog_api_client.v2.model.service_now_basic_auth_type import ServiceNowBasicAuthType
        from datadog_api_client.v2.model.service_now_basic_auth_username import ServiceNowBasicAuthUsername

        return {
            "instance": (ServiceNowBasicAuthInstance,),
            "password": (ServiceNowBasicAuthPassword,),
            "type": (ServiceNowBasicAuthType,),
            "username": (ServiceNowBasicAuthUsername,),
        }

    attribute_map = {
        "instance": "instance",
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(
        self_,
        instance: Union[ServiceNowBasicAuthInstance, str, ActionConnectionAWSSecretsManagerReference],
        password: Union[ServiceNowBasicAuthPassword, str, ActionConnectionAWSSecretsManagerReference],
        type: ServiceNowBasicAuthType,
        username: Union[ServiceNowBasicAuthUsername, str, ActionConnectionAWSSecretsManagerReference],
        **kwargs,
    ):
        """
        The definition of the ``ServiceNowBasicAuth`` object.

        :param instance: The ``ServiceNowBasicAuth`` ``instance``.
        :type instance: ServiceNowBasicAuthInstance

        :param password: The ``ServiceNowBasicAuth`` ``password``.
        :type password: ServiceNowBasicAuthPassword

        :param type: The definition of the ``ServiceNowBasicAuth`` object.
        :type type: ServiceNowBasicAuthType

        :param username: The ``ServiceNowBasicAuth`` ``username``.
        :type username: ServiceNowBasicAuthUsername
        """
        super().__init__(kwargs)

        self_.instance = instance
        self_.password = password
        self_.type = type
        self_.username = username
