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
    from datadog_api_client.v2.model.freshservice_credentials_update import FreshserviceCredentialsUpdate
    from datadog_api_client.v2.model.freshservice_integration_type import FreshserviceIntegrationType
    from datadog_api_client.v2.model.freshservice_api_key_update import FreshserviceAPIKeyUpdate


class FreshserviceIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.freshservice_credentials_update import FreshserviceCredentialsUpdate
        from datadog_api_client.v2.model.freshservice_integration_type import FreshserviceIntegrationType

        return {
            "credentials": (FreshserviceCredentialsUpdate,),
            "type": (FreshserviceIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: FreshserviceIntegrationType,
        credentials: Union[FreshserviceCredentialsUpdate, FreshserviceAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``FreshserviceIntegrationUpdate`` object.

        :param credentials: The definition of the ``FreshserviceCredentialsUpdate`` object.
        :type credentials: FreshserviceCredentialsUpdate, optional

        :param type: The definition of the ``FreshserviceIntegrationType`` object.
        :type type: FreshserviceIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
