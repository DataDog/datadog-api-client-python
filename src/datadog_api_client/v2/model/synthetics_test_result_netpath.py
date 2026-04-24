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
    from datadog_api_client.v2.model.synthetics_test_result_netpath_destination import (
        SyntheticsTestResultNetpathDestination,
    )
    from datadog_api_client.v2.model.synthetics_test_result_netpath_hop import SyntheticsTestResultNetpathHop
    from datadog_api_client.v2.model.synthetics_test_result_netpath_endpoint import SyntheticsTestResultNetpathEndpoint


class SyntheticsTestResultNetpath(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_netpath_destination import (
            SyntheticsTestResultNetpathDestination,
        )
        from datadog_api_client.v2.model.synthetics_test_result_netpath_hop import SyntheticsTestResultNetpathHop
        from datadog_api_client.v2.model.synthetics_test_result_netpath_endpoint import (
            SyntheticsTestResultNetpathEndpoint,
        )

        return {
            "destination": (SyntheticsTestResultNetpathDestination,),
            "hops": ([SyntheticsTestResultNetpathHop],),
            "origin": (str,),
            "pathtrace_id": (str,),
            "protocol": (str,),
            "source": (SyntheticsTestResultNetpathEndpoint,),
            "tags": ([str],),
            "timestamp": (int,),
        }

    attribute_map = {
        "destination": "destination",
        "hops": "hops",
        "origin": "origin",
        "pathtrace_id": "pathtrace_id",
        "protocol": "protocol",
        "source": "source",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        destination: Union[SyntheticsTestResultNetpathDestination, UnsetType] = unset,
        hops: Union[List[SyntheticsTestResultNetpathHop], UnsetType] = unset,
        origin: Union[str, UnsetType] = unset,
        pathtrace_id: Union[str, UnsetType] = unset,
        protocol: Union[str, UnsetType] = unset,
        source: Union[SyntheticsTestResultNetpathEndpoint, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Network Path test result capturing the path between source and destination.

        :param destination: Destination endpoint of a network path measurement.
        :type destination: SyntheticsTestResultNetpathDestination, optional

        :param hops: Hops along the network path.
        :type hops: [SyntheticsTestResultNetpathHop], optional

        :param origin: Origin of the network path (for example, probe source).
        :type origin: str, optional

        :param pathtrace_id: Identifier of the path trace.
        :type pathtrace_id: str, optional

        :param protocol: Protocol used for the path trace (for example, ``tcp`` , ``udp`` , ``icmp`` ).
        :type protocol: str, optional

        :param source: Source endpoint of a network path measurement.
        :type source: SyntheticsTestResultNetpathEndpoint, optional

        :param tags: Tags associated with the network path measurement.
        :type tags: [str], optional

        :param timestamp: Unix timestamp (ms) of the network path measurement.
        :type timestamp: int, optional
        """
        if destination is not unset:
            kwargs["destination"] = destination
        if hops is not unset:
            kwargs["hops"] = hops
        if origin is not unset:
            kwargs["origin"] = origin
        if pathtrace_id is not unset:
            kwargs["pathtrace_id"] = pathtrace_id
        if protocol is not unset:
            kwargs["protocol"] = protocol
        if source is not unset:
            kwargs["source"] = source
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
