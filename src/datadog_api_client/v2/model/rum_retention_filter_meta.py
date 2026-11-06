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
    from datadog_api_client.v2.model.rum_retention_filter_meta_edition_mode import RumRetentionFilterMetaEditionMode
    from datadog_api_client.v2.model.rum_retention_filter_meta_source import RumRetentionFilterMetaSource


class RumRetentionFilterMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_retention_filter_meta_edition_mode import RumRetentionFilterMetaEditionMode
        from datadog_api_client.v2.model.rum_retention_filter_meta_source import RumRetentionFilterMetaSource

        return {
            "edition_mode": (RumRetentionFilterMetaEditionMode,),
            "source": (RumRetentionFilterMetaSource,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "edition_mode": "edition_mode",
        "source": "source",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        edition_mode: Union[RumRetentionFilterMetaEditionMode, UnsetType] = unset,
        source: Union[RumRetentionFilterMetaSource, UnsetType] = unset,
        updated_at: Union[int, UnsetType] = unset,
        updated_by_handle: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about a RUM retention filter.

        :param edition_mode: Which attributes of the retention filter can be edited. `complete`: all attributes can be edited. `limited`: only the sample rates can be edited; the name, event type, and query are fixed and the filter cannot be reordered (for example, default filters). ``unknown`` : the edition mode is not set.
        :type edition_mode: RumRetentionFilterMetaEditionMode, optional

        :param source: The source of the last change to a RUM retention filter.
        :type source: RumRetentionFilterMetaSource, optional

        :param updated_at: The timestamp of the last update to the retention filter, in milliseconds since the Unix epoch.
        :type updated_at: int, optional

        :param updated_by_handle: The handle of the user who last updated the retention filter.
        :type updated_by_handle: str, optional
        """
        if edition_mode is not unset:
            kwargs["edition_mode"] = edition_mode
        if source is not unset:
            kwargs["source"] = source
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by_handle is not unset:
            kwargs["updated_by_handle"] = updated_by_handle
        super().__init__(kwargs)
