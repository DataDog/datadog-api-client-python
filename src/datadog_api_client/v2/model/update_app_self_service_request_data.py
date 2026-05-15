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
    from datadog_api_client.v2.model.update_app_self_service_request_data_attributes import (
        UpdateAppSelfServiceRequestDataAttributes,
    )
    from datadog_api_client.v2.model.app_self_service_type import AppSelfServiceType


class UpdateAppSelfServiceRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_self_service_request_data_attributes import (
            UpdateAppSelfServiceRequestDataAttributes,
        )
        from datadog_api_client.v2.model.app_self_service_type import AppSelfServiceType

        return {
            "attributes": (UpdateAppSelfServiceRequestDataAttributes,),
            "type": (AppSelfServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UpdateAppSelfServiceRequestDataAttributes, UnsetType] = unset,
        type: Union[AppSelfServiceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for updating an app's self-service status.

        :param attributes: Attributes for updating an app's self-service status.
        :type attributes: UpdateAppSelfServiceRequestDataAttributes, optional

        :param type: The self-service resource type.
        :type type: AppSelfServiceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
