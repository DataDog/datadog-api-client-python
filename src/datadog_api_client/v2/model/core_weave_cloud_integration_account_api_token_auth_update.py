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
    from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
        CoreWeaveCloudIntegrationAccountAPITokenAuthType,
    )


class CoreWeaveCloudIntegrationAccountAPITokenAuthUpdate(ModelNormal):
    validations = {
        "api_token": {},
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.core_weave_cloud_integration_account_api_token_auth_type import (
            CoreWeaveCloudIntegrationAccountAPITokenAuthType,
        )

        return {
            "api_token": (str,),
            "auth_type": (CoreWeaveCloudIntegrationAccountAPITokenAuthType,),
        }

    attribute_map = {
        "api_token": "api_token",
        "auth_type": "auth_type",
    }

    def __init__(
        self_,
        auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType,
        api_token: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        API token authentication, the only method CoreWeave integration accounts support. Only the fields provided are changed; omit ``api_token`` to keep the stored one.

        :param api_token: Secret CoreWeave API access token used to authenticate with CoreWeave. It cannot be cleared; sending ``null`` or an empty string is rejected with a ``422`` response.
        :type api_token: str, optional

        :param auth_type: The authentication method type.
        :type auth_type: CoreWeaveCloudIntegrationAccountAPITokenAuthType
        """
        if api_token is not unset:
            kwargs["api_token"] = api_token
        super().__init__(kwargs)

        self_.auth_type = auth_type
