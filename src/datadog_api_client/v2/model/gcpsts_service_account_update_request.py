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
    from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import (
        GCPSTSServiceAccountUpdateRequestData,
    )


class GCPSTSServiceAccountUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcpsts_service_account_update_request_data import (
            GCPSTSServiceAccountUpdateRequestData,
        )

        return {
            "data": (GCPSTSServiceAccountUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GCPSTSServiceAccountUpdateRequestData, UnsetType] = unset, **kwargs):
        """
        Service account info.

        :param data: Data on your service account.
        :type data: GCPSTSServiceAccountUpdateRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
