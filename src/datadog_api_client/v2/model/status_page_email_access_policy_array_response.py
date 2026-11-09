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
    from datadog_api_client.v2.model.status_page_email_access_policy_data import StatusPageEmailAccessPolicyData
    from datadog_api_client.v2.model.status_page_email_access_policy_included import StatusPageEmailAccessPolicyIncluded
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded


class StatusPageEmailAccessPolicyArrayResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_page_email_access_policy_data import StatusPageEmailAccessPolicyData
        from datadog_api_client.v2.model.status_page_email_access_policy_included import (
            StatusPageEmailAccessPolicyIncluded,
        )

        return {
            "data": ([StatusPageEmailAccessPolicyData],),
            "included": ([StatusPageEmailAccessPolicyIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[StatusPageEmailAccessPolicyData],
        included: Union[
            List[Union[StatusPageEmailAccessPolicyIncluded, StatusPagesUser, StatusPageAsIncluded]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response object for a list of status page email access policies.

        :param data: A list of status page email access policy data objects.
        :type data: [StatusPageEmailAccessPolicyData]

        :param included: Resources related to the email access policies, when requested using the ``include`` query parameter.
        :type included: [StatusPageEmailAccessPolicyIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
