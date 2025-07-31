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
    from datadog_api_client.v2.model.split_credentials import SplitCredentials
    from datadog_api_client.v2.model.split_integration_type import SplitIntegrationType
    from datadog_api_client.v2.model.split_api_key import SplitAPIKey


class SplitIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.split_credentials import SplitCredentials
        from datadog_api_client.v2.model.split_integration_type import SplitIntegrationType

        return {
            "credentials": (SplitCredentials,),
            "type": (SplitIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[SplitCredentials, SplitAPIKey], type: SplitIntegrationType, **kwargs):
        """
        The definition of the ``SplitIntegration`` object.

        :param credentials: The definition of the ``SplitCredentials`` object.
        :type credentials: SplitCredentials

        :param type: The definition of the ``SplitIntegrationType`` object.
        :type type: SplitIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
