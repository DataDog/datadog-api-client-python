# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_journey_conversion_type import (
        ProductAnalyticsJourneyConversionType,
    )


class SegmentJourneyBlock(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_conversion_type import (
            ProductAnalyticsJourneyConversionType,
        )

        return {
            "conversion_type": (ProductAnalyticsJourneyConversionType,),
            "exclude_anonymous_traffic": (bool,),
            "_from": (int,),
            "group_by": (
                [
                    {
                        str: (
                            bool,
                            date,
                            datetime,
                            dict,
                            float,
                            int,
                            list,
                            str,
                            UUID,
                            none_type,
                        )
                    }
                ],
            ),
            "name": (str,),
            "search": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "target": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "to": (int,),
        }

    attribute_map = {
        "conversion_type": "conversion_type",
        "exclude_anonymous_traffic": "exclude_anonymous_traffic",
        "_from": "from",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
        "target": "target",
        "to": "to",
    }

    def __init__(
        self_,
        conversion_type: Union[ProductAnalyticsJourneyConversionType, UnsetType] = unset,
        exclude_anonymous_traffic: Union[bool, UnsetType] = unset,
        _from: Union[int, UnsetType] = unset,
        group_by: Union[List[Dict[str, Any]], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        search: Union[Dict[str, Any], UnsetType] = unset,
        target: Union[Dict[str, Any], UnsetType] = unset,
        to: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Selects the users who converted or dropped off in a funnel.

        :param conversion_type: Whether to return the entities that converted at the target step, or those that dropped off.
        :type conversion_type: ProductAnalyticsJourneyConversionType, optional

        :param exclude_anonymous_traffic: Whether to leave out anonymous users.
        :type exclude_anonymous_traffic: bool, optional

        :param _from: Start of the time range, in epoch milliseconds.
        :type _from: int, optional

        :param group_by: Group-by definitions of the funnel query.
        :type group_by: [{str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}], optional

        :param name: Name of the block, used in ``combination``.
        :type name: str, optional

        :param search: Funnel search, with the same shape as the ``search`` of a Product Analytics journey query.
        :type search: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param target: Funnel step or step range to evaluate.
        :type target: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param to: End of the time range, in epoch milliseconds.
        :type to: int, optional
        """
        if conversion_type is not unset:
            kwargs["conversion_type"] = conversion_type
        if exclude_anonymous_traffic is not unset:
            kwargs["exclude_anonymous_traffic"] = exclude_anonymous_traffic
        if _from is not unset:
            kwargs["_from"] = _from
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if name is not unset:
            kwargs["name"] = name
        if search is not unset:
            kwargs["search"] = search
        if target is not unset:
            kwargs["target"] = target
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)
