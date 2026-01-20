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
    from datadog_api_client.v2.model.security_monitoring_suppression import SecurityMonitoringSuppression
    from datadog_api_client.v2.model.security_monitoring_suppressions_meta import SecurityMonitoringSuppressionsMeta


class SecurityMonitoringPaginatedSuppressionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_suppression import SecurityMonitoringSuppression
        from datadog_api_client.v2.model.security_monitoring_suppressions_meta import SecurityMonitoringSuppressionsMeta

        return {
            "data": ([SecurityMonitoringSuppression],),
            "meta": (SecurityMonitoringSuppressionsMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[SecurityMonitoringSuppression], UnsetType] = unset,
        meta: Union[SecurityMonitoringSuppressionsMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object containing the available suppression rules with pagination metadata.

        :param data: A list of suppressions objects.
        :type data: [SecurityMonitoringSuppression], optional

        :param meta: Metadata for the suppression list response.
        :type meta: SecurityMonitoringSuppressionsMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
