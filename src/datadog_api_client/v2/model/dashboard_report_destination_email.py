# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DashboardReportDestinationEmail(ModelNormal):
    validations = {
        "recipient_addresses": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "recipient_addresses": ([str],),
        }

    attribute_map = {
        "recipient_addresses": "recipient_addresses",
    }

    def __init__(self_, recipient_addresses: Union[List[str], UnsetType] = unset, **kwargs):
        """
        Email destinations for a report.

        :param recipient_addresses: List of email addresses to send reports to.
        :type recipient_addresses: [str], optional
        """
        if recipient_addresses is not unset:
            kwargs["recipient_addresses"] = recipient_addresses
        super().__init__(kwargs)
