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
    from datadog_api_client.v2.model.segment_data_attributes_data_query_event_platform_items import (
        SegmentDataAttributesDataQueryEventPlatformItems,
    )
    from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items import (
        SegmentDataAttributesDataQueryReferenceTableItems,
    )
    from datadog_api_client.v2.model.segment_data_attributes_data_query_static_items import (
        SegmentDataAttributesDataQueryStaticItems,
    )
    from datadog_api_client.v2.model.segment_data_attributes_data_query_user_store_items import (
        SegmentDataAttributesDataQueryUserStoreItems,
    )


class SegmentDataAttributesDataQuery(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.segment_data_attributes_data_query_event_platform_items import (
            SegmentDataAttributesDataQueryEventPlatformItems,
        )
        from datadog_api_client.v2.model.segment_data_attributes_data_query_reference_table_items import (
            SegmentDataAttributesDataQueryReferenceTableItems,
        )
        from datadog_api_client.v2.model.segment_data_attributes_data_query_static_items import (
            SegmentDataAttributesDataQueryStaticItems,
        )
        from datadog_api_client.v2.model.segment_data_attributes_data_query_user_store_items import (
            SegmentDataAttributesDataQueryUserStoreItems,
        )

        return {
            "combination": (str,),
            "event_platform": ([SegmentDataAttributesDataQueryEventPlatformItems],),
            "reference_table": ([SegmentDataAttributesDataQueryReferenceTableItems],),
            "static": ([SegmentDataAttributesDataQueryStaticItems],),
            "user_store": ([SegmentDataAttributesDataQueryUserStoreItems],),
        }

    attribute_map = {
        "combination": "combination",
        "event_platform": "event_platform",
        "reference_table": "reference_table",
        "static": "static",
        "user_store": "user_store",
    }

    def __init__(
        self_,
        combination: Union[str, UnsetType] = unset,
        event_platform: Union[List[SegmentDataAttributesDataQueryEventPlatformItems], UnsetType] = unset,
        reference_table: Union[List[SegmentDataAttributesDataQueryReferenceTableItems], UnsetType] = unset,
        static: Union[List[SegmentDataAttributesDataQueryStaticItems], UnsetType] = unset,
        user_store: Union[List[SegmentDataAttributesDataQueryUserStoreItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param combination:
        :type combination: str, optional

        :param event_platform:
        :type event_platform: [SegmentDataAttributesDataQueryEventPlatformItems], optional

        :param reference_table:
        :type reference_table: [SegmentDataAttributesDataQueryReferenceTableItems], optional

        :param static:
        :type static: [SegmentDataAttributesDataQueryStaticItems], optional

        :param user_store:
        :type user_store: [SegmentDataAttributesDataQueryUserStoreItems], optional
        """
        if combination is not unset:
            kwargs["combination"] = combination
        if event_platform is not unset:
            kwargs["event_platform"] = event_platform
        if reference_table is not unset:
            kwargs["reference_table"] = reference_table
        if static is not unset:
            kwargs["static"] = static
        if user_store is not unset:
            kwargs["user_store"] = user_store
        super().__init__(kwargs)
