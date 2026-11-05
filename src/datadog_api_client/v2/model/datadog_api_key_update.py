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
    from datadog_api_client.v2.model.datadog_api_key_update_api_key import DatadogAPIKeyUpdateApiKey
    from datadog_api_client.v2.model.datadog_api_key_update_app_key import DatadogAPIKeyUpdateAppKey
    from datadog_api_client.v2.model.datadog_api_key_update_datacenter import DatadogAPIKeyUpdateDatacenter
    from datadog_api_client.v2.model.datadog_api_key_subdomain import DatadogAPIKeySubdomain
    from datadog_api_client.v2.model.datadog_api_key_type import DatadogAPIKeyType
    from datadog_api_client.v2.model.action_connection_aws_secrets_manager_reference import (
        ActionConnectionAWSSecretsManagerReference,
    )


class DatadogAPIKeyUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_api_key_update_api_key import DatadogAPIKeyUpdateApiKey
        from datadog_api_client.v2.model.datadog_api_key_update_app_key import DatadogAPIKeyUpdateAppKey
        from datadog_api_client.v2.model.datadog_api_key_update_datacenter import DatadogAPIKeyUpdateDatacenter
        from datadog_api_client.v2.model.datadog_api_key_subdomain import DatadogAPIKeySubdomain
        from datadog_api_client.v2.model.datadog_api_key_type import DatadogAPIKeyType

        return {
            "api_key": (DatadogAPIKeyUpdateApiKey,),
            "app_key": (DatadogAPIKeyUpdateAppKey,),
            "datacenter": (DatadogAPIKeyUpdateDatacenter,),
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
        type: DatadogAPIKeyType,
        api_key: Union[DatadogAPIKeyUpdateApiKey, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        app_key: Union[DatadogAPIKeyUpdateAppKey, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        datacenter: Union[
            DatadogAPIKeyUpdateDatacenter, str, ActionConnectionAWSSecretsManagerReference, UnsetType
        ] = unset,
        subdomain: Union[DatadogAPIKeySubdomain, str, ActionConnectionAWSSecretsManagerReference, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``DatadogAPIKey`` object.

        :param api_key: The ``DatadogAPIKeyUpdate`` ``api_key``.
        :type api_key: DatadogAPIKeyUpdateApiKey, optional

        :param app_key: The ``DatadogAPIKeyUpdate`` ``app_key``.
        :type app_key: DatadogAPIKeyUpdateAppKey, optional

        :param datacenter: The ``DatadogAPIKeyUpdate`` ``datacenter``.
        :type datacenter: DatadogAPIKeyUpdateDatacenter, optional

        :param subdomain: Custom subdomain used for Datadog URLs generated with this Connection. For example, if this org uses ``https://acme.datadoghq.com`` to access Datadog, set this field to ``acme``. If this field is omitted, generated URLs will use the default site URL for its datacenter (see `https://docs.datadoghq.com/getting_started/site <https://docs.datadoghq.com/getting_started/site>`_ ).
        :type subdomain: DatadogAPIKeySubdomain, optional

        :param type: The definition of the ``DatadogAPIKey`` object.
        :type type: DatadogAPIKeyType
        """
        if api_key is not unset:
            kwargs["api_key"] = api_key
        if app_key is not unset:
            kwargs["app_key"] = app_key
        if datacenter is not unset:
            kwargs["datacenter"] = datacenter
        if subdomain is not unset:
            kwargs["subdomain"] = subdomain
        super().__init__(kwargs)

        self_.type = type
