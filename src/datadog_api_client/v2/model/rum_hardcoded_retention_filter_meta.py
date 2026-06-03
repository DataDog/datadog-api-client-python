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
    from datadog_api_client.v2.model.rum_hardcoded_retention_filter_meta_source import (
        RumHardcodedRetentionFilterMetaSource,
    )


class RumHardcodedRetentionFilterMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_hardcoded_retention_filter_meta_source import (
            RumHardcodedRetentionFilterMetaSource,
        )

        return {
            "source": (RumHardcodedRetentionFilterMetaSource,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "source": "source",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        source: Union[RumHardcodedRetentionFilterMetaSource, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updated_by_handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the hardcoded retention filter.

        :param source: The source of the last update to a hardcoded retention filter.
        :type source: RumHardcodedRetentionFilterMetaSource, optional

        :param updated_at: Unix epoch (in milliseconds) of the last update.
        :type updated_at: int, optional

        :param updated_by_handle: Handle of the user who last updated the filter.
        :type updated_by_handle: str, optional
        """
        if source is not unset:
            kwargs["source"] = source
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by_handle is not unset:
            kwargs["updated_by_handle"] = updated_by_handle
        super().__init__(kwargs)
