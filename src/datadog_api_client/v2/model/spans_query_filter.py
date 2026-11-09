# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SpansQueryFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (str,),
            "query": (str,),
            "to": (str,),
        }

    attribute_map = {
        "_from": "from",
        "query": "query",
        "to": "to",
    }

    def __init__(
        self_,
        _from: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        to: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The search and filter query settings.

        :param _from: The minimum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type _from: str, optional

        :param query: The search query, following the
            `span search syntax <https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/>`_.
            Reserved fields ( ``service`` , ``env`` , ``version`` , ``resource_name`` , ``operation_name`` , ``status`` , ``span_id`` ,
            ``trace_id`` , ``type`` ) take no ``@`` prefix, and neither do tags such as ``host`` or primary tags such as
            ``datacenter``. Span attributes need one, for example ``@span.kind:server`` or ``@http.status_code:500``.
            Wrap values that contain special characters such as ``:`` , ``{`` , ``}`` , ``(`` , ``)`` , or spaces in double quotes,
            for example ``@http.route:"/api/v1/users/{id}"`` or ``resource_name:"GET /api/v1/users"``.
            Wildcards do not work inside quotes, so to combine a wildcard with special characters, escape each one
            with ``\\`` instead, for example ``resource_name:Clients\:\:*``.
        :type query: str, optional

        :param to: The maximum time for the requested spans, supports date-time ISO8601, date math, and regular timestamps (milliseconds).
        :type to: str, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if query is not unset:
            kwargs["query"] = query
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)
