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
    from datadog_api_client.v2.model.io_c_geo_location import IoCGeoLocation
    from datadog_api_client.v2.model.io_c_source import IoCSource
    from datadog_api_client.v2.model.io_c_score_effect import IoCScoreEffect
    from datadog_api_client.v2.model.io_c_signal_severity_count import IoCSignalSeverityCount


class IoCIndicatorDetailed(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.io_c_geo_location import IoCGeoLocation
        from datadog_api_client.v2.model.io_c_source import IoCSource
        from datadog_api_client.v2.model.io_c_score_effect import IoCScoreEffect
        from datadog_api_client.v2.model.io_c_signal_severity_count import IoCSignalSeverityCount

        return {
            "additional_data": (
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
            "as_cidr_block": (str,),
            "as_geo": (IoCGeoLocation,),
            "as_number": (str,),
            "as_organization": (str,),
            "as_type": (str,),
            "benign_sources": ([IoCSource], none_type),
            "categories": ([str],),
            "critical_assets": ([str],),
            "first_seen": (datetime,),
            "hosts": ([str],),
            "id": (str,),
            "indicator": (str,),
            "indicator_type": (str,),
            "last_seen": (datetime,),
            "log_matches": (int,),
            "log_sources": ([str],),
            "m_as_type": (IoCScoreEffect,),
            "m_persistence": (IoCScoreEffect,),
            "m_signal": (IoCScoreEffect,),
            "m_sources": (IoCScoreEffect,),
            "malicious_sources": ([IoCSource], none_type),
            "max_trust_score": (IoCScoreEffect,),
            "score": (float,),
            "services": ([str],),
            "signal_matches": (int,),
            "signal_severity": ([IoCSignalSeverityCount],),
            "signal_tier": (int,),
            "suspicious_sources": ([IoCSource], none_type),
            "tags": ([str],),
            "users": ({str: ([str],)},),
        }

    attribute_map = {
        "additional_data": "additional_data",
        "as_cidr_block": "as_cidr_block",
        "as_geo": "as_geo",
        "as_number": "as_number",
        "as_organization": "as_organization",
        "as_type": "as_type",
        "benign_sources": "benign_sources",
        "categories": "categories",
        "critical_assets": "critical_assets",
        "first_seen": "first_seen",
        "hosts": "hosts",
        "id": "id",
        "indicator": "indicator",
        "indicator_type": "indicator_type",
        "last_seen": "last_seen",
        "log_matches": "log_matches",
        "log_sources": "log_sources",
        "m_as_type": "m_as_type",
        "m_persistence": "m_persistence",
        "m_signal": "m_signal",
        "m_sources": "m_sources",
        "malicious_sources": "malicious_sources",
        "max_trust_score": "max_trust_score",
        "score": "score",
        "services": "services",
        "signal_matches": "signal_matches",
        "signal_severity": "signal_severity",
        "signal_tier": "signal_tier",
        "suspicious_sources": "suspicious_sources",
        "tags": "tags",
        "users": "users",
    }

    def __init__(
        self_,
        additional_data: Union[Dict[str, Any], UnsetType] = unset,
        as_cidr_block: Union[str, UnsetType] = unset,
        as_geo: Union[IoCGeoLocation, UnsetType] = unset,
        as_number: Union[str, UnsetType] = unset,
        as_organization: Union[str, UnsetType] = unset,
        as_type: Union[str, UnsetType] = unset,
        benign_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        categories: Union[List[str], UnsetType] = unset,
        critical_assets: Union[List[str], UnsetType] = unset,
        first_seen: Union[datetime, UnsetType] = unset,
        hosts: Union[List[str], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        indicator: Union[str, UnsetType] = unset,
        indicator_type: Union[str, UnsetType] = unset,
        last_seen: Union[datetime, UnsetType] = unset,
        log_matches: Union[int, UnsetType] = unset,
        log_sources: Union[List[str], UnsetType] = unset,
        m_as_type: Union[IoCScoreEffect, UnsetType] = unset,
        m_persistence: Union[IoCScoreEffect, UnsetType] = unset,
        m_signal: Union[IoCScoreEffect, UnsetType] = unset,
        m_sources: Union[IoCScoreEffect, UnsetType] = unset,
        malicious_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        max_trust_score: Union[IoCScoreEffect, UnsetType] = unset,
        score: Union[float, UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        signal_matches: Union[int, UnsetType] = unset,
        signal_severity: Union[List[IoCSignalSeverityCount], UnsetType] = unset,
        signal_tier: Union[int, UnsetType] = unset,
        suspicious_sources: Union[List[IoCSource], none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        users: Union[Dict[str, List[str]], UnsetType] = unset,
        **kwargs,
    ):
        """
        An indicator of compromise with extended context from your environment.

        :param additional_data: Additional domain-specific context from threat intelligence sources.
        :type additional_data: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param as_cidr_block: Autonomous system CIDR block.
        :type as_cidr_block: str, optional

        :param as_geo: Geographic location information for an IP indicator.
        :type as_geo: IoCGeoLocation, optional

        :param as_number: Autonomous system number.
        :type as_number: str, optional

        :param as_organization: Autonomous system organization name.
        :type as_organization: str, optional

        :param as_type: Autonomous system type.
        :type as_type: str, optional

        :param benign_sources: Threat intelligence sources that flagged this indicator as benign.
        :type benign_sources: [IoCSource], none_type, optional

        :param categories: Threat categories associated with the indicator.
        :type categories: [str], optional

        :param critical_assets: Critical assets associated with this indicator.
        :type critical_assets: [str], optional

        :param first_seen: Timestamp when the indicator was first seen.
        :type first_seen: datetime, optional

        :param hosts: Hosts associated with this indicator.
        :type hosts: [str], optional

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

        :param log_sources: Log sources where this indicator was observed.
        :type log_sources: [str], optional

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

        :param services: Services where this indicator was observed.
        :type services: [str], optional

        :param signal_matches: Number of security signals that matched this indicator.
        :type signal_matches: int, optional

        :param signal_severity: Breakdown of security signals by severity.
        :type signal_severity: [IoCSignalSeverityCount], optional

        :param signal_tier: Signal tier level.
        :type signal_tier: int, optional

        :param suspicious_sources: Threat intelligence sources that flagged this indicator as suspicious.
        :type suspicious_sources: [IoCSource], none_type, optional

        :param tags: Tags associated with the indicator.
        :type tags: [str], optional

        :param users: Users associated with this indicator, grouped by category.
        :type users: {str: ([str],)}, optional
        """
        if additional_data is not unset:
            kwargs["additional_data"] = additional_data
        if as_cidr_block is not unset:
            kwargs["as_cidr_block"] = as_cidr_block
        if as_geo is not unset:
            kwargs["as_geo"] = as_geo
        if as_number is not unset:
            kwargs["as_number"] = as_number
        if as_organization is not unset:
            kwargs["as_organization"] = as_organization
        if as_type is not unset:
            kwargs["as_type"] = as_type
        if benign_sources is not unset:
            kwargs["benign_sources"] = benign_sources
        if categories is not unset:
            kwargs["categories"] = categories
        if critical_assets is not unset:
            kwargs["critical_assets"] = critical_assets
        if first_seen is not unset:
            kwargs["first_seen"] = first_seen
        if hosts is not unset:
            kwargs["hosts"] = hosts
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
        if log_sources is not unset:
            kwargs["log_sources"] = log_sources
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
        if services is not unset:
            kwargs["services"] = services
        if signal_matches is not unset:
            kwargs["signal_matches"] = signal_matches
        if signal_severity is not unset:
            kwargs["signal_severity"] = signal_severity
        if signal_tier is not unset:
            kwargs["signal_tier"] = signal_tier
        if suspicious_sources is not unset:
            kwargs["suspicious_sources"] = suspicious_sources
        if tags is not unset:
            kwargs["tags"] = tags
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
