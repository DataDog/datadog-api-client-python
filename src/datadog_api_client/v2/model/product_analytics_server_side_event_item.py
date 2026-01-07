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
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_account import (
        ProductAnalyticsServerSideEventItemAccount,
    )
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_application import (
        ProductAnalyticsServerSideEventItemApplication,
    )
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_event import (
        ProductAnalyticsServerSideEventItemEvent,
    )
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_session import (
        ProductAnalyticsServerSideEventItemSession,
    )
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_type import (
        ProductAnalyticsServerSideEventItemType,
    )
    from datadog_api_client.v2.model.product_analytics_server_side_event_item_usr import (
        ProductAnalyticsServerSideEventItemUsr,
    )


class ProductAnalyticsServerSideEventItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_account import (
            ProductAnalyticsServerSideEventItemAccount,
        )
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_application import (
            ProductAnalyticsServerSideEventItemApplication,
        )
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_event import (
            ProductAnalyticsServerSideEventItemEvent,
        )
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_session import (
            ProductAnalyticsServerSideEventItemSession,
        )
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_type import (
            ProductAnalyticsServerSideEventItemType,
        )
        from datadog_api_client.v2.model.product_analytics_server_side_event_item_usr import (
            ProductAnalyticsServerSideEventItemUsr,
        )

        return {
            "account": (ProductAnalyticsServerSideEventItemAccount,),
            "application": (ProductAnalyticsServerSideEventItemApplication,),
            "event": (ProductAnalyticsServerSideEventItemEvent,),
            "session": (ProductAnalyticsServerSideEventItemSession,),
            "type": (ProductAnalyticsServerSideEventItemType,),
            "usr": (ProductAnalyticsServerSideEventItemUsr,),
        }

    attribute_map = {
        "account": "account",
        "application": "application",
        "event": "event",
        "session": "session",
        "type": "type",
        "usr": "usr",
    }

    def __init__(
        self_,
        application: ProductAnalyticsServerSideEventItemApplication,
        event: ProductAnalyticsServerSideEventItemEvent,
        type: ProductAnalyticsServerSideEventItemType,
        account: Union[ProductAnalyticsServerSideEventItemAccount, UnsetType] = unset,
        session: Union[ProductAnalyticsServerSideEventItemSession, UnsetType] = unset,
        usr: Union[ProductAnalyticsServerSideEventItemUsr, UnsetType] = unset,
        **kwargs,
    ):
        """
        A Product Analytics server-side event.

        :param account: The account linked to your event.
        :type account: ProductAnalyticsServerSideEventItemAccount, optional

        :param application: The application in which you want to send your events.
        :type application: ProductAnalyticsServerSideEventItemApplication

        :param event: Fields used for the event.
        :type event: ProductAnalyticsServerSideEventItemEvent

        :param session: The session linked to your event.
        :type session: ProductAnalyticsServerSideEventItemSession, optional

        :param type: The type of Product Analytics event. Must be ``server`` for server-side events.
        :type type: ProductAnalyticsServerSideEventItemType

        :param usr: The user linked to your event.
        :type usr: ProductAnalyticsServerSideEventItemUsr, optional
        """
        if account is not unset:
            kwargs["account"] = account
        if session is not unset:
            kwargs["session"] = session
        if usr is not unset:
            kwargs["usr"] = usr
        super().__init__(kwargs)

        self_.application = application
        self_.event = event
        self_.type = type
