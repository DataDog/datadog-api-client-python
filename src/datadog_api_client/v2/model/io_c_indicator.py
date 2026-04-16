# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.io_c_geo_location import IoCGeoLocation
    from datadog_api_client.v2.model.io_c_source import IoCSource
    from datadog_api_client.v2.model.io_c_score_effect import IoCScoreEffect


class IoCIndicator(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_geo_location import IoCGeoLocation
        from datadog_api_client.v2.model.io_c_source import IoCSource
        from datadog_api_client.v2.model.io_c_score_effect import IoCScoreEffect

        return {
            "as_geo": (IoCGeoLocation,),
            "as_type": (str,),
            "benign_sources": ([IoCSource], none_type),
            "categories": ([str],),
            "first_seen": (datetime,),
            "id": (str,),
            "indicator": (str,),
            "indicator_type": (str,),
            "last_seen": (datetime,),
            "log_matches": (int,),
            "m_as_type": (IoCScoreEffect,),
            "m_persistence": (IoCScoreEffect,),
            "m_signal": (IoCScoreEffect,),
            "m_sources": (IoCScoreEffect,),
            "malicious_sources": ([IoCSource], none_type),
            "max_trust_score": (IoCScoreEffect,),
            "score": (float,),
            "signal_matches": (int,),
            "signal_tier": (int,),
            "suspicious_sources": ([IoCSource], none_type),
            "tags": ([str],),
        }

    attribute_map = {
        "as_geo": "as_geo",
        "as_type": "as_type",
        "benign_sources": "benign_sources",
        "categories": "categories",
        "first_seen": "first_seen",
        "id": "id",
        "indicator": "indicator",
        "indicator_type": "indicator_type",
        "last_seen": "last_seen",
        "log_matches": "log_matches",
        "m_as_type": "m_as_type",
        "m_persistence": "m_persistence",
        "m_signal": "m_signal",
        "m_sources": "m_sources",
        "malicious_sources": "malicious_sources",
        "max_trust_score": "max_trust_score",
        "score": "score",
        "signal_matches": "signal_matches",
        "signal_tier": "signal_tier",
        "suspicious_sources": "suspicious_sources",
        "tags": "tags",
    }

    def __init__(
        self_,
        as_geo: Union[IoCGeoLocation, UnsetType] = unset,
        as_type: Union[str, UnsetType] = unset,
        benign_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        categories: Union[List[str], UnsetType] = unset,
        first_seen: Union[datetime, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        indicator: Union[str, UnsetType] = unset,
        indicator_type: Union[str, UnsetType] = unset,
        last_seen: Union[datetime, UnsetType] = unset,
        log_matches: Union[int, UnsetType] = unset,
        m_as_type: Union[IoCScoreEffect, UnsetType] = unset,
        m_persistence: Union[IoCScoreEffect, UnsetType] = unset,
        m_signal: Union[IoCScoreEffect, UnsetType] = unset,
        m_sources: Union[IoCScoreEffect, UnsetType] = unset,
        malicious_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        max_trust_score: Union[IoCScoreEffect, UnsetType] = unset,
        score: Union[float, UnsetType] = unset,
        signal_matches: Union[int, UnsetType] = unset,
        signal_tier: Union[int, UnsetType] = unset,
        suspicious_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        An indicator of compromise with threat intelligence data.

        :param as_geo: Geographic location information for an IP indicator.
        :type as_geo: IoCGeoLocation, optional

        :param as_type: Autonomous system type.
        :type as_type: str, optional

        :param benign_sources: Threat intelligence sources that flagged this indicator as benign.
        :type benign_sources: [IoCSource], none_type, optional

        :param categories: Threat categories associated with the indicator.
        :type categories: [str], optional

        :param first_seen: Timestamp when the indicator was first seen.
        :type first_seen: datetime, optional

        :param id: Unique identifier for the indicator.
        :type id: str, optional

        :param indicator: The indicator value (for example, an IP address or domain).
        :type indicator: str, optional

        :param indicator_type: Type of indicator (for example, IP address or domain).
        :type indicator_type: str, optional

        :param last_seen: Timestamp when the indicator was last seen.
        :type last_seen: datetime, optional

        :param log_matches: Number of logs that matched this indicator.
        :type log_matches: int, optional

        :param m_as_type: Effect of a scoring factor on the indicator's threat score.
        :type m_as_type: IoCScoreEffect, optional

        :param m_persistence: Effect of a scoring factor on the indicator's threat score.
        :type m_persistence: IoCScoreEffect, optional

        :param m_signal: Effect of a scoring factor on the indicator's threat score.
        :type m_signal: IoCScoreEffect, optional

        :param m_sources: Effect of a scoring factor on the indicator's threat score.
        :type m_sources: IoCScoreEffect, optional

        :param malicious_sources: Threat intelligence sources that flagged this indicator as malicious.
        :type malicious_sources: [IoCSource], none_type, optional

        :param max_trust_score: Effect of a scoring factor on the indicator's threat score.
        :type max_trust_score: IoCScoreEffect, optional

        :param score: Threat score for the indicator (0-100).
        :type score: float, optional

        :param signal_matches: Number of security signals that matched this indicator.
        :type signal_matches: int, optional

        :param signal_tier: Signal tier level.
        :type signal_tier: int, optional

        :param suspicious_sources: Threat intelligence sources that flagged this indicator as suspicious.
        :type suspicious_sources: [IoCSource], none_type, optional

        :param tags: Tags associated with the indicator.
        :type tags: [str], optional
        """
        if as_geo is not unset:
            kwargs["as_geo"] = as_geo
        if as_type is not unset:
            kwargs["as_type"] = as_type
        if benign_sources is not unset:
            kwargs["benign_sources"] = benign_sources
        if categories is not unset:
            kwargs["categories"] = categories
        if first_seen is not unset:
            kwargs["first_seen"] = first_seen
        if id is not unset:
            kwargs["id"] = id
        if indicator is not unset:
            kwargs["indicator"] = indicator
        if indicator_type is not unset:
            kwargs["indicator_type"] = indicator_type
        if last_seen is not unset:
            kwargs["last_seen"] = last_seen
        if log_matches is not unset:
            kwargs["log_matches"] = log_matches
        if m_as_type is not unset:
            kwargs["m_as_type"] = m_as_type
        if m_persistence is not unset:
            kwargs["m_persistence"] = m_persistence
        if m_signal is not unset:
            kwargs["m_signal"] = m_signal
        if m_sources is not unset:
            kwargs["m_sources"] = m_sources
        if malicious_sources is not unset:
            kwargs["malicious_sources"] = malicious_sources
        if max_trust_score is not unset:
            kwargs["max_trust_score"] = max_trust_score
        if score is not unset:
            kwargs["score"] = score
        if signal_matches is not unset:
            kwargs["signal_matches"] = signal_matches
        if signal_tier is not unset:
            kwargs["signal_tier"] = signal_tier
        if suspicious_sources is not unset:
            kwargs["suspicious_sources"] = suspicious_sources
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
