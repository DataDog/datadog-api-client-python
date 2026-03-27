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
    from datadog_api_client.v2.model.synthetics_test_version_change_data import SyntheticsTestVersionChangeData
    from datadog_api_client.v2.model.synthetics_test_version_history_meta import SyntheticsTestVersionHistoryMeta


class SyntheticsTestVersionHistoryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_version_change_data import SyntheticsTestVersionChangeData
        from datadog_api_client.v2.model.synthetics_test_version_history_meta import SyntheticsTestVersionHistoryMeta

        return {
            "data": ([SyntheticsTestVersionChangeData],),
            "meta": (SyntheticsTestVersionHistoryMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[SyntheticsTestVersionChangeData], UnsetType] = unset,
        meta: Union[SyntheticsTestVersionHistoryMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing the paginated version history for a Synthetic test.

        :param data: List of version change records.
        :type data: [SyntheticsTestVersionChangeData], optional

        :param meta: Pagination metadata for a version history response.
        :type meta: SyntheticsTestVersionHistoryMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
