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
    from datadog_api_client.v2.model.datadog_api_key_api_key import DatadogAPIKeyApiKey
    from datadog_api_client.v2.model.datadog_api_key_app_key import DatadogAPIKeyAppKey
    from datadog_api_client.v2.model.datadog_api_key_datacenter import DatadogAPIKeyDatacenter
    from datadog_api_client.v2.model.datadog_api_key_subdomain import DatadogAPIKeySubdomain
    from datadog_api_client.v2.model.datadog_api_key_type import DatadogAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class DatadogAPIKey(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_api_key_api_key import DatadogAPIKeyApiKey
        from datadog_api_client.v2.model.datadog_api_key_app_key import DatadogAPIKeyAppKey
        from datadog_api_client.v2.model.datadog_api_key_datacenter import DatadogAPIKeyDatacenter
        from datadog_api_client.v2.model.datadog_api_key_subdomain import DatadogAPIKeySubdomain
        from datadog_api_client.v2.model.datadog_api_key_type import DatadogAPIKeyType

        return {
            "api_key": (DatadogAPIKeyApiKey,),
            "app_key": (DatadogAPIKeyAppKey,),
            "datacenter": (DatadogAPIKeyDatacenter,),
            "subdomain": (DatadogAPIKeySubdomain,),
            "type": (DatadogAPIKeyType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "app_key": "app_key",
        "datacenter": "datacenter",
        "subdomain": "subdomain",
        "type": "type",
    }

    def __init__(
        self_,
        api_key: Union[DatadogAPIKeyApiKey, str, ActionConnectionAWSSecretsManagerReference],
        app_key: Union[DatadogAPIKeyAppKey, str, ActionConnectionAWSSecretsManagerReference],
        datacenter: Union[DatadogAPIKeyDatacenter, str, ActionConnectionAWSSecretsManagerReference],
        type: DatadogAPIKeyType,
        subdomain: Union[DatadogAPIKeySubdomain, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``DatadogAPIKey`` object.

        :param api_key: The ``DatadogAPIKey`` ``api_key``.
        :type api_key: DatadogAPIKeyApiKey

        :param app_key: The ``DatadogAPIKey`` ``app_key``.
        :type app_key: DatadogAPIKeyAppKey

        :param datacenter: The ``DatadogAPIKey`` ``datacenter``.
        :type datacenter: DatadogAPIKeyDatacenter

        :param subdomain: Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses ``https://acme.datadoghq.com`` to access Datadog, set this field to ``acme``. If this field is omitted, generated URLs will use the default site URL for its datacenter (see `https://docs.datadoghq.com/getting_started/site <https://docs.datadoghq.com/getting_started/site>`_ ).
        :type subdomain: DatadogAPIKeySubdomain, optional

        :param type: The definition of the ``DatadogAPIKey`` object.
        :type type: DatadogAPIKeyType
        """
        if subdomain is not unset:
            kwargs["subdomain"] = subdomain
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.app_key = app_key
        self_.datacenter = datacenter
        self_.type = type
