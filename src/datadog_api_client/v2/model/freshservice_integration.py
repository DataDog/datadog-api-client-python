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
    from datadog_api_client.v2.model.freshservice_credentials import FreshserviceCredentials
    from datadog_api_client.v2.model.freshservice_integration_type import FreshserviceIntegrationType
    from datadog_api_client.v2.model.freshservice_api_key import FreshserviceAPIKey


class FreshserviceIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.freshservice_credentials import FreshserviceCredentials
        from datadog_api_client.v2.model.freshservice_integration_type import FreshserviceIntegrationType

        return {
            "credentials": (FreshserviceCredentials,),
            "type": (FreshserviceIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        credentials: Union[FreshserviceCredentials, FreshserviceAPIKey],
        type: FreshserviceIntegrationType,
        **kwargs,
    ):
        """
        The definition of the ``FreshserviceIntegration`` object.

        :param credentials: The definition of the ``FreshserviceCredentials`` object.
        :type credentials: FreshserviceCredentials

        :param type: The definition of the ``FreshserviceIntegrationType`` object.
        :type type: FreshserviceIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
