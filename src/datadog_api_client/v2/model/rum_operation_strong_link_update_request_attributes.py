# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_operation_strong_link_update_status import RUMOperationStrongLinkUpdateStatus


class RUMOperationStrongLinkUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_update_status import (
            RUMOperationStrongLinkUpdateStatus,
        )

        return {
            "status": (RUMOperationStrongLinkUpdateStatus,),
        }

    attribute_map = {
        "status": "status",
    }

    def __init__(self_, status: RUMOperationStrongLinkUpdateStatus, **kwargs):
        """
        Attributes for updating a RUM operation strong link.

        :param status: The status of a RUM operation strong link. Can only be set to ``CONFIRMED`` or ``REJECTED``.
        :type status: RUMOperationStrongLinkUpdateStatus
        """
        super().__init__(kwargs)

        self_.status = status
