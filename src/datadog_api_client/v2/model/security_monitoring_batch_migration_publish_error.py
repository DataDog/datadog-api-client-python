# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_error_detail import (
        SecurityMonitoringBatchMigrationPublishErrorDetail,
    )


class SecurityMonitoringBatchMigrationPublishError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_batch_migration_publish_error_detail import (
            SecurityMonitoringBatchMigrationPublishErrorDetail,
        )

        return {
            "code": (str,),
            "details": ([SecurityMonitoringBatchMigrationPublishErrorDetail],),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "details": "details",
        "message": "message",
    }

    def __init__(
        self_,
        message: str,
        code: Union[str, UnsetType] = unset,
        details: Union[List[SecurityMonitoringBatchMigrationPublishErrorDetail], UnsetType] = unset,
        **kwargs,
    ):
        """
        The reason why the resource could not be published.

        :param code: The error code returned on rule creation.
        :type code: str, optional

        :param details: The rule validation errors returned on rule creation.
        :type details: [SecurityMonitoringBatchMigrationPublishErrorDetail], optional

        :param message: The error message.
        :type message: str
        """
        if code is not unset:
            kwargs["code"] = code
        if details is not unset:
            kwargs["details"] = details
        super().__init__(kwargs)

        self_.message = message
